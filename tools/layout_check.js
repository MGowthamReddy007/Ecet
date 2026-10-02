/*
 * layout_check.js — drives headless Chrome (via CDP, no npm deps) to find
 * horizontal-overflow / spacing issues across phone, tablet and desktop widths,
 * in both dark and light themes, on every app screen.
 *
 * Usage:  node tools/layout_check.js [baseUrl]
 */
const { spawn } = require("child_process");
const os = require("os");
const path = require("path");

const CHROME = process.env.CHROME ||
  "C:/Program Files/Google/Chrome/Application/chrome.exe";
const PORT = 9333;
const USER_DATA = path.join(os.tmpdir(), "ecet-layout-" + Date.now());
const BASE = process.argv[2] || "http://localhost:8000";
const WIDTHS = [320, 360, 414, 600, 768, 1024, 1280, 1440];
const SCREENS = ["login", "home", "practice", "progress", "impact", "mockstart", "mock", "result"];

const sleep = ms => new Promise(r => setTimeout(r, ms));

async function waitForChrome() {
  for (let i = 0; i < 80; i++) {
    try {
      const r = await fetch(`http://127.0.0.1:${PORT}/json/version`);
      if (r.ok) return;
    } catch (e) { /* not ready */ }
    await sleep(200);
  }
  throw new Error("Chrome did not start");
}

class CDP {
  constructor(ws) {
    this.ws = ws; this.id = 0; this.pending = new Map(); this.handlers = new Map();
    ws.onmessage = ev => {
      const m = JSON.parse(ev.data);
      if (m.id && this.pending.has(m.id)) {
        const { res, rej } = this.pending.get(m.id); this.pending.delete(m.id);
        m.error ? rej(new Error(JSON.stringify(m.error))) : res(m.result);
      } else if (m.method) {
        (this.handlers.get(m.method) || []).forEach(h => h(m.params));
      }
    };
  }
  send(method, params = {}) {
    const id = ++this.id;
    return new Promise((res, rej) => {
      this.pending.set(id, { res, rej });
      this.ws.send(JSON.stringify({ id, method, params }));
    });
  }
  on(method, h) {
    const a = this.handlers.get(method) || []; a.push(h); this.handlers.set(method, a);
  }
}

const MEASURE = `(() => {
  const vw = document.documentElement.clientWidth;
  const out = { vw, docScroll: document.documentElement.scrollWidth, docOver: document.documentElement.scrollWidth - vw, offenders: [] };
  const screen = document.querySelector('.screen.active');
  if (screen) {
    for (const el of screen.querySelectorAll('*')) {
      const r = el.getBoundingClientRect();
      if (r.width <= 0 || r.height <= 0) continue;
      let p = el, scrollable = false;
      while (p) { const s = getComputedStyle(p); if (s.overflowX === 'auto' || s.overflowX === 'scroll') { scrollable = true; break; } p = p.parentElement; }
      if (scrollable) continue;
      if (r.right > vw + 1 || r.left < -1) {
        out.offenders.push({ tag: el.tagName, cls: (el.className || '').toString().slice(0, 44), left: Math.round(r.left), right: Math.round(r.right), w: Math.round(r.width) });
      }
    }
  }
  out.offenders = out.offenders.slice(0, 10);
  // cramped tap targets (interactive elements smaller than 36px)
  out.tiny = [];
  if (screen) for (const el of screen.querySelectorAll('.btn, .opt, .seg-btn, .lb, #btnTheme')) {
    const r = el.getBoundingClientRect();
    if (r.width > 0 && r.height > 0 && r.height < 32) out.tiny.push(el.className + ' h=' + Math.round(r.height));
  }
  out.tiny = out.tiny.slice(0, 8);
  // clipped / overflowing text inside hidden-overflow boxes
  out.clipped = [];
  if (screen) for (const el of screen.querySelectorAll('*')) {
    const s = getComputedStyle(el);
    const hidesX = s.overflowX === 'hidden' || s.textOverflow === 'ellipsis';
    if (!hidesX) continue;
    if (el.clientWidth > 0 && el.scrollWidth > el.clientWidth + 2) {
      // ignore deliberate ellipsis on leaderboard names
      if (el.classList.contains('nm')) continue;
      out.clipped.push((el.className || el.tagName) + ' scroll=' + el.scrollWidth + ' client=' + el.clientWidth);
    }
  }
  out.clipped = out.clipped.slice(0, 8);
  return out;
})()`;

(async () => {
  const chrome = spawn(CHROME, [
    "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
    `--remote-debugging-port=${PORT}`, `--user-data-dir=${USER_DATA}`,
    "--window-size=1440,900", "about:blank",
  ], { stdio: "ignore" });

  try {
    await waitForChrome();
    const t = await (await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: "PUT" })).json();
    const ws = new WebSocket(t.webSocketDebuggerUrl);
    await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
    const cdp = new CDP(ws);
    await cdp.send("Page.enable");
    await cdp.send("Runtime.enable");
    await cdp.send("Console.enable").catch(() => {});

    const errors = [];
    cdp.on("Runtime.exceptionThrown", p => errors.push(p.exceptionDetails?.text + " " + (p.exceptionDetails?.exception?.description || "")));

    const evaluate = async (expr, awaitPromise = false) => {
      const r = await cdp.send("Runtime.evaluate", { expression: expr, awaitPromise, returnByValue: true });
      if (r.exceptionDetails) throw new Error(r.exceptionDetails.text + " :: " + (r.exceptionDetails.exception?.description || ""));
      return r.result.value;
    };

    const loaded = new Promise(res => cdp.on("Page.loadEventFired", res));

    let problems = 0;
    for (const theme of ["dark", "light"]) {
      for (const w of WIDTHS) {
        await cdp.send("Emulation.setDeviceMetricsOverride",
          { width: w, height: 900, deviceScaleFactor: 1, mobile: false });
        await cdp.send("Page.navigate", { url: BASE + "/" });
        await loaded.catch(() => {});
        await sleep(500);
        await evaluate(`localStorage.setItem('ecet-theme', ${JSON.stringify(theme)})`);
        await cdp.send("Page.navigate", { url: BASE + "/" });
        await sleep(600);

        // log in once we reach home
        await evaluate(`(async () => {
          document.getElementById('inName').value='Demo';
          document.getElementById('inRoll').value='DIP23-001';
          document.getElementById('inBranch').value='CSE';
          await login();
        })()`, true);
        await sleep(700);

        const seen = [];
        for (const s of SCREENS) {
          if (s === "mockstart") await evaluate(`openMockChooser()`);
          else if (s === "mock") { await evaluate(`startMock('quick')`); await sleep(600); }
          else if (s === "result") { await evaluate(`submitMock()`); await sleep(600); }
          else await evaluate(`go('tab-${s}')`);
          await sleep(650);
          const m = await evaluate(MEASURE);
          const info = await evaluate(`(() => { const el=document.querySelector('.screen.active'); return { id: el?el.id:'none', els: el?el.querySelectorAll('*').length:0, txt: el?el.innerText.replace(/\s+/g,' ').trim().length:0 }; })()`);
          seen.push(`${info.id}:${info.els}e/${info.txt}c`);
          const bad = m.docOver > 0 || m.offenders.length > 0;
          if (bad) {
            problems++;
            console.log(`\n[${theme} ${w}px ${s}] docScroll=${m.docScroll} vw=${m.vw} (over=${m.docOver})`);
            m.offenders.forEach(o => console.log(`   - ${o.tag}.${o.cls} left=${o.left} right=${o.right} w=${o.w}`));
          }
          if (m.tiny.length) { problems++; console.log(`[small taps ${theme} ${w}px ${s}] ${m.tiny.join(' | ')}`); }
          if (m.clipped.length) { problems++; console.log(`[clipped ${theme} ${w}px ${s}] ${m.clipped.join(' | ')}`); }
        }
        if (process.env.VERBOSE) console.log(`  ${theme} ${w}px -> ${seen.join("  ")}`);
      }
    }

    if (errors.length) {
      console.log("\nJS ERRORS (" + errors.length + "):");
      [...new Set(errors)].slice(0, 10).forEach(e => console.log("   " + e.slice(0, 200)));
    }
    console.log(problems ? `\nRESULT: ${problems} overflow issue(s) found.` : "\nRESULT: clean — no horizontal overflow anywhere.");
    ws.close();
  } finally {
    chrome.kill();
  }
})().catch(e => { console.error("FATAL", e); process.exit(1); });

"""
tutor.py — Bilingual AI explanations via local Ollama (gemma4:e4b).
Falls back to stored explanations if Ollama is unavailable.
"""
import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:e4b"
TIMEOUT = 60


def _ollama(prompt: str) -> str | None:
    try:
        req = urllib.request.Request(
            OLLAMA_URL,
            data=json.dumps({
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {"num_predict": 220, "temperature": 0.4},
            }).encode(),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return json.loads(r.read().decode()).get("response", "").strip()
    except Exception:
        return None


def explain(question: dict, lang: str = "en") -> dict:
    """
    question: dict with q_en, q_te, opt_a..d, correct, explanation_en, explanation_te, subject, topic
    lang: 'en' | 'te' | 'both'
    Returns {"text": ..., "source": "ai"|"stored"}
    """
    if lang == "te":
        stored = question.get("explanation_te")
        prompt = (
            f"మీరు ఒక స్నేహపూర్వక ECET ట్యూటర్. ఈ క్రింది ప్రశ్నకు సమాధానం ఎందుకు సరైనదో సరళమైన తెలుగులో "
            f"3-4 వాక్యాల్లో వివరించండి.\n\n"
            f"ప్రశ్న: {question.get('q_te') or question['q_en']}\n"
            f"సరైన సమాధానం: {question['correct'].upper()}) {question.get('opt_' + question['correct'], '')}\n\n"
            f"సూత్రం/భావన: {stored or question.get('explanation_en','')}\n\n"
            "సరళ తెలుగులో మాత్రమే సమాధానం ఇవ్వండి."
        )
    else:
        stored = question.get("explanation_en")
        prompt = (
            "You are a friendly ECET tutor for diploma students. Explain in 3-4 simple sentences "
            "why the given answer is correct.\n\n"
            f"Question: {question['q_en']}\n"
            f"Correct answer: {question['correct'].upper()}) {question.get('opt_' + question['correct'], '')}\n"
            f"Concept: {stored or ''}\n\n"
            "Use simple English a diploma student understands. No headings."
        )

    ai = _ollama(prompt)
    if ai:
        return {"text": ai, "source": "ai"}

    # graceful fallback
    if lang == "te":
        text = question.get("explanation_te") or question.get("explanation_en") or ""
    else:
        text = question.get("explanation_en") or ""
    return {"text": text, "source": "stored"}

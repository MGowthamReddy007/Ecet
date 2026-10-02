"""
bank_chemistry.py — ECET Chemistry model + previous-year questions (English only).
Syllabus: Fundamentals, Solutions, Acids & Bases, Water Technology, Electrochemistry,
Metallurgy, Corrosion, Polymers, Environmental Studies.
"""
SUBJECT = "Chemistry"
TRACK = "chemistry"

BANK = [
 # ---------------- Fundamentals (11) ----------------
 ("Fundamentals", "The atomic number of carbon is:", ["6", "12", "14", "8"], 0, 1, "2018,2022", "Carbon has 6 protons in its nucleus."),
 ("Fundamentals", "The maximum number of electrons in the M shell (n = 3) is:", ["18", "8", "2", "32"], 0, 1, "2019,2023", "Using 2n^2, for n = 3 it is 18."),
 ("Fundamentals", "Avogadro's number is approximately:", ["6.022 x 10^23", "6.022 x 10^22", "3.14 x 10^23", "9.8 x 10^23"], 0, 1, "2018,2021", "One mole contains 6.022 x 10^23 particles."),
 ("Fundamentals", "The atomic number of an element equals the number of:", ["Protons", "Neutrons", "Electrons plus neutrons", "Nucleons"], 0, 1, "2019", "It is the number of protons in the nucleus."),
 ("Fundamentals", "Isotopes of an element have the same number of:", ["Protons", "Neutrons", "Nucleons", "Mass number"], 0, 2, "2020,2024", "They differ in neutrons but have the same atomic number."),
 ("Fundamentals", "The modern periodic law states that properties are a periodic function of:", ["Atomic number", "Atomic mass", "Density", "Valency"], 0, 2, "2019,2023", "Moseley's law uses atomic number as the basis."),
 ("Fundamentals", "Group 1 elements are known as:", ["Alkali metals", "Halogens", "Noble gases", "Transition metals"], 0, 1, "2018,2022", "Group 1 metals are the alkali metals."),
 ("Fundamentals", "The electronic configuration of helium is:", ["1s^2", "1s^1", "2s^2", "1s^2 2s^1"], 0, 1, "2020", "Helium has two electrons in the 1s orbital."),
 ("Fundamentals", "The number of neutrons in carbon-12 is:", ["6", "12", "18", "0"], 0, 2, "2019", "12 nucleons minus 6 protons gives 6 neutrons."),
 ("Fundamentals", "The valency of sodium is:", ["1", "2", "3", "0"], 0, 1, "2018,2023", "Sodium loses one electron to become Na+."),
 ("Fundamentals", "The molecular mass of water (H2O) is:", ["18", "16", "20", "10"], 0, 1, "2021", "Two hydrogens (2) plus one oxygen (16) equals 18."),

 # ---------------- Solutions (11) ----------------
 ("Solutions", "Molarity is defined as moles of solute per:", ["Litre of solution", "Kilogram of solvent", "Gram of solute", "Mole of solvent"], 0, 1, "2018,2022", "M = moles of solute / volume of solution in litres."),
 ("Solutions", "Molality is defined as moles of solute per:", ["Kilogram of solvent", "Litre of solution", "Gram of solute", "Mole of solution"], 0, 2, "2019,2023", "Molality uses the mass of solvent in kilograms."),
 ("Solutions", "Normality is expressed as:", ["Gram equivalents of solute per litre of solution", "Moles per kilogram", "Grams per mole", "Moles per mole"], 0, 2, "2020", "Normality uses gram equivalents per litre."),
 ("Solutions", "The mole fraction of a component is:", ["Moles of that component divided by total moles", "Moles times volume", "Grams per litre", "Moles per kilogram"], 0, 2, "2019,2024", "Mole fraction is a dimensionless ratio."),
 ("Solutions", "Raoult's law relates the vapour pressure of a solution to the:", ["Mole fraction of solvent", "Mass of solute", "Volume of solution", "Colour of solute"], 0, 3, "2020", "Partial vapour pressure equals mole fraction times pure vapour pressure."),
 ("Solutions", "Colligative properties depend on the:", ["Number of solute particles", "Nature of solute", "Colour of solute", "Size of solute"], 0, 2, "2018,2023", "They depend on the number of particles, not their identity."),
 ("Solutions", "One mole of a substance contains:", ["6.022 x 10^23 particles", "10^23 particles", "12.0 x 10^24 particles", "3.14 x 10^23 particles"], 0, 1, "2019,2022", "This is Avogadro's number."),
 ("Solutions", "Mass percent of a solution is:", ["Mass of solute per 100 g of solution", "Moles per litre", "Mass per unit volume", "Moles per kilogram"], 0, 1, "2018", "It expresses solute mass as a percentage of total mass."),
 ("Solutions", "On dilution with water, the molarity of a solution:", ["Decreases", "Increases", "Stays the same", "Becomes zero"], 0, 1, "2020,2024", "Adding solvent increases volume and reduces molarity."),
 ("Solutions", "Henry's law relates the solubility of a gas to its:", ["Partial pressure", "Temperature only", "Volume of solvent", "Molar mass"], 0, 3, "2021", "Solubility is proportional to partial pressure above the liquid."),
 ("Solutions", "Which of these is a colligative property?", ["Elevation of boiling point", "Colour", "Density", "Refractive index"], 0, 2, "2020,2023", "Boiling point elevation depends on particle number."),

 # ---------------- Acids & Bases (11) ----------------
 ("Acids & Bases", "The pH of a neutral solution at 25 C is:", ["7", "0", "14", "1"], 0, 1, "2018,2021", "Pure water is neutral with pH 7."),
 ("Acids & Bases", "Acid + Base gives:", ["Salt + Water", "Salt + Oxygen", "Salt + Hydrogen", "Salt + CO2"], 0, 1, "2019,2022", "This is the neutralisation reaction."),
 ("Acids & Bases", "A solution with pH less than 7 is:", ["Acidic", "Basic", "Neutral", "Amphoteric"], 0, 1, "2018", "Lower pH means higher acidity."),
 ("Acids & Bases", "Which of the following is a strong acid?", ["HCl", "CH3COOH", "H2CO3", "HCOOH"], 0, 1, "2019,2023", "Hydrochloric acid ionises completely in water."),
 ("Acids & Bases", "According to Bronsted-Lowry theory, an acid is a:", ["Proton donor", "Proton acceptor", "Electron donor", "Electron acceptor"], 0, 2, "2020", "Bronsted acids donate protons."),
 ("Acids & Bases", "According to Lewis theory, an acid is an:", ["Electron pair acceptor", "Electron pair donor", "Proton donor", "Hydroxide donor"], 0, 2, "2021,2024", "Lewis acids accept electron pairs."),
 ("Acids & Bases", "The pH of 0.1 M HCl is approximately:", ["1", "7", "13", "0.1"], 0, 2, "2019,2023", "pH = -log(0.1) = 1."),
 ("Acids & Bases", "Phenolphthalein is used as an:", ["Indicator", "Catalyst", "Solvent", "Oxidising agent"], 0, 1, "2018,2022", "It changes colour with pH and acts as an indicator."),
 ("Acids & Bases", "A buffer solution:", ["Resists change in pH", "Changes pH rapidly", "Is always acidic", "Is always basic"], 0, 2, "2020", "Buffers oppose pH changes on adding acid or base."),
 ("Acids & Bases", "The ionic product of water Kw at 25 C is:", ["1 x 10^-14", "1 x 10^-7", "1 x 10^14", "1 x 10^-1"], 0, 3, "2021", "Kw equals the product of hydrogen and hydroxide concentrations."),
 ("Acids & Bases", "The pH scale normally ranges from:", ["0 to 14", "0 to 7", "1 to 10", "0 to 100"], 0, 1, "2018,2022", "Standard pH values span 0 to 14."),

 # ---------------- Water Technology (11) ----------------
 ("Water Technology", "Hard water contains dissolved salts of:", ["Calcium and magnesium", "Sodium and potassium", "Iron and copper", "Zinc and lead"], 0, 1, "2018,2023", "Calcium and magnesium salts cause hardness."),
 ("Water Technology", "Temporary hardness of water is due to:", ["Bicarbonates of calcium and magnesium", "Sulphates of calcium", "Chlorides of sodium", "Nitrates of potassium"], 0, 2, "2019,2022", "Bicarbonates decompose on boiling, causing temporary hardness."),
 ("Water Technology", "Permanent hardness of water is caused by:", ["Sulphates and chlorides of calcium and magnesium", "Bicarbonates only", "Sodium chloride", "Dissolved oxygen"], 0, 2, "2020", "These salts are not removed by boiling."),
 ("Water Technology", "The ion exchange process softens water by:", ["Replacing calcium and magnesium ions with sodium ions", "Adding more salts", "Boiling", "Filtering mud"], 0, 2, "2019,2023", "Zeolite and resin exchange sodium for hardness ions."),
 ("Water Technology", "The zeolite process is used for:", ["Water softening", "Water chlorination", "Water distillation", "Water filtration"], 0, 1, "2018,2022", "Zeolites exchange ions to remove hardness."),
 ("Water Technology", "Water hardness is usually expressed in:", ["Parts per million of calcium carbonate", "Litres", "Moles", "Degrees Celsius"], 0, 2, "2020", "Hardness is reported as ppm of CaCO3 equivalent."),
 ("Water Technology", "Boiling removes:", ["Temporary hardness", "Permanent hardness", "All hardness", "No hardness"], 0, 1, "2019", "Boiling precipitates bicarbonate hardness."),
 ("Water Technology", "Calgon conditioning is used to:", ["Prevent scale formation in boilers", "Increase hardness", "Disinfect water", "Add minerals"], 0, 3, "2021", "Calgon keeps hardness salts in solution."),
 ("Water Technology", "Potable water means water that is:", ["Safe for drinking", "Hard water", "Sea water", "Distilled water only"], 0, 1, "2018,2022", "Potable water is fit for human consumption."),
 ("Water Technology", "Distilled water is:", ["Soft", "Hard", "Temporary hard", "Permanent hard"], 0, 1, "2020,2024", "Distillation removes dissolved salts, giving soft water."),
 ("Water Technology", "The lime-soda process is used to remove:", ["Hardness of water", "Colour of water", "Turbidity only", "Dissolved gases"], 0, 2, "2019,2023", "Lime and soda precipitate hardness causing salts."),

 # ---------------- Electrochemistry (11) ----------------
 ("Electrochemistry", "In electrolysis, oxidation occurs at the:", ["Anode", "Cathode", "Both electrodes", "Neither electrode"], 0, 2, "2018,2023", "Anode is where oxidation takes place."),
 ("Electrochemistry", "In electrolysis, reduction occurs at the:", ["Cathode", "Anode", "Salt bridge", "Solution"], 0, 2, "2019,2022", "Cathode is where reduction takes place."),
 ("Electrochemistry", "Faraday's laws deal with:", ["Electrolysis and the amount of substance deposited", "Gas pressure", "Vapour density", "Atomic mass"], 0, 2, "2020", "They relate the quantity of charge to mass deposited."),
 ("Electrochemistry", "An electrolyte is a substance that:", ["Conducts electricity in solution", "Does not conduct electricity", "Is always a metal", "Is always a gas"], 0, 1, "2018,2021", "Ions carry current through the solution."),
 ("Electrochemistry", "A galvanic cell converts:", ["Chemical energy to electrical energy", "Electrical energy to chemical energy", "Heat to light", "Light to heat"], 0, 2, "2019,2023", "Spontaneous reactions drive a current."),
 ("Electrochemistry", "The SI unit of electromotive force is:", ["Volt", "Ampere", "Ohm", "Coulomb"], 0, 1, "2020", "Emf is measured in volts."),
 ("Electrochemistry", "The Nernst equation relates cell potential to:", ["Concentration of ions", "Temperature only", "Volume", "Mass"], 0, 3, "2021", "It accounts for ion concentration and temperature."),
 ("Electrochemistry", "One Faraday is approximately:", ["96500 coulombs", "9650 coulombs", "965 coulombs", "96.5 coulombs"], 0, 2, "2019,2024", "One Faraday equals the charge on one mole of electrons."),
 ("Electrochemistry", "Electroplating is based on:", ["Electrolysis", "Distillation", "Sublimation", "Filtration"], 0, 1, "2018,2022", "A metal is deposited by passing current through a solution."),
 ("Electrochemistry", "The Daniell cell is an example of a:", ["Galvanic cell", "Fuel cell", "Electrolytic cell", "Storage battery"], 0, 2, "2020", "It is a classic galvanic (voltaic) cell."),
 ("Electrochemistry", "The SI unit of conductance is:", ["Siemens", "Ohm", "Volt", "Ampere"], 0, 2, "2021,2023", "Conductance is measured in siemens."),

 # ---------------- Metallurgy (11) ----------------
 ("Metallurgy", "The extraction of metal from its ore is called:", ["Metallurgy", "Polymerisation", "Neutralisation", "Electroplating"], 0, 1, "2018,2022", "The whole process of obtaining metals is metallurgy."),
 ("Metallurgy", "The process of removing impurities from an ore is called:", ["Concentration", "Roasting", "Smelting", "Alloying"], 0, 2, "2019,2023", "Ore dressing or concentration removes gangue."),
 ("Metallurgy", "Roasting involves heating the ore:", ["In the presence of air", "In the absence of air", "With water", "With acid"], 0, 2, "2020", "Roasting uses air to convert sulphide ores to oxides."),
 ("Metallurgy", "Calcination involves heating the ore:", ["In the absence of air", "In the presence of air", "With a reducing agent", "With flux"], 0, 2, "2019,2022", "Calcination drives off volatile matter without air."),
 ("Metallurgy", "Smelting is the reduction of an ore:", ["By heating with a reducing agent", "By cooling", "By dissolving in water", "By electrolysis only"], 0, 3, "2020", "Carbon or another reductant frees the metal."),
 ("Metallurgy", "A flux is added to:", ["Remove gangue as slag", "Increase the metal content", "Add colour", "Cool the furnace"], 0, 2, "2018,2023", "Flux combines with impurities to form fusible slag."),
 ("Metallurgy", "The fusible waste formed in smelting is called:", ["Slag", "Flux", "Ore", "Matte"], 0, 1, "2019,2022", "Slag is the molten waste removed from the metal."),
 ("Metallurgy", "Bauxite is the chief ore of:", ["Aluminium", "Iron", "Copper", "Zinc"], 0, 1, "2020,2024", "Aluminium is extracted from bauxite."),
 ("Metallurgy", "Froth flotation is used to concentrate:", ["Sulphide ores", "Oxide ores", "Carbonate ores", "Native metals"], 0, 3, "2021", "It separates sulphide minerals using air bubbles and oil."),
 ("Metallurgy", "Galena is the ore of:", ["Lead", "Iron", "Copper", "Silver"], 0, 2, "2019,2023", "Galena is lead sulphide, PbS."),
 ("Metallurgy", "Haematite is an ore of:", ["Iron", "Aluminium", "Copper", "Tin"], 0, 1, "2018,2022", "Haematite is Fe2O3, a key iron ore."),

 # ---------------- Corrosion (11) ----------------
 ("Corrosion", "Rusting of iron is essentially the:", ["Oxidation of iron", "Reduction of iron", "Melting of iron", "Sublimation of iron"], 0, 1, "2018,2022", "Iron loses electrons and forms hydrated oxide."),
 ("Corrosion", "Rust is chemically:", ["Hydrated iron(III) oxide", "Iron sulphide", "Iron chloride", "Pure iron"], 0, 2, "2019,2023", "Rust is Fe2O3.xH2O."),
 ("Corrosion", "Rusting of iron requires:", ["Oxygen and moisture", "Only oxygen", "Only moisture", "Only heat"], 0, 1, "2020", "Both air and water are needed for rusting."),
 ("Corrosion", "Galvanisation protects iron by coating it with:", ["Zinc", "Copper", "Tin", "Silver"], 0, 1, "2018,2022", "A zinc layer prevents rust formation."),
 ("Corrosion", "Cathodic protection makes the protected metal:", ["The cathode", "The anode", "Neutral", "An electrolyte"], 0, 3, "2021", "The metal to protect is forced to be cathodic."),
 ("Corrosion", "In sacrificial anode protection, the metal used as anode is:", ["More reactive than the protected metal", "Less reactive", "The same metal", "A noble metal"], 0, 3, "2020,2024", "A more reactive metal corrodes instead."),
 ("Corrosion", "Electroplating helps prevent corrosion by:", ["Coating with a less reactive metal", "Removing the metal", "Adding water", "Heating"], 0, 2, "2019,2023", "A protective coating shields the base metal."),
 ("Corrosion", "Corrosion is basically a:", ["Electrochemical process", "Physical change only", "Nuclear process", "Mechanical process"], 0, 2, "2020", "It involves anodic and cathodic regions."),
 ("Corrosion", "Painting prevents corrosion by:", ["Blocking contact with air and moisture", "Adding oxygen", "Increasing temperature", "Adding salt"], 0, 1, "2018,2022", "The paint film isolates the metal from the environment."),
 ("Corrosion", "Brass is an alloy of:", ["Copper and zinc", "Copper and tin", "Iron and carbon", "Aluminium and copper"], 0, 2, "2019,2023", "Brass contains copper and zinc."),
 ("Corrosion", "Stainless steel resists corrosion because it contains:", ["Chromium", "Lead", "Sodium", "Sulphur"], 0, 2, "2021", "Chromium forms a protective oxide layer."),

 # ---------------- Polymers (11) ----------------
 ("Polymers", "The monomer of polyethylene is:", ["Ethylene", "Propylene", "Styrene", "Vinyl chloride"], 0, 1, "2018,2023", "Many ethylene units join to form polyethylene."),
 ("Polymers", "The monomer of PVC is:", ["Vinyl chloride", "Ethylene", "Styrene", "Isoprene"], 0, 1, "2019,2022", "Polyvinyl chloride comes from vinyl chloride."),
 ("Polymers", "Nylon is a:", ["Polyamide", "Polyester", "Polyolefin", "Polycarbonate"], 0, 2, "2020", "Amide linkages join the monomer units."),
 ("Polymers", "The monomer of Teflon is:", ["Tetrafluoroethylene", "Ethylene", "Styrene", "Vinyl chloride"], 0, 2, "2021,2024", "Teflon is polytetrafluoroethylene."),
 ("Polymers", "Bakelite is an example of a:", ["Thermosetting polymer", "Thermoplastic", "Elastomer", "Fibre"], 0, 2, "2019,2023", "It sets permanently and cannot be remelted."),
 ("Polymers", "Addition polymerisation involves:", ["Unsaturated monomers joining without loss of small molecules", "Loss of water", "Loss of ammonia", "Only condensation"], 0, 3, "2020", "Double bonds open and monomers link directly."),
 ("Polymers", "Condensation polymerisation involves:", ["Loss of a small molecule such as water", "No loss of any molecule", "Only addition", "Only free radicals"], 0, 3, "2021", "Each linkage step eliminates a small molecule."),
 ("Polymers", "Natural rubber is a polymer of:", ["Isoprene", "Styrene", "Ethylene", "Vinyl chloride"], 0, 2, "2018,2022", "Natural rubber is cis-polyisoprene."),
 ("Polymers", "The monomer of polystyrene is:", ["Styrene", "Ethylene", "Isoprene", "Butadiene"], 0, 1, "2019,2023", "Styrene polymerises to polystyrene."),
 ("Polymers", "Buna-S is a:", ["Synthetic rubber", "Polyester fibre", "Thermoset plastic", "Natural fibre"], 0, 2, "2020", "It is a copolymer of butadiene and styrene."),
 ("Polymers", "Dacron is a:", ["Polyester", "Polyamide", "Polyolefin", "Polyurethane"], 0, 2, "2021,2024", "Dacron is a polyester fibre."),

 # ---------------- Environmental Studies (12) ----------------
 ("Environmental Studies", "The major cause of global warming is:", ["Carbon dioxide", "Oxygen", "Nitrogen", "Helium"], 0, 1, "2018,2021", "CO2 is a major greenhouse gas."),
 ("Environmental Studies", "The depletion of the ozone layer is mainly caused by:", ["Chlorofluorocarbons", "Carbon dioxide", "Oxygen", "Methane"], 0, 2, "2019,2023", "CFCs release chlorine that destroys ozone."),
 ("Environmental Studies", "Acid rain is mainly caused by:", ["Sulphur dioxide and nitrogen oxides", "Carbon dioxide", "Oxygen", "Helium"], 0, 2, "2020", "These gases form acids in the atmosphere."),
 ("Environmental Studies", "BOD stands for:", ["Biochemical Oxygen Demand", "Basic Oxygen Demand", "Biological Organic Decomposition", "Benzene Oxygen Demand"], 0, 2, "2019,2022", "It measures organic pollution in water."),
 ("Environmental Studies", "Green chemistry aims to:", ["Reduce or eliminate hazardous substances", "Increase pollution", "Use more energy", "Increase waste"], 0, 1, "2021", "It designs processes that are environmentally friendly."),
 ("Environmental Studies", "Which of the following is a greenhouse gas?", ["Methane", "Oxygen", "Nitrogen", "Argon"], 0, 1, "2018,2022", "Methane is a potent greenhouse gas."),
 ("Environmental Studies", "Photochemical smog is formed by the action of sunlight on:", ["Nitrogen oxides and hydrocarbons", "Carbon dioxide", "Oxygen", "Water vapour"], 0, 3, "2020", "Sunlight drives reactions forming ozone and other pollutants."),
 ("Environmental Studies", "Particulate matter (PM) pollution refers to:", ["Fine solid and liquid particles in air", "Dissolved salts in water", "Soil minerals", "Gases only"], 0, 2, "2019,2023", "PM includes suspended fine particles."),
 ("Environmental Studies", "Sewage treatment primarily removes:", ["Organic and microbial pollutants", "Oxygen", "Nitrogen gas", "Helium"], 0, 1, "2020", "It cleans wastewater before discharge."),
 ("Environmental Studies", "The chemical formula of ozone is:", ["O3", "O2", "CO2", "SO2"], 0, 1, "2018,2022", "Ozone is a triatomic form of oxygen."),
 ("Environmental Studies", "Carbon monoxide is dangerous because it:", ["Binds to haemoglobin", "Dissolves in water", "Is a greenhouse gas only", "Is odourless but harmless"], 0, 2, "2021", "It reduces the oxygen carrying capacity of blood."),
 ("Environmental Studies", "The best way to reduce plastic pollution is:", ["Reduce, reuse and recycle", "Burn all plastic", "Dump in rivers", "Increase production"], 0, 1, "2023", "The three R approach cuts plastic waste."),
]

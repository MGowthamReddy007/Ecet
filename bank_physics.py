"""
bank_physics.py — ECET Physics model + previous-year questions (English only).
Syllabus: Units & Dimensions, Friction, Vectors, Mechanics, Properties of Matter,
Heat & Thermodynamics, Waves & Sound, Simple Harmonic Motion, Modern Physics, Magnetism & Electricity.
"""
SUBJECT = "Physics"
TRACK = "physics"

BANK = [
 # ---------------- Units & Dimensions (11) ----------------
 ("Units & Dimensions", "The SI unit of force is:", ["Newton", "Joule", "Watt", "Pascal"], 0, 1, "2018,2023", "Force is measured in newtons (kg m/s^2)."),
 ("Units & Dimensions", "The dimensional formula of force is:", ["MLT^-2", "ML^2T^-2", "MLT^-1", "ML^-1T^-2"], 0, 2, "2019,2024", "F = ma, so M L T^-2."),
 ("Units & Dimensions", "The SI unit of work is:", ["Joule", "Newton", "Watt", "Pascal"], 0, 1, "2018,2022", "Work and energy are measured in joules."),
 ("Units & Dimensions", "The dimensional formula of energy is:", ["ML^2T^-2", "MLT^-2", "ML^2T^-1", "M^-1L^2T^-2"], 0, 2, "2020", "Energy = force x distance = M L^2 T^-2."),
 ("Units & Dimensions", "How many base units are there in the SI system?", ["7", "5", "9", "3"], 0, 1, "2019", "Metre, kilogram, second, ampere, kelvin, mole and candela."),
 ("Units & Dimensions", "The dimensional formula of velocity is:", ["LT^-1", "L^-1T", "LT^-2", "L^2T^-1"], 0, 1, "2018,2021", "Velocity = displacement / time = L T^-1."),
 ("Units & Dimensions", "The SI unit of pressure is:", ["Pascal", "Newton", "Joule", "Bar"], 0, 1, "2022", "Pressure is force per area, measured in pascals."),
 ("Units & Dimensions", "The dimensional formula of acceleration is:", ["LT^-2", "LT^-1", "LT", "L^-1T^2"], 0, 1, "2019,2023", "Acceleration = velocity / time = L T^-2."),
 ("Units & Dimensions", "1 newton is equal to:", ["10^5 dyne", "10^3 dyne", "10^7 dyne", "10 dyne"], 0, 2, "2020", "The CGS unit of force, the dyne, is 10^-5 N."),
 ("Units & Dimensions", "The SI unit of power is:", ["Watt", "Joule", "Newton", "Pascal"], 0, 1, "2018,2024", "Power is work per time, measured in watts."),
 ("Units & Dimensions", "Which of the following is a dimensionless quantity?", ["Strain", "Force", "Pressure", "Energy"], 0, 2, "2021", "Strain is a ratio of lengths and has no dimensions."),

 # ---------------- Friction (11) ----------------
 ("Friction", "The force of friction between two surfaces depends on:", ["Normal reaction", "Area of contact", "Volume", "Colour"], 0, 1, "2018,2022", "f = mu N, so it depends on the normal reaction."),
 ("Friction", "The relation between limiting friction f and normal reaction N is:", ["f = mu N", "f = N / mu", "f = mu / N", "f = mu + N"], 0, 1, "2019,2023", "mu is the coefficient of friction."),
 ("Friction", "Generally, the coefficient of static friction is:", ["Greater than kinetic friction", "Less than kinetic friction", "Equal to kinetic friction", "Zero"], 0, 2, "2020", "It takes more force to start motion than to keep it going."),
 ("Friction", "The coefficient of friction is:", ["Dimensionless", "Measured in newton", "Measured in metre", "Measured in kg"], 0, 1, "2018", "It is a ratio of two forces, so it has no units."),
 ("Friction", "The maximum value of friction just before motion begins is called:", ["Limiting friction", "Kinetic friction", "Rolling friction", "Dynamic friction"], 0, 1, "2019,2022", "At the verge of sliding friction reaches its limiting value."),
 ("Friction", "If the angle of repose is theta and mu is the coefficient of friction, then:", ["tan theta = mu", "sin theta = mu", "cos theta = mu", "mu = 1/tan theta"], 0, 2, "2021", "The angle of repose satisfies tan theta = mu."),
 ("Friction", "The direction of friction is:", ["Opposite to relative motion", "Along the motion", "Perpendicular to the surface", "Vertically upward always"], 0, 1, "2018,2023", "Friction always opposes relative sliding."),
 ("Friction", "Among the following, the least friction is:", ["Rolling friction", "Sliding friction", "Static friction", "Limiting friction"], 0, 1, "2019", "Rolling contact gives the least resistance."),
 ("Friction", "Friction between two surfaces is independent of:", ["Area of contact", "Nature of surfaces", "Normal reaction", "Weight of body"], 0, 2, "2020,2024", "Friction depends on the normal reaction, not the contact area."),
 ("Friction", "Lubricants are used to:", ["Reduce friction", "Increase friction", "Increase weight", "Increase area"], 0, 1, "2018", "A lubricant forms a layer that lowers friction."),
 ("Friction", "The normal reaction on a body resting on a horizontal surface is:", ["Perpendicular to the surface", "Along the surface", "At 45 degrees", "Zero"], 0, 1, "2021", "Normal reaction always acts perpendicular to the surface."),

 # ---------------- Vectors (11) ----------------
 ("Vectors", "The magnitude of the vector 3i + 4j is:", ["5", "7", "1", "25"], 0, 1, "2018,2023", "sqrt(9 + 16) = 5."),
 ("Vectors", "The dot product of two perpendicular vectors is:", ["0", "1", "Maximum", "Negative"], 0, 1, "2019,2022", "cos 90 = 0, so the dot product is zero."),
 ("Vectors", "The cross product of two parallel vectors is:", ["0", "Maximum", "1", "Equal to their product"], 0, 2, "2020", "sin 0 = 0 for parallel vectors."),
 ("Vectors", "The magnitude of a unit vector is:", ["1", "0", "infinite", "depends on direction"], 0, 1, "2018,2021", "A unit vector has unit magnitude by definition."),
 ("Vectors", "i . i equals:", ["1", "0", "-1", "i"], 0, 1, "2019", "The dot product of a unit vector with itself is 1."),
 ("Vectors", "i x j equals:", ["k", "-k", "0", "i"], 0, 2, "2020,2024", "The cross product follows the right hand rule."),
 ("Vectors", "The scalar (dot) product of two vectors is:", ["Commutative", "Not commutative", "Always zero", "A vector"], 0, 2, "2021", "A . B = B . A, so it is commutative."),
 ("Vectors", "The vector (cross) product satisfies A x B =", ["-(B x A)", "B x A", "A . B", "0 always"], 0, 2, "2019,2023", "The cross product is anti-commutative."),
 ("Vectors", "The magnitude of A x B is:", ["AB sin(theta)", "AB cos(theta)", "A + B", "A / B"], 0, 1, "2018,2022", "It equals the product of magnitudes times sine of the angle."),
 ("Vectors", "The magnitude of the vector 6i + 8j is:", ["10", "14", "48", "2"], 0, 1, "2020", "sqrt(36 + 64) = 10."),
 ("Vectors", "The value of (i + j) . (i - j) is:", ["0", "2", "1", "-2"], 0, 2, "2021,2024", "(i.i - i.j + j.i - j.j) = 1 - 0 + 0 - 1 = 0."),

 # ---------------- Mechanics (11) ----------------
 ("Mechanics", "A body moving with uniform velocity has acceleration:", ["Zero", "Constant non-zero", "Increasing", "Negative"], 0, 1, "2018,2021", "If velocity is not changing, acceleration is zero."),
 ("Mechanics", "Newton's second law gives:", ["F = ma", "E = mc^2", "V = IR", "P = W/t"], 0, 1, "2019,2023", "Force equals mass times acceleration."),
 ("Mechanics", "Newton's third law states:", ["Every action has an equal and opposite reaction", "F = ma", "A body at rest stays at rest", "Energy is conserved"], 0, 1, "2018,2022", "Action and reaction are equal and opposite."),
 ("Mechanics", "Which of the following is a kinematic equation?", ["v^2 = u^2 + 2as", "F = ma", "P = mv", "W = Fs"], 0, 2, "2020", "It relates velocity, acceleration and displacement."),
 ("Mechanics", "Linear momentum is defined as:", ["p = mv", "p = ma", "p = mgh", "p = mv^2"], 0, 1, "2019,2024", "Momentum is mass times velocity."),
 ("Mechanics", "The SI unit of momentum is:", ["kg m/s", "kg m/s^2", "N", "J"], 0, 1, "2018", "Momentum has units of kg m/s."),
 ("Mechanics", "Newton's first law is also known as the law of:", ["Inertia", "Force", "Motion", "Gravitation"], 0, 1, "2020,2022", "A body continues in its state unless acted on by a force."),
 ("Mechanics", "The work done by a force F making angle theta with displacement s is:", ["Fs cos(theta)", "Fs sin(theta)", "F + s", "Fs"], 0, 1, "2019,2023", "Only the component along displacement does work."),
 ("Mechanics", "The kinetic energy of a body of mass m moving with velocity v is:", ["(1/2) mv^2", "mv^2", "mgh", "mv"], 0, 1, "2018,2022", "Standard kinetic energy formula."),
 ("Mechanics", "The potential energy of a body at height h is:", ["mgh", "(1/2) mv^2", "mv", "ma"], 0, 1, "2021", "Gravitational potential energy equals mgh."),
 ("Mechanics", "When no external force acts on a system, the quantity conserved is:", ["Linear momentum", "Velocity", "Acceleration", "Energy only"], 0, 2, "2020,2024", "Momentum is conserved in the absence of external forces."),

 # ---------------- Properties of Matter (11) ----------------
 ("Properties of Matter", "Hooke's law states that within elastic limit:", ["Stress is proportional to strain", "Stress is inversely proportional to strain", "Strain is zero", "Stress equals strain"], 0, 1, "2018,2023", "Stress and strain are proportional within the elastic limit."),
 ("Properties of Matter", "Young's modulus is defined as:", ["Stress / strain", "Strain / stress", "Force / area", "Force x extension"], 0, 1, "2019,2022", "It is the ratio of longitudinal stress to longitudinal strain."),
 ("Properties of Matter", "The SI unit of stress is:", ["N/m^2", "N", "J", "m/s"], 0, 1, "2020", "Stress is force per area, the pascal."),
 ("Properties of Matter", "The SI unit of surface tension is:", ["N/m", "N/m^2", "J/m^2", "kg/m"], 0, 2, "2021,2024", "Surface tension is force per unit length."),
 ("Properties of Matter", "The SI unit of viscosity is:", ["Pa s", "Pa", "N/m", "kg/m^2"], 0, 2, "2019,2023", "The SI unit of dynamic viscosity is the pascal second."),
 ("Properties of Matter", "Steel is more elastic than rubber because:", ["It has a larger Young's modulus", "It is harder", "It is denser", "It is stronger"], 0, 2, "2020", "A larger Young's modulus means greater elasticity for the same strain."),
 ("Properties of Matter", "Small liquid drops are spherical due to:", ["Surface tension", "Viscosity", "Elasticity", "Gravity"], 0, 1, "2018,2022", "Surface tension minimises surface area, giving a sphere."),
 ("Properties of Matter", "The pressure at depth h in a liquid of density rho is:", ["rho g h", "rho h", "g h", "rho g / h"], 0, 1, "2019", "Hydrostatic pressure equals depth times density times g."),
 ("Properties of Matter", "The SI unit of Young's modulus is:", ["N/m^2", "N", "N/m", "J"], 0, 1, "2021", "Modulus has the same unit as stress."),
 ("Properties of Matter", "Poisson's ratio is the ratio of:", ["Lateral strain to longitudinal strain", "Stress to strain", "Force to area", "Volume to area"], 0, 3, "2020,2024", "It measures lateral contraction per unit longitudinal extension."),
 ("Properties of Matter", "Liquid rises in a narrow capillary tube because of:", ["Surface tension and adhesion", "Viscosity", "High pressure", "Low density only"], 0, 2, "2018,2023", "Capillary rise results from surface tension and adhesion."),

 # ---------------- Heat & Thermodynamics (11) ----------------
 ("Heat & Thermodynamics", "The first law of thermodynamics is the conservation of:", ["Energy", "Mass", "Momentum", "Charge"], 0, 1, "2018,2023", "dQ = dU + dW expresses energy conservation."),
 ("Heat & Thermodynamics", "Heat flows naturally from:", ["Hot to cold", "Cold to hot", "Either direction", "Nowhere"], 0, 1, "2019,2022", "The second law fixes the direction of heat flow."),
 ("Heat & Thermodynamics", "The first law of thermodynamics is written as:", ["dQ = dU + dW", "dQ = dU - dW", "dQ = dW", "dU = dQ + dW"], 0, 2, "2020", "Heat supplied equals change in internal energy plus work done."),
 ("Heat & Thermodynamics", "The second law of thermodynamics introduces the concept of:", ["Entropy", "Force", "Momentum", "Density"], 0, 2, "2021,2024", "Entropy always tends to increase in spontaneous processes."),
 ("Heat & Thermodynamics", "The SI unit of heat is:", ["Joule", "Calorie only", "Newton", "Watt"], 0, 1, "2018", "The SI unit of heat energy is the joule."),
 ("Heat & Thermodynamics", "The specific heat of water is about:", ["4186 J/kg K", "1000 J/kg K", "2100 J/kg K", "4.2 J/kg K"], 0, 2, "2020", "Water has a famously high specific heat capacity."),
 ("Heat & Thermodynamics", "The zeroth law of thermodynamics defines:", ["Thermal equilibrium", "Entropy", "Work", "Heat capacity"], 0, 3, "2021", "It establishes the basis for temperature measurement."),
 ("Heat & Thermodynamics", "For an ideal gas, the equation of state is:", ["PV = nRT", "P = VI", "F = ma", "E = mc^2"], 0, 1, "2019,2023", "The ideal gas equation relates pressure, volume and temperature."),
 ("Heat & Thermodynamics", "In an adiabatic process:", ["No heat is exchanged", "Temperature is constant", "Pressure is constant", "Volume is constant"], 0, 2, "2018,2022", "Adiabatic means no heat flows in or out."),
 ("Heat & Thermodynamics", "In an isothermal process the quantity kept constant is:", ["Temperature", "Heat", "Pressure", "Volume"], 0, 1, "2020", "Iso means same and thermal refers to temperature."),
 ("Heat & Thermodynamics", "The efficiency of a Carnot engine is:", ["1 - T2/T1", "T2/T1", "1 + T2/T1", "T1/T2"], 0, 3, "2021,2024", "It depends only on the source and sink temperatures."),

 # ---------------- Waves & Sound (11) ----------------
 ("Waves & Sound", "Sound cannot travel through:", ["Vacuum", "Air", "Water", "Steel"], 0, 1, "2018,2023", "Sound needs a material medium to propagate."),
 ("Waves & Sound", "The speed of sound is maximum in:", ["Solids", "Liquids", "Gases", "Vacuum"], 0, 2, "2019,2022", "Elasticity is highest in solids, so sound travels fastest there."),
 ("Waves & Sound", "The SI unit of frequency is:", ["Hertz", "Metre", "Second", "Decibel"], 0, 1, "2018", "Frequency is measured in hertz."),
 ("Waves & Sound", "The relation between wave speed v, frequency f and wavelength lambda is:", ["v = f lambda", "v = f / lambda", "v = lambda / f", "v = f + lambda"], 0, 1, "2019,2023", "Wave speed equals frequency times wavelength."),
 ("Waves & Sound", "Ultrasonic waves have frequency:", ["Greater than 20 kHz", "Less than 20 Hz", "Between 20 and 20000 Hz", "Equal to zero"], 0, 2, "2020", "Above the audible range of about 20 kHz."),
 ("Waves & Sound", "Loudness of sound is measured in:", ["Decibel", "Hertz", "Metre", "Newton"], 0, 1, "2018,2022", "Sound level is expressed in decibels."),
 ("Waves & Sound", "The apparent change in frequency due to relative motion is called:", ["Doppler effect", "Echo", "Resonance", "Refraction"], 0, 2, "2019,2024", "This is the Doppler effect."),
 ("Waves & Sound", "An echo is due to:", ["Reflection of sound", "Refraction of sound", "Diffraction of sound", "Absorption of sound"], 0, 1, "2020", "Sound reflects off a distant surface to form an echo."),
 ("Waves & Sound", "The time period is related to frequency by:", ["T = 1/f", "T = f", "T = 2f", "T = f^2"], 0, 1, "2018,2023", "Time period is the reciprocal of frequency."),
 ("Waves & Sound", "Sound waves in air are:", ["Longitudinal", "Transverse", "Electromagnetic", "Stationary"], 0, 1, "2019,2022", "Particles vibrate along the direction of propagation."),
 ("Waves & Sound", "Resonance occurs when the applied frequency equals the:", ["Natural frequency of the body", "Speed of sound", "Wavelength", "Amplitude"], 0, 2, "2021", "Maximum energy transfer occurs at the natural frequency."),

 # ---------------- Simple Harmonic Motion (11) ----------------
 ("Simple Harmonic Motion", "In SHM the acceleration is:", ["Proportional to displacement and directed towards the mean position", "Constant", "Zero", "Proportional to velocity"], 0, 1, "2018,2023", "a = -omega^2 x is the defining relation of SHM."),
 ("Simple Harmonic Motion", "The time period of a simple pendulum is:", ["2 pi sqrt(l/g)", "2 pi sqrt(g/l)", "2 pi l/g", "sqrt(l/g)"], 0, 2, "2019,2022", "It depends on length and gravity."),
 ("Simple Harmonic Motion", "In SHM, the acceleration at displacement x is:", ["-omega^2 x", "omega^2 x", "omega x", "-omega x"], 0, 2, "2020", "Acceleration is proportional to negative displacement."),
 ("Simple Harmonic Motion", "In SHM, the velocity is maximum at:", ["Mean position", "Extreme position", "Quarter amplitude", "Nowhere"], 0, 2, "2019,2023", "Speed is greatest as the body crosses the centre."),
 ("Simple Harmonic Motion", "In SHM, the acceleration is maximum at:", ["Extreme position", "Mean position", "Quarter amplitude", "The centre"], 0, 2, "2020", "Restoring force, hence acceleration, is largest at the extremes."),
 ("Simple Harmonic Motion", "In SHM the total energy is:", ["Constant", "Zero", "Maximum at extremes only", "Maximum at the mean position"], 0, 2, "2018,2022", "Energy alternates between kinetic and potential but the total stays constant."),
 ("Simple Harmonic Motion", "The time period of a mass spring system is:", ["2 pi sqrt(m/k)", "2 pi sqrt(k/m)", "2 pi m/k", "sqrt(m/k)"], 0, 3, "2021,2024", "It depends on mass and spring constant."),
 ("Simple Harmonic Motion", "The angular frequency omega is related to time period T by:", ["omega = 2 pi / T", "omega = T / 2 pi", "omega = 2 pi T", "omega = 1/T"], 0, 2, "2019", "Angular frequency is 2 pi divided by the period."),
 ("Simple Harmonic Motion", "At the mean position of a SHM, the energy is:", ["All kinetic", "All potential", "Zero", "Infinite"], 0, 2, "2020,2023", "Potential energy is minimum and kinetic energy is maximum."),
 ("Simple Harmonic Motion", "The time period of a pendulum depends on:", ["Length and g", "Mass of the bob", "Amplitude", "Colour of the bob"], 0, 1, "2018,2022", "It is independent of the mass of the bob."),
 ("Simple Harmonic Motion", "SHM is a special case of:", ["Periodic motion", "Random motion", "Linear motion", "Circular motion only"], 0, 1, "2021", "It is a periodic motion with a sinusoidal displacement."),

 # ---------------- Modern Physics (11) ----------------
 ("Modern Physics", "The photoelectric effect was explained by:", ["Einstein", "Newton", "Bohr", "Rutherford"], 0, 1, "2018,2022", "Einstein used the photon concept in 1905."),
 ("Modern Physics", "The energy of a photon is given by:", ["E = h nu", "E = mgh", "E = (1/2) mv^2", "E = qV only"], 0, 1, "2019,2023", "Photon energy equals Planck's constant times frequency."),
 ("Modern Physics", "The de Broglie wavelength is given by:", ["lambda = h/p", "lambda = p/h", "lambda = hp", "lambda = h/m"], 0, 2, "2020", "Matter waves have wavelength equal to h over momentum."),
 ("Modern Physics", "The SI unit of Planck's constant is:", ["J s", "J/s", "N s", "J m"], 0, 2, "2021,2024", "Planck's constant carries units of joule second."),
 ("Modern Physics", "The nucleus of an atom was discovered by:", ["Rutherford", "Bohr", "Thomson", "Chadwick"], 0, 1, "2018", "Rutherford's gold foil experiment revealed the nucleus."),
 ("Modern Physics", "The Bohr model explains the stability of:", ["Atomic orbits", "The nucleus", "Molecules", "Crystals"], 0, 2, "2019,2022", "It introduced quantised stationary orbits."),
 ("Modern Physics", "Mass and energy are related by:", ["E = mc^2", "E = h nu", "F = ma", "P = VI"], 0, 1, "2020,2023", "Einstein's famous mass energy equivalence."),
 ("Modern Physics", "Isotopes of an element have the same:", ["Atomic number", "Mass number", "Number of neutrons", "Atomic mass"], 0, 1, "2018,2022", "They differ only in the number of neutrons."),
 ("Modern Physics", "Cathode rays are actually:", ["Electrons", "Protons", "Neutrons", "Photons"], 0, 1, "2019", "Cathode rays are streams of electrons."),
 ("Modern Physics", "The work function is the minimum energy needed to:", ["Eject an electron from a metal surface", "Split the nucleus", "Ionise a gas", "Break a molecule"], 0, 2, "2021", "It is the threshold energy for photoemission."),
 ("Modern Physics", "The photoelectric effect is possible only if the incident light frequency is:", ["Above the threshold frequency", "Below the threshold frequency", "Equal to zero", "Independent of frequency"], 0, 2, "2020,2024", "Below the threshold, no electrons are emitted regardless of intensity."),

 # ---------------- Magnetism & Electricity (11) ----------------
 ("Magnetism & Electricity", "Ohm's law states that V =", ["IR", "I/R", "R/I", "I^2 R"], 0, 1, "2018,2023", "Voltage equals current times resistance."),
 ("Magnetism & Electricity", "Three 3 ohm resistors connected in parallel give a resistance of:", ["1 ohm", "3 ohm", "9 ohm", "6 ohm"], 0, 2, "2019,2024", "For n equal resistors, R = r/n = 1 ohm."),
 ("Magnetism & Electricity", "The magnetic field inside a long solenoid is:", ["Uniform", "Zero", "Maximum at the ends", "Circular"], 0, 1, "2018,2021", "It is nearly uniform along the axis."),
 ("Magnetism & Electricity", "The SI unit of resistance is:", ["Ohm", "Volt", "Ampere", "Watt"], 0, 1, "2019", "Resistance is measured in ohms."),
 ("Magnetism & Electricity", "Electrical power is given by:", ["P = VI", "P = V/I", "P = I/V", "P = V + I"], 0, 1, "2018,2022", "Power equals voltage times current."),
 ("Magnetism & Electricity", "Fleming's left hand rule gives the direction of:", ["Force on a current carrying conductor", "Induced current", "Magnetic flux", "Resistance"], 0, 2, "2020,2023", "It is used for motors."),
 ("Magnetism & Electricity", "Coulomb's law gives the force between two:", ["Charges", "Masses", "Magnets only", "Currents"], 0, 1, "2019,2022", "It is the inverse square law for electric charges."),
 ("Magnetism & Electricity", "Resistors in series have a total resistance equal to:", ["The sum of individual resistances", "The product of resistances", "The reciprocal sum", "The average"], 0, 1, "2018", "Series resistances simply add up."),
 ("Magnetism & Electricity", "The SI unit of magnetic field is:", ["Tesla", "Weber", "Henry", "Ohm"], 0, 2, "2021", "Magnetic flux density is measured in tesla."),
 ("Magnetism & Electricity", "Kirchhoff's junction rule is based on conservation of:", ["Charge", "Energy", "Momentum", "Mass"], 0, 2, "2020,2024", "The sum of currents entering a junction equals the sum leaving."),
 ("Magnetism & Electricity", "For two resistors connected in parallel, the equivalent resistance is:", ["Less than the smallest resistor", "Greater than the largest", "The sum of both", "Their product"], 0, 2, "2019,2023", "Parallel resistance is always smaller than each branch."),
]

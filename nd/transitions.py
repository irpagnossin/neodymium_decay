transitions = {
    "A": [
        # (End state, probability of transition, transition process name)
        ("B", 0.2, "Photon emission"),
        ("C", 0.4, "Beta decay"),
        ("D", 0.3, "Photon emission"),
        ("E", 0.1, "Photon emission"),
    ],
    "B": [
        ("C", 0.6, "Photon emission"),
        ("D", 0.4, "Photon emission"),
    ],
    "C": [
        ("D", 0.3, "Photon emission"),
        ("E", 0.7, "Photon emission"),
    ],
    "D": [
        ("E", 1.0, "Photon emission"),
    ],
}

energies = {  # MeV
    "A": 0.70,
    "B": 0.50,
    "C": 0.30,
    "D": 0.05,
    "E": 0.00,
}

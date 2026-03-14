from dynamic import simulate, spectrum
from transitions import transitions


def merge_spectra(s1, s2):
    for energy, count in s2.items():
        if energy in s1:
            s1[energy] += count
        else:
            s1[energy] = count
    return s1


def simulate_mc():
    n_simulations: int = 100

    total_spectrum: dict = {}
    for _ in range(n_simulations):
        trajectory = simulate('A', transitions)
        spectrum_ = spectrum(trajectory)
        merge_spectra(total_spectrum, spectrum_)

    print(total_spectrum)


if __name__ == "__main__":
    simulate_mc()

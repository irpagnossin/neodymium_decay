from dynamic import simulate
from transitions import transitions


def merge_transitions(tA, tB: list[tuple[float, str]]):
    for energy, process in tB:
        if process in tA:
            tA[process].append(energy)
        else:
            tA[process] = [energy]
    return tA


def build_and_plot_spectrum(
    energies: dict[str, list[float]],
    process: str,
) -> None:
    import matplotlib.pyplot as plt
    import numpy as np

    energies_ = [-1 * energy for energy in energies[process]]
    frequencies, bin_edges = np.histogram(energies_, bins=50, range=(0, 1.1), density=True)

    plt.bar(bin_edges[:-1], frequencies, width=np.diff(bin_edges), align='edge', edgecolor='black')
    plt.title(f'Espectro de energia: {process}')
    plt.xlabel('Energia (MeV)')
    plt.ylabel('Intensidade')
    plt.show()


def simulate_mc():
    n_simulations: int = 10
    ans = {}

    for _ in range(n_simulations):
        trajectory, transitions_ = simulate('A', transitions)
        ans = merge_transitions(ans, transitions_)

    return ans


if __name__ == "__main__":
    energies = simulate_mc()
    build_and_plot_spectrum(energies, 'Photon emission')
    build_and_plot_spectrum(energies, 'Beta decay')

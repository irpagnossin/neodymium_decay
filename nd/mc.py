from dynamic import simulate, transition_energies
from transitions import transitions


def simulate_mc():
    n_simulations: int = 100_000
    ans: list[float] = []

    for _ in range(n_simulations):
        trajectory = simulate('A', transitions)
        ans.extend(transition_energies(trajectory))

    return ans


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    energies = simulate_mc()
    energies = [-1 * energy for energy in energies]
    frequencies, bin_edges = np.histogram(energies, bins=50, range=(0, 1.1), density=True)

    plt.bar(bin_edges[:-1], frequencies, width=np.diff(bin_edges), align='edge', edgecolor='black')
    plt.title('Espectro de energia')
    plt.xlabel('Energia (MeV)')
    plt.ylabel('Intensidade')
    plt.show()

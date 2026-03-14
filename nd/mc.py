from dynamic import simulate, transition_energies
import numpy as np
from transitions import transitions


def merge_spectra(s1, s2):
    for energy, count in s2.items():
        if energy in s1:
            s1[energy] += count
        else:
            s1[energy] = count
    return s1


def simulate_mc():
    n_simulations: int = 100_000
    ans: list[float] = []

    for _ in range(n_simulations):
        trajectory = simulate('A', transitions)
        ans.extend(transition_energies(trajectory))

    return ans


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    energies = simulate_mc()
    hist, bin_edges = np.histogram(energies, bins=50, range=(-1.1, 0), density=True)
    print("Histogram counts:", hist)
    print("Bin edges:", bin_edges)

    plt.bar(bin_edges[:-1], hist, width=np.diff(bin_edges), align='edge', edgecolor='black')
    plt.title('Histogram using np.histogram and plt.bar')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

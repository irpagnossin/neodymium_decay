from collections import Counter

from .dynamic import simulate


def merge_transitions(tA, tB: list[tuple[float, str]]):
    for energy, process in tB:
        if process in tA:
            tA[process].append(energy)
        else:
            tA[process] = [energy]
    return tA


def run(transitions_profile, energies, start_state, n_simulations: int = 1_000):
    last_states = Counter()
    executed_transitions = {}

    for _ in range(n_simulations):
        trajectory, transitions = simulate(transitions_profile, energies, start_state)
        executed_transitions = merge_transitions(executed_transitions, transitions)
        last_state = trajectory[-1]
        last_states[last_state] += 1

    return last_states, executed_transitions


def build_and_plot_spectrum(
    energies: dict[str, list[float]],
    process: str,
) -> None:
    import matplotlib.pyplot as plt
    import numpy as np

    energies_ = [-1 * energy for energy in energies[process]]
    frequencies, bin_edges = np.histogram(energies_, bins=50, density=True)

    plt.bar(bin_edges[:-1], frequencies, width=np.diff(bin_edges), align='edge', edgecolor='black')
    plt.title(f'Espectro de energia: {process}')
    plt.xlabel('Energia (MeV)')
    plt.ylabel('Intensidade')
    plt.show()


def plot_abundances(data):
    import matplotlib.pyplot as plt

    total = sum(data.values())
    frequencies = {state: count/total for state, count in data.items()}

    states = list(frequencies.keys())
    abundance = list(frequencies.values())

    plt.bar(states, abundance)
    plt.xlabel("State")
    plt.ylabel("Abundance ∈[0,1]")
    plt.title("Last state abundance")
    plt.ylim(0, 1)
    plt.show()

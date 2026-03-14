from collections import Counter


from transitions import transitions, energies
from dynamic import step


def monte_carlo_stationary(start_state, transitions, n_steps):
    state = start_state
    counts = Counter()
    t_counts = Counter()

    try:
        for _ in range(n_steps):
            counts[state] += 1
            next_state = step(state, transitions)
            transition_energy = energies[next_state] - energies[state]
            t_counts[transition_energy] += 1
            state = next_state
    except StopIteration as e:
        print(e)

    total = sum(counts.values())
    t_total = sum(t_counts.values())
    return {s: counts[s]/total for s in counts}, {e: t_counts[e]/t_total for e in t_counts}


if __name__ == "__main__":
    states_dist, transitions_dist = monte_carlo_stationary("A", transitions, 100_000)
    print(states_dist)
    print(transitions_dist)

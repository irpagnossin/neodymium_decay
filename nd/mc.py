from collections import Counter


from transitions import transitions
from dynamic import step


def monte_carlo_stationary(start_state, transitions, n_steps):
    state = start_state
    counts = Counter()

    for _ in range(n_steps):
        counts[state] += 1
        state = step(state, transitions)

    total = sum(counts.values())
    return {s: counts[s]/total for s in counts}


if __name__ == "__main__":
    dist = monte_carlo_stationary("A", transitions, 100_000)
    print(dist)

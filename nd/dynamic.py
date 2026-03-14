import random
import numpy as np


def step(state, transitions):
    """Return the next state"""
    if state not in transitions:
        raise StopIteration(f"Evolution stopped: state {state} has empty fringe.")

    fringe, probs = zip(*transitions[state])
    return random.choices(fringe, weights=probs)[0]


def simulate(start_state, transitions, n_steps: int = 1_000):
    state = start_state
    trajectory = [state]

    try:
        for _ in range(n_steps):
            state = step(state, transitions)
            trajectory.append(state)
    except StopIteration:
        pass

    return trajectory


def spectrum(trajectory: list):
    from transitions import energies
    from collections import Counter

    t = np.array(trajectory, dtype=str)
    t_rolled = np.roll(t, shift=-1)
    transitions = list(zip(t, t_rolled))
    spectrum = Counter()
    for s_from, s_to in transitions[:-1]:
        transition_energy = energies[s_to] - energies[s_from]
        spectrum[transition_energy] += 1
    return spectrum


if __name__ == "__main__":
    from transitions import transitions
    trajectory = simulate("A", transitions, 20)
    print(trajectory)
    print(spectrum(trajectory))

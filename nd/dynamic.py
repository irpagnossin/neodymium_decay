import random


def step(state, transitions):
    """Return the next state"""
    if state not in transitions:
        raise StopIteration(f"Evolution stopped: state {state} has empty fringe.")

    fringe, probs, process = zip(*transitions[state])
    return random.choices(list(zip(fringe, process)), weights=probs)[0]


def simulate(start_state, transitions, n_steps: int = 1_000):
    from transitions import energies

    state = start_state
    trajectory = [state]
    transitions_ = []

    try:
        for _ in range(n_steps):
            next_state, process = step(state, transitions)
            transition_energy = energies[next_state] - energies[state]
            state = next_state
            trajectory.append(state)
            transitions_.append((transition_energy, process))
    except StopIteration:
        pass

    return trajectory, transitions_


if __name__ == "__main__":
    from transitions import transitions
    trajectory, transitions = simulate("A", transitions, 20)
    print("Trajetória:", trajectory)
    print("Transições:", transitions)

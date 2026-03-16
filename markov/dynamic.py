import random

SELF_TRANSITION: str = "Self-transition"


def step(state, transitions):
    """Return the next state"""

    if state not in transitions:
        raise StopIteration(f"Evolution stopped: state {state} has empty fringe.")

    fringe, probs, process = zip(*transitions[state])

    assert state not in fringe  # TODO: validate case instead

    fringe = list(fringe)
    fringe.append(state)

    probs = list(probs)
    probs.append(1 - sum(probs))

    process = list(process)
    process.append(SELF_TRANSITION)

    return random.choices(list(zip(fringe, process)), weights=probs)[0]


def simulate(transitions_profile, energies, start_state, n_steps: int = 1_000):
    state = start_state
    trajectory = [state]
    transitions_ = []

    try:
        for i in range(n_steps):
            next_state, process = step(state, transitions_profile)
            transition_energy = energies[next_state] - energies[state]
            state = next_state
            trajectory.append(state)
            transitions_.append((transition_energy, process))
    except StopIteration:
        # print(f"StopIteration at {i}")
        pass

    return trajectory, transitions_

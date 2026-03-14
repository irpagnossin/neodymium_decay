import random


def step(state, transitions):
    """Return the next state"""
    fringe, probs = zip(*transitions[state])
    return random.choices(fringe, weights=probs)[0]


def simulate(start_state, transitions, n_steps):
    state = start_state
    trajectory = [state]

    for _ in range(n_steps):
        state = step(state, transitions)
        trajectory.append(state)

    return trajectory


if __name__ == "__main__":
    from transitions import transitions
    trajectory = simulate("A", transitions, 20)
    print(trajectory)

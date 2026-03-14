from dynamic import simulate
from transitions import transitions


if __name__ == "__main__":
    trajectories = [simulate('A', transitions) for _ in range(100)]
    print(trajectories)

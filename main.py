from markov import run, build_and_plot_spectrum, plot_abundances
# from cases.dummy_01 import energies, transitions
from cases.Np import energies, transitions


if __name__ == "__main__":
    last_states, energies = run(transitions, energies, 'Np')
    for process in energies.keys():
        build_and_plot_spectrum(energies, process)
    plot_abundances(last_states)

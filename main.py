from nd import run, build_and_plot_spectrum, plot_abundances
from cases.eg_1 import energies, transitions


if __name__ == "__main__":
    last_states, energies = run(transitions, energies, 'A')
    build_and_plot_spectrum(energies, 'Photon emission')
    build_and_plot_spectrum(energies, 'Beta decay')
    plot_abundances(last_states)

# -*- coding: utf-8 -*-

from simulation import Simulation
import matplotlib.pyplot as plt
import sys

def main(population_size = 20, individual_size = 8, delta = 0.005):
    print("pop size = {}, ind size = {}, delta = {}".format(population_size, individual_size, delta))

    simulation = Simulation(population_size, individual_size, delta)
    simulation.run_simulation()
    print(simulation.population)
    plt.plot(simulation.global_fitness_records)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2:
        main(int(sys.argv[1]))
    elif len(sys.argv) == 3:
        main(int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) == 4:
        main(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))

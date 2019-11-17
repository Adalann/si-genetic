# -*- coding: utf-8 -*-

import getopt
import sys

import matplotlib.pyplot as plt

from simulation import Simulation


def main(argv):
    population_size = 20
    individual_size = 8
    delta = 0.005
    cross_point_count = 1
    verbose = False

    try:
        opts, args = getopt.getopt(argv, 'hvp:i:c:d:', [
            'help',
            'verbose',
            'population-size=', 
            'individual-size=', 
            'cross-points=', 
            'delta='
        ])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        if opt in ('-v', '--verbose'):
            verbose = True
        if opt in ('-p', '--population-size'):
            population_size = int(arg)
        if opt in ('-i', '--individual-size'):
            individual_size = int(arg)
        if opt in ('-c', '--cross-points'):
            cross_point_count = int(arg)
        if opt in ('-d', '--delta'):
            delta = float(arg)

    print("pop size = {}, ind size = {}, cross points = {}, delta = {}".format(
        population_size, individual_size, cross_point_count, delta))
    simulation = Simulation(
        population_size, individual_size, cross_point_count, delta)
    simulation.run_simulation()
    if verbose:
        print(simulation.population)


    # Ploting
    x_values = range(0, len(simulation.global_fitness_records))
    y_values = [
        simulation.global_fitness_records,
        simulation.convergence_values
    ]
    labels = ["Average fitness score", "Convergence values"]

    for y_array, label in zip(y_values, labels):
        plt.plot(x_values, y_array, label=label)

    plt.legend()
    plt.show()


def usage():
    print("""
    Usage : python genetic.py [OPTIONS]

    You can specify the following options :
        -v, --verbose:
            If specified the last population will be printed out in the terminal.
        -p, --population-size [integer]:
            The size of the population that will be use in the genetic algorithm.
        -u, --individual-size [integer]
            The number of gene of each individual member of the population.
        -d, --delta [float]
            A value for the convergence detection. The less this value will be, the longer the algorithm will take to stop but the greater the average fitness value will be.
            This value must be less than 1.
    """)


if __name__ == "__main__":
    main(sys.argv[1:])

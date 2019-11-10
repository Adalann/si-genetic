# -*- coding: utf-8 -*-

from simulation import Simulation
import matplotlib.pyplot as plt
import sys, getopt

def main(argv):
    population_size = 20
    individual_size = 8
    delta = 0.005

    try:
        opts, args = getopt.getopt(argv, 'hp:i:d:', ['help', 'population-size=', 'individual-size=', 'delta='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        if opt in ('-p', '--population-size'):
            population_size = int(arg)
        if opt in ('-i', '--individual-size'):
            individual_size = int(arg)
        if opt in ('-d', '--delta'):
            delta = float(arg)
    
    print("pop size = {}, ind size = {}, delta = {}".format(population_size, individual_size, delta))
    simulation = Simulation(population_size, individual_size, delta)
    simulation.run_simulation()
    print(simulation.population)
    plt.plot(simulation.global_fitness_records)
    plt.show()

def usage():
    print("""
    Usage : python genetic.py [OPTIONS]

    You can specify the folloing options : 
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

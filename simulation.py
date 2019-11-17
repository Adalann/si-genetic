# -*- coding: utf-8 -*-

import datetime
from random import random

from individual import Individual
from population import Population


class Simulation:
    """ Gère l'algorithme genetique """

    SELECTION_ROULETTE = 0
    SELECTION_TOURNAMENT = 1

    def __init__(self, population_size, individual_size, cross_point_count, delta, mutation_probability=0.1, selection_mode=SELECTION_ROULETTE):
        self.population_size = population_size
        self.population = Population(population_size, individual_size)
        self.cross_point_count = cross_point_count
        self.delta = delta
        self.selection_mode = selection_mode

        self.generation = 0
        self.population_historic = []
        self.global_fitness_records = []
        self.convergence_value = 0
        self.convergence_values = []
        self.mutation_probability = mutation_probability

    def run_simulation(self):
        """ Algorithme génétique """

        genesis_time = datetime.datetime.now()
        self.population.genesis()
        self.population.eval_population()
        global_fitness = self.population.get_global_fitness(
                normalized=True)
        self.global_fitness_records.append(global_fitness)
        #print("Genesis, global fitness : {}".format(global_fitness))
        self.generation += 1

        while not self.has_converged():
            selection = self.selection(self.selection_mode)
            children = self.crossing(selection)
            self.mutation(children)
            self.replace_population(children)
            self.population.eval_population()
            global_fitness = self.population.get_global_fitness(
                normalized=True)
            self.global_fitness_records.append(global_fitness)
            gene_time = datetime.datetime.now()
            #print("Gen {}, global fitness : {}, time : {}".format(
                #self.generation, global_fitness, str(gene_time - genesis_time)))
            self.generation += 1

    def has_converged(self):
        """ Calcul la convergence de l'algorithme """

        has_converged = True if self.population.get_global_fitness(normalized=True) == 1.0 else False

        if len(self.global_fitness_records) != 0 and not has_converged:
            new_convergence_value = sum(self.global_fitness_records) / len(self.global_fitness_records)

            if abs(new_convergence_value - self.convergence_value) < self.delta:
                has_converged = True
            self.convergence_value = new_convergence_value
        
        self.convergence_values.append(self.convergence_value)

        return has_converged

    def selection(self, selection_mode=0):
        """
            Réalise l'opération de sélection
            Si selection_mode = SELECTION_ROULETTE alors le mode de sélection sera la roulette, sinon un tournois sera utilisé
        """

        selection = []
        if selection_mode == Simulation.SELECTION_ROULETTE:
            selection = self.population.selection_roulette()
        elif selection_mode == Simulation.SELECTION_TOURNAMENT:
            selection = self.population.selection_tournament()

        return selection

    def crossing(self, selection):
        """ Réalise l'opération de croisement """

        children = []
        for i in range(len(selection) - 1):
            children.extend(Individual.reproduce(
                selection[i],
                selection[i + 1],
                cross_point_count=self.cross_point_count
            ))

            i += 1

        return children

    def mutation(self, individuals):
        """ Réalise les mutations """

        for individual in individuals:
            if random() < self.mutation_probability:
                individual.mutate()

    def replace_population(self, children, store=False):
        """
            Réalise l'opération de remplacement
            Si store = True, la population précédente sera sauvegardé dans la liste population_historic
        """

        if store:
            self.population_historic.append(self.population)

        self.population = self.population.generate_population_tournament(children)

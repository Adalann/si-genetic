# -*- coding: utf-8 -*-

from random import shuffle

from individual import Individual


class Population:
    """ Représente une multitute d'individu """

    def __init__(self, size, size_individuals):
        self.size = size
        self.size_individuals = size_individuals
        self.individuals = []
    

    def genesis(self):
        """ Créé la première génération """

        for _ in range(self.size):
            self.individuals.append(Individual(self.size_individuals))


    def get_global_fitness(self, normalized = False):
        """
            Retourne la valeur de fitness global de la population 
            Si normalized est True, le score sera comprit entre 0 et 1
        """

        self.eval_population()
        global_fitness = 0
        for individual in self.individuals:
            global_fitness += individual.fit_score

        global_fitness /= len(self.individuals)

        if normalized:
            global_fitness /= Individual.get_maximal_fit_score()

        return global_fitness


    def eval_population(self):
        """ Rafraichit les valeurs de Fitness de la population """

        for individual in self.individuals:
            individual.evaluate()

    
    def shuffle(self):
        """ Mélange la population """
        shuffle(self.individuals)


    def __str__(self):
        res = ""
        for ind in self.individuals:
            res += "{} ".format(ind.fit_score)

        return res

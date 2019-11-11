# -*- coding: utf-8 -*-

from random import shuffle, randint

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

    def get_global_fitness(self, normalized=False):
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

    def selection_roulette(self):
        """ Réalise l'opération de séléction par roulette """

        selection = []
        sum_fit = 0

        for individu in self.individuals:
            sum_fit += individu.get_fitness()

        while len(selection) < self.size:
            draw = randint(0, sum_fit)
            cursor = self.individuals[0].get_fitness()
            i = 0
            while cursor <= draw:
                i += 1
                cursor += self.individuals[i].get_fitness()
            selection.append(self.individuals[i])

        return selection

    def selection_tournament(self):
        """ Réalise l'opération de séléction par tournois """

        selection = []
        for _ in range(2):
            self.shuffle()
            for i in range(self.size - 1):
                selection.append(Individual.oppose(
                    self.individuals[i],
                    self.individuals[i + 1]
                ))

                i += 1

        return selection

    def generate_population_elitism(self, children):
        """ Réalise l'opération de remplacement - Elitisme """

        new_population = Population(self.size, self.size_individuals)
        new_population.individuals = [None] * self.size

        self.individuals.sort(key=lambda i: i.fit_score)
        children.sort(key=lambda i: i.fit_score, reverse=True)

        limit_new_population = (int)(self.size * 0.8)
        new_population.individuals[:limit_new_population] = children[:limit_new_population]

        need = self.size - limit_new_population
        new_population.individuals[limit_new_population:
                                   ] = self.individuals[need:2 * need]

        return new_population

    def generate_population_tournament(self, children):
        """ Réalise l'opération de remplacement - Tournois """

        new_population = Population(self.size, self.size_individuals)
        candidates = self.individuals + children
        shuffle(candidates)

        for i in range(len(candidates) - 1):
            new_population.individuals.append(Individual.oppose(
                candidates[i],
                candidates[i + 1]
            ))
            i += 1

        return new_population

    def __str__(self):
        res = "Population [global_fit_score = {}, individuals = [".format(
            self.get_global_fitness())
        for ind in self.individuals:
            res += "{} ".format(ind.fit_score)
        res = res.strip() + "]]"

        return res

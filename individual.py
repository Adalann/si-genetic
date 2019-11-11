# -*- coding: utf-8 -*-

from random import randint


class Individual:
    """ Représente les individus """

    SIZE = 0

    def __init__(self, size):
        Individual.SIZE = size
        self.size = Individual.SIZE
        self.genes = []
        self.fit_score = 0
        for _ in range(0, size):
            self.genes.append(randint(0, 1))
        
        self.evaluate()


    def evaluate(self):
        """ Calcule la valeur de Fitness """

        self.fit_score = 0
        for i in range(0, self.size):
            self.fit_score += (2 ** (self.size - 1 - i)) * self.genes[i]


    def mutate(self):
        """ Réalise la mutation """

        pos = randint(0, self.size - 1)
        self.genes[pos] = 0 if self.genes[pos] == 1 else 1


    def get_fitness(self, normalized = False):
        """
        Retoune le score de fitness de l'individu.
        Si normalized est à True, ce résultat est comprit en 0 et 1
        """

        if normalized:
            return self.fit_score / Individual.get_maximal_fit_score()
        else:
            return self.fit_score


    @staticmethod
    def oppose(individual_A, individual_B):
        """ Réalise le combat entre 2 individus donnés """
        individual_A.evaluate()
        individual_B.evaluate()

        if individual_A.fit_score > individual_B.fit_score:
            return individual_A
        else:
            return individual_B


    @staticmethod
    def reproduce(parent_A, parent_B, cross_point_count = 1):
        """ Réalise la reproduction entre deux parents """

        child_A = Individual(Individual.SIZE)
        child_B = Individual(Individual.SIZE)

        temporary_A = parent_A
        temporary_B = parent_B

        cross_points = []
        while len(cross_points) < cross_point_count:
            new_break_point = randint(0, Individual.SIZE - 2)
            if new_break_point not in cross_points:
                cross_points.append(new_break_point)
        cross_points.sort()

        for i in range(Individual.SIZE):
            if i in cross_points:
                temporary_A, temporary_B = temporary_B, temporary_A
            child_A.genes[i] = temporary_A.genes[i]
            child_B.genes[i] = temporary_B.genes[i]

        return (child_A, child_B)


    @staticmethod
    def get_maximal_fit_score():
        maximal_fit_score = 0
        for i in range(Individual.SIZE):
            maximal_fit_score += 2 ** i

        return maximal_fit_score

        
    def __str__(self):
        return "Individual [fitscore = {}, genes = {}]".format(self.fit_score, self.genes)

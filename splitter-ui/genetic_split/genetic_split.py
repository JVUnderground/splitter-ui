import random
from individual import Individual
from functions import slice_sequence, score_population, select_mates


class GeneticSplitter():
    '''
    GeneticSplitter:
    '''
    POPULATION_SIZE = 100
    NUMBER_GENERATIONS = 1000
    EVOLUTION_STOP = 200

    def __init__(self, sequence):
        self.sequence = sequence
        self.individual_length = len(sequence) - 1
        with open("dictionary.txt") as d:
            dictionary = d.readlines()

        self.dictionary = [x.strip() for x in dictionary]
        self.population = []
        self.create_population()

    def create_population(self):
        '''
        Generates a random population of individuals
        '''
        for _ in xrange(self.POPULATION_SIZE):
            genes = bin(random.getrandbits(self.individual_length))[2:self.individual_length+2]
            individual = Individual('0'*(self.individual_length - len(genes)) + genes)
            self.population.append(individual)

    def evolve_population(self):


        '''
        Evolves population towards solution until one of two stopping conditions are met.
        '''
        stuck = 0
        elitist = self.population[0]
        for _ in xrange(self.NUMBER_GENERATIONS):
            self.population = slice_sequence(self.population, self.sequence)
            self.population = score_population(self.population, self.dictionary)

            # Exit conditions.
            # First by perfect match.
            if self.population[-1].errors == 0:
                break

            # Then by stuck evolution.
            if self.population[-1].errors == elitist.errors/2:
                stuck += 1
                if stuck > self.EVOLUTION_STOP:
                    break
            else:
                stuck = 0

            elitist = self.population[-1].copy() # Best individual.

            # Selection
            mating_pairs = select_mates(self.population)

            # Crossover
            self.population = []
            for mates in mating_pairs:
                first = mates[0]
                second = mates[1]

                children = first.crossover(second)
                self.population.append(children[0])
                self.population.append(children[1])

            # Mutation
            for k, individual in enumerate(self.population):
                self.population[k].gene = individual.mutate()

            # Elitism
            self.population.sort(key=lambda x: x.errors, reverse=True)
            self.population[0] = elitist

        self.solution = self.population[-1]


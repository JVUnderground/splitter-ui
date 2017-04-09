from random import random, randint

class Individual():
    mutation_rate = 0.08
    crossover_rate = 0.65

    def __init__(self, genes):
        self.genes = genes
        self.errors = 0
        self.solution = []
        self.fitness = 0
        self.score = 0

    def __str__(self):
        return " ".join(self.solution) or self.genes

    def __repr__(self):
        return " ".join(self.solution) or self.genes

    def mutate(self):
        mutated = ""
        for gene in self.genes:
            if random() <= self.mutation_rate:
                mutated += str(1 - int(gene))
            else:
                mutated += gene

        return Individual(mutated)

    def crossover(self, other):
        if random() <= self.crossover_rate:
            crossover_point = randint(1,len(other.genes)-1)
            first = Individual(self.genes[:crossover_point] + other.genes[crossover_point:])
            second = Individual(other.genes[:crossover_point] + self.genes[crossover_point:])
            return [first, second]

        else:
            return [self, other]

    def copy(self):
        copy = Individual(self.genes)
        copy.errors = self.errors
        copy.solution = self.solution
        copy.fitness = self.fitness
        copy.score = self.score
        
        return copy

            
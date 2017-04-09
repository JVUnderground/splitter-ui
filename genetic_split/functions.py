import random

def slice_sequence(population, sequence):
    '''
    Partitions the letter sequence, according to individual genes.
    '''
    for k,individual in enumerate(population):
        words = []
        delta = 0
        for i,gene in enumerate(individual.genes):
            if gene == '1':
                word = sequence[delta:i+1]
                words.append(word)
                delta = i+1
                #print("DELTA: %d, INDEX: %d, WORD: %s" % (delta,i,word))
            
            if i == len(individual.genes) - 1:
                words.append(sequence[delta:])

                population[k].solution = words

    return population

def score_population(population, dictionary):
    '''
    Evaluates the fitness of each individual in population according to how many
    words in it's solution exist in the supplied dictionary.

    score_population will automatically sort the population according to fitness.
    '''
    for k, individual in enumerate(population):
        for j, word in enumerate(individual.solution):
            if word in dictionary:
                continue
            else:
                population[k].solution[j] = word.upper()
                population[k].errors += len(word)


    population.sort(key=lambda x: x.errors, reverse=True)
    for k,individual in enumerate(population):
        if k > 0:
            population[k].fitness = k + population[k-1].fitness
        else:
            population[k].fitness = 1

    return population

def select_mates(population):
    '''
    Selects pairs of individuals according to population fitness probability.
    '''
    mating_pairs = []
    for i in xrange(len(population)/2):
        max_range = sum(range(1,len(population)))
        mating_population = population
        
        selected = []
        for i in range(0,2):
            not_found = True
            for individual in mating_population:
                required_fitness = random.randint(1,max_range)
                if individual.fitness >= required_fitness:
                    selected.append(individual)
                    mating_population.remove(individual)
                    not_found = False
                    break
            if not_found:
                selected.append(selected[0]) # Essentially don't mate.
            

        mating_pairs.append(selected)
        
    return mating_pairs
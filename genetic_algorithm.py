# coding: utf-8
import math
import random
import numpy as np
import pandas as pd
from utils import dict_to_list, get_parameters_name
from constants import *

import argparse
parser = argparse.ArgumentParser()

for param in parameters_pretty_name.keys():
    parser.add_argument('--'+param)
args = parser.parse_args()

x_max = X_MAX
x_min = X_MIN

winner_prob = MAINTAIN_WINNER_PROBABILITY

if args.eid:
    eid = args.eid
else:
    eid = None

if args.num_pop:
    num_pop = int(args.num_pop)
else:
    num_pop = NUM_POP

if args.num_generations:
    num_generations = int(args.num_generations)
else:
    num_generations = NUM_GENERATIONS

if args.num_bits:
    num_bits = int(args.num_bits)
else:
    num_bits = NUM_BITS

if args.num_genes:
    num_genes = int(args.num_genes)
else:
    num_genes = NUM_GENES

total_genes_size = num_bits * num_genes


if args.cross_rate:
    cross_rate = float(args.cross_rate)
else:
    cross_rate = CROSS_RATE

num_cross = int((cross_rate * num_pop)/2)
# num_cross = num_cross if num_pop%2 == 0 else num_cross-1
num_no_cross = num_pop-2*num_cross

if args.elitism_rate:
    elitism_rate = float(args.elitism_rate)
else:
    elitism_rate = ELITISM_RATE
num_elitists = int(elitism_rate * num_pop)

if args.mutation_rate:
    mutation_rate = float(args.mutation_rate)
else:
    mutation_rate = MUTATION_RATE # probability of mutate a single bit

if args.mutateds_rate:
    mutateds_rate = float(args.mutateds_rate)
else:
    mutateds_rate = MUTATEDS_RATE # number of individuals to mutate, not using in this research
num_mutateds = int(mutateds_rate*num_pop)

parameters_values = {
    'num_pop': num_pop, 'num_generations': num_generations, 'num_bits': num_bits,
    'num_genes': num_genes, 'cross_rate': cross_rate,
    'elitism_rate': elitism_rate,
    'mutateds_rate': mutateds_rate,
    'mutation_rate': mutation_rate,
    'eid':eid,
}

parameters = {key: val for key, val in zip(parameters_pretty_name.values(),parameters_values.values())}

# information to catch from algorithm
def func_obj(x):
    n = float(len(x))
    f_exp = -0.2 * math.sqrt(1/n * sum(np.power(x, 2)))

    t = 0
    for i in range(0, len(x)):
            t += np.cos(2 * math.pi * x[i])

    s_exp = 1/n * t
    f = -20 * math.exp(f_exp) - math.exp(s_exp) + 20 + math.exp(1)

    return f

def bin_to_int(binary):
    res = 0
    for i in range(num_bits):
        res += 2**i*int(binary[i])
    return res

def interval_values(binary):
    return x_min+((x_max-x_min)/(2**num_bits-1))*bin_to_int(binary)

def random_binary():
    string = ''
    for i in range(num_bits):
        string += str(random.randint(0,1))
    return string

class Individual:
    def __init__(self,genome=[]):
        self.genome = genome
        self.fo = None
        pass
    def rand_genome(self):
        self.genome = []
        for i in range(num_genes):
            self.genome.append(random_binary())
        return self.genome

    def genome_to_int_list(self):
        return list(map(interval_values,self.genome))
    
    def calc_fo(self):
        # if self.fo is None:
        self.fo = func_obj(self.genome_to_int_list())
        return self.fo

    def string_to_genome_list(self,genome_string):
        genome = []
        for i in range(num_genes):
            genome.append(genome_string[i*num_bits:(i+1)*num_bits])
        return genome

    def crossover(self,ind):
        idx = random.randint(1,total_genes_size-2)
        flat_genome_1 = ''.join(self.genome)
        flat_genome_2 = ''.join(ind.genome)
        new_genome = flat_genome_1[:idx+1]
        new_genome += flat_genome_2[idx+1:]
        new_genome = self.string_to_genome_list(new_genome)
        new_ind1 = Individual(new_genome)

        new_genome = flat_genome_2[idx+1:]
        new_genome += flat_genome_1[:idx+1]
        new_genome = self.string_to_genome_list(new_genome)
        new_ind2 = Individual(new_genome)
        return new_ind1, new_ind2

    def mutate(self,p):
        mutate_any = False
        for i in range(num_genes):
            new_gene = ""
            for j in range(num_bits):
                going_to_mutate = False if random.uniform(0,1)<=p else True
                if going_to_mutate:
                    new_gene += '0' if self.genome[i][j] == '1' else '1'
                    mutate_any = True
                else:
                    new_gene += self.genome[i][j]
            self.genome[i] = new_gene
        if mutate_any:
            self.calc_fo()
        
    def __str__(self):
        return 'genome = '+''.join(self.genome) + f' {self.genome_to_int_list()} , fo = {self.fo}'

def tournament(population):
    fathers = []

    for i in range(2):
        inds = []
        for j in range(2):
            inds.append(random.randint(0,num_pop-1))
        ind = None
        get_winner = np.random.rand() <= winner_prob
        if population[inds[0]].calc_fo() < population[inds[1]].calc_fo():
            ind = population[inds[0]]
            if not get_winner:
                ind = population[inds[1]]
        else:
            ind = population[inds[1]]
            if not get_winner:
                ind = population[inds[0]]
                    
        fathers.append(ind)
    return fathers


#num_pop,num_genes*num_bits

def sort_population(population):
    return sorted(population,key = lambda x: x.fo,reverse=False)

population = []
for i in range(num_pop):
    ind = Individual()
    ind.rand_genome()
    population.append(ind)
    ind.calc_fo()
    # print(ind)

population= sort_population(population)
best_ind = population[0]


df = pd.DataFrame([],columns = columns)
df = df.set_index(columns[0])

df.loc[1] = [', '.join(best_ind.genome), ', '.join(map(lambda x: f'{x:.4}',best_ind.genome_to_int_list())), f'{best_ind.fo:.4}']
for i in range(2,num_generations+1):
    new_population = []
    # Cross
    choices = list(range(len(population)))
    for j in range(num_cross):
        ind1, ind2 = tournament(population)
        nind1, nind2 = ind1.crossover(ind2)
        nind1.calc_fo()
        nind2.calc_fo()
        new_population.append(nind1)
        new_population.append(nind2)
    # Select the rest left of individuals if the cross rate is not 100%
    new_population.extend(population[:num_no_cross])
    new_population = sort_population(new_population)[:num_pop]

    # Mutate these new individuals - Mutation
    idx_pop = list(range(num_pop))
    for _ in range(num_mutateds):
        ind_idx = random.choice(idx_pop)
        idx_pop.remove(ind_idx)
        new_population[ind_idx].mutate(mutation_rate)
    # Select best individuals from previous population - Elitism   
    new_population = sort_population(new_population)

    candidates_to_substitution = list(range(0,num_pop))
    for ind in range(num_elitists):
        # if new_population[num_pop-ind-1].fo > population[ind].fo:
        ind_to_sub = random.choice(candidates_to_substitution)
        new_population[ind_to_sub] = population[ind]
        candidates_to_substitution.remove(ind_to_sub)

    new_population= sort_population(new_population)

    population = new_population
    best_ind = population[0]
    df.loc[i] = [', '.join(best_ind.genome), ', '.join(map(lambda x: f'{x:.2}',best_ind.genome_to_int_list())), f'{best_ind.fo:.2}']
df = df.reset_index()

# PRINT TABLE BLOCK
column_names_size = []
max_size = max(map(len,parameters.keys()))
max_size_val = max(map(len,map(str,parameters.values())))

print(Colors.DARK,end='')
# print(Symbols.HOR*(max_size+max_size_val+1)+Symbols.RTOP)

for key, value in parameters.items():
    print(Colors.Backgrounds.MAGENTA+key+' '*(max_size-len(key)),
          Colors.Backgrounds.BLUE+str(value)+' '*(max_size_val-len(str(value)))+Colors.RESET_BACKGROUND)
SPACED_STR = '   '
for i, col in enumerate(columns):
    col =SPACED_STR + col + SPACED_STR
    print(COLORS[i],end='')
    # curses.init_pair(i+1, curses.COLOR_BLACK, COLORS[i])
    if i != 0:
        print(col,end='')

        # stdscr.addstr(1, np.sum(column_names_size), col, curses.color_pair(i+1))
    else:
        # stdscr.addstr(1, 0, col, curses.color_pair(i+1))
        print(col,end='')
    print(Colors.RESET_BACKGROUND,end='')
    column_names_size.append(len(col))
print()
i=2

for index, row in df.iterrows():
    # string = ''.join(row.T.to_list())
    print(Colors.Backgrounds.WHITE,end='')
    for j, item in enumerate(row.T.to_list()):
        item = str(item)
        print(item,end='')
        size = len(item)
        print(" "*(len(columns[j]+SPACED_STR*2)-size),end='')
        
    print(Colors.RESET_BACKGROUND)
    i+=1

print(Colors.RESET,end='')
fout = open(DIRS['DATA_DIR']+get_parameters_name(parameters_values),'w')
fout.write(df.to_json(orient='records',lines=False))
fout.close()

# coding: utf-8
import math
import random
import argparse

import numpy as np
import pandas as pd
import yaml

from utils import *
from constants import *
from Individual import *
from Objective import *
from selection_policy import *
from mutation_policy import *
from cross_policy import *

import traceback
import warnings
import sys

def warn_with_traceback(message, category, filename, lineno, file=None, line=None):

    log = file if hasattr(file,'write') else sys.stderr
    traceback.print_stack(file=log)
    log.write(warnings.formatwarning(message, category, filename, lineno, line))

warnings.showwarning = warn_with_traceback

parser = argparse.ArgumentParser()

parameters = yaml.load(open('config.yaml'), Loader=yaml.FullLoader)

for k, v in parameters.items():
    parser.add_argument('--'+k,default=v['default'],type=type(v['default']))

args = parser.parse_args()
for k,v in vars(args).items():
    exec(f"{k} = {v}")
    exec(f"parameters['{k}']['value'] = {v}")

num_cross = int((cross_rate * num_pop)/2)
num_no_cross = num_pop-2*num_cross

# information to catch from algorithm

objective = Objective()
cross_policy = BLXa(min_value,max_value)
mutation_policy = UniformRandomSolutionSpace(mutation_rate,min_value,max_value)

population = []
for i in range(num_pop):
    ind = Individual()
    ind.rand_genome(num_genes,min_value,max_value)
    population.append(ind)
    objective.compute(ind)

columns = ['#Generation','Best genome','Best fitness','Mean fitness']
df = pd.DataFrame([],columns = columns)
df = df.set_index(columns[0])

best_ind = population[np.argmin([ind.ofv for ind in population])]
df.loc[1] = [','.join(map(lambda x: f'{x:.5f}',best_ind.genome)), f'{best_ind.ofv:.4}',np.mean([ind.ofv for ind in population])]

for i in range(2,num_generations+1):
    new_population = []
    # Cross
    choices = list(range(len(population)))
    selection_policy=Roulette(population)
    for j in range(num_cross):
        ind1=selection_policy.select()
        ind2=selection_policy.select()
        nind1, nind2 = cross_policy.cross(ind1,ind2)
        new_population.append(nind1)
        new_population.append(nind2)
    # Select the rest left of individuals if the cross rate is not 100%
    new_population.extend([population[i].__copy__()
                           for i in random.sample(list(range(len(population))),num_no_cross)])

    # Mutate these new individuals - Mutation
    for j in range(num_pop):
        mutation_policy.mutate(new_population[j])

    # Select best individual from previous population - Elitism
    new_population[random.randint(0,len(new_population)-1)]=best_ind.__copy__()
    population = new_population
    best_ind = population[0]

    for ind in population:
        objective.compute(ind)

    df.loc[i] = [','.join(map(lambda x: f'{x:.5f}',best_ind.genome)), f'{best_ind.ofv:.4}',np.mean([ind.ofv for ind in population])]
df = df.reset_index()

# PRINT TABLE BLOCK
parameters_print = {key: val
                    for key, val
                    in zip([i['pretty_name'] for i in parameters.values()],
                           [i['value'] for i in parameters.values()])}
column_names_size = []
max_size = max(map(len,parameters_print.keys()))
max_size_val = max(map(len,map(str,parameters_print.values())))

print(Colors.DARK,end='')
# print(Symbols.HOR*(max_size+max_size_val+1)+Symbols.RTOP)

for key, value in parameters_print.items():
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
fout = open(DIRS['DATA_DIR']+get_parameters_name({k: v['value'] for k,v in parameters.items()})+'.json','w')
fout.write(df.to_json(orient='records',lines=False))
fout.close()
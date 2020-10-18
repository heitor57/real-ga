# from cycler import cycler
import numpy as np
import os
from constants import *

# args = cycler('num_pop', range(2,200,25))+cycler('itr_max', range(1,100,8))\
#     +cycler('num_bits', range(2,30,2))+cycler('num_genes', range(2,6))\
#     +cycler('cross_rate', np.linspace(0,1,5))+cycler('elitism_rate', np.linspace(0,1,5))\
#     +cycler('mutateds_rate', np.linspace(0,1,5))+cycler('mutation_rate', np.linspace(0,1,5))

args = range(1,41,4)
num_args = len(args)
for i,arg in enumerate(args):
    print(f'[{i+1}/{num_args}]')
    for j in multiple_run_range:
        print(f'\t [{j}/{num_executions}]')
        os.system(f'python genetic_algorithm.py --num_generations {arg} --eid {j}')

args = range(1,201,10)
num_args = len(args)
for i,arg in enumerate(args):
    print(f'[{i+1}/{num_args}]')
    for j in multiple_run_range:
        print(f'\t [{j}/{num_executions}]')
        os.system(f'python genetic_algorithm.py --num_pop {arg} --eid {j}')

args = range(4,64,6)
num_args = len(args)
for i,arg in enumerate(args):
    print(f'[{i+1}/{num_args}]')
    for j in multiple_run_range:
        print(f'\t [{j}/{num_executions}]')
        os.system(f'python genetic_algorithm.py --num_bits {arg} --eid {j}')


args = range(4,64,6)
num_args = len(args)
for i,arg in enumerate(args):
    print(f'[{i+1}/{num_args}]')
    for j in multiple_run_range:
        print(f'\t [{j}/{num_executions}]')
        os.system(f'python genetic_algorithm.py --num_genes {arg} --eid {j}')

args = np.linspace(0.2,1,6)
num_args = len(args)
for i,arg in enumerate(args):
    print(f'[{i+1}/{num_args}]')
    for j in multiple_run_range:
        print(f'\t [{j}/{num_executions}]')
        os.system(f'python genetic_algorithm.py --cross_rate {arg} --eid {j}')


args = np.linspace(0.01,0.5,11)
num_args = len(args)
for i,arg in enumerate(args):
    print(f'[{i+1}/{num_args}]')
    for j in multiple_run_range:
        print(f'\t [{j}/{num_executions}]')
        os.system(f'python genetic_algorithm.py --mutation_rate {arg} --eid {j}')

bits = [25]
generations = [50,100]
populations = [50,100]
cross_rates = [0.6,0.8,1.0]
mutation_rates = [0.01,0.05,0.1]
i = 0
for bit in bits:
    for generation in generations:
        for population in populations:
            for cross_rate in cross_rates:
                for mutation_rate in mutation_rates:
                    for j in multiple_run_range:
                        os.system(f'python genetic_algorithm.py --num_bits={bit} --num_generations={generation} --num_pop={population} --cross_rate={cross_rate} --mutation_rate={mutation_rate} --eid {j}')
                        print(f'{i}')
                        i+=1

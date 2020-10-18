import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from constants import *
from utils import *
from tqdm import tqdm
import matplotlib 

matplotlib.rc('xtick', labelsize=14) 
matplotlib.rc('ytick', labelsize=14) 
matplotlib.rc('axes', labelsize=14) 
#matplotlib.rc('lines', linewidth=2) 

IMG = DIRS['IMG']
DATA = DIRS['DATA_DIR']

parameters_values = {
    'num_pop': NUM_POP, 'num_generations': NUM_GENERATIONS, 'num_bits': NUM_BITS,
    'num_genes': NUM_GENES, 'cross_rate': CROSS_RATE,
    'elitism_rate': ELITISM_RATE,
    'mutateds_rate': MUTATEDS_RATE,
    'mutation_rate': MUTATION_RATE,
    'eid': None,
}
bckp = parameters_values.copy()

fo_values = np.zeros(num_executions)

args = range(1,41,4)
num_args = len(args)
bests = dict()
bests_std = dict()
for i,arg in enumerate(args):
    print(f'[{i+1}/{num_args}]')
    parameters_values['num_generations'] = arg
    
    for k, j in enumerate(multiple_run_range):
        print(f'\t [{j}/{num_executions}]')
        parameters_values['eid'] = j
        name = get_parameters_name(parameters_values)
        df = pd.read_json(DATA+name)
        fo_values[k] = df['Fo'].iloc[-1]
    # fo_mean /= len(multiple_run_range)
    bests[arg] = fo_values.mean()
    bests_std[arg] = fo_values.std()
    

fig = plt.figure()
ax=fig.add_subplot(111)
ax.errorbar(list(bests.keys()),list(bests.values()),yerr=list(bests_std.values()),capsize=6,
                    color='k',marker='o',markersize=6,markerfacecolor='red',linewidth=None)
ax.set_xlabel("Quantidade de gerações")
ax.set_ylabel("Aptidão")
fig.savefig(f"{IMG}num_generations.eps",bbox_inches="tight")
fig.savefig(f"{IMG}num_generations.png",bbox_inches="tight")
parameters_values = bckp.copy()

# -----------------------------------------------------
args = range(1,201,10)
num_args = len(args)
bests = dict()
bests_std = dict()
for i,arg in enumerate(args):
    print(f'[{i+1}/{num_args}]')
    parameters_values['num_pop'] = arg
    
    for k, j in enumerate(multiple_run_range):
        print(f'\t [{j}/{num_executions}]')
        parameters_values['eid'] = j
        name = get_parameters_name(parameters_values)
        df = pd.read_json(DATA+name)
        fo_values[k] = df['Fo'].iloc[-1]
    # fo_mean /= len(multiple_run_range)
    bests[arg] = fo_values.mean()
    bests_std[arg] = fo_values.std()
    

fig = plt.figure()
ax=fig.add_subplot(111)
ax.errorbar(list(bests.keys()),list(bests.values()),yerr=list(bests_std.values()),capsize=6,
                    color='k',marker='o',markersize=6,markerfacecolor='red',linewidth=None)
ax.set_xlabel("Tamanho da população")
ax.set_ylabel("Aptidão")
fig.savefig(f"{IMG}num_pop.eps",bbox_inches="tight")
fig.savefig(f"{IMG}num_pop.png",bbox_inches="tight")
parameters_values = bckp.copy()

# -----------------------------------------------------
args = range(4,64,6)
num_args = len(args)
bests = dict()
bests_std = dict()
for i,arg in enumerate(args):
    print(f'[{i+1}/{num_args}]')
    parameters_values['num_bits'] = arg
    
    for k, j in enumerate(multiple_run_range):
        print(f'\t [{j}/{num_executions}]')
        parameters_values['eid'] = j
        name = get_parameters_name(parameters_values)
        df = pd.read_json(DATA+name)
        fo_values[k] = df['Fo'].iloc[-1]
    # fo_mean /= len(multiple_run_range)
    bests[arg] = fo_values.mean()
    bests_std[arg] = fo_values.std()
    

fig = plt.figure()
ax=fig.add_subplot(111)
ax.errorbar(list(bests.keys()),list(bests.values()),yerr=list(bests_std.values()),capsize=6,
                    color='k',marker='o',markersize=6,markerfacecolor='red',linewidth=None)
ax.set_xlabel("Quantidade de bits para representação")
ax.set_ylabel("Aptidão")
fig.savefig(f"{IMG}num_bits.eps",bbox_inches="tight")
fig.savefig(f"{IMG}num_bits.png",bbox_inches="tight")
parameters_values = bckp.copy()
# -----------------------------------------------------
args = range(4,64,6)
num_args = len(args)
bests = dict()
bests_std = dict()
for i,arg in enumerate(args):
    print(f'[{i+1}/{num_args}]')
    parameters_values['num_genes'] = arg
    
    for k, j in enumerate(multiple_run_range):
        print(f'\t [{j}/{num_executions}]')
        parameters_values['eid'] = j
        name = get_parameters_name(parameters_values)
        df = pd.read_json(DATA+name)
        fo_values[k] = df['Fo'].iloc[-1]
    # fo_mean /= len(multiple_run_range)
    bests[arg] = fo_values.mean()
    bests_std[arg] = fo_values.std()
    

fig = plt.figure()
ax=fig.add_subplot(111)
ax.errorbar(list(bests.keys()),list(bests.values()),yerr=list(bests_std.values()),capsize=6,
                    color='k',marker='o',markersize=6,markerfacecolor='red',linewidth=None)
ax.set_xlabel("Quantidade de genes")
ax.set_ylabel("Aptidão")
fig.savefig(f"{IMG}num_genes.eps",bbox_inches="tight")
fig.savefig(f"{IMG}num_genes.png",bbox_inches="tight")
parameters_values = bckp.copy()
# -----------------------------------------------------
args = np.linspace(0.2,1,6)
num_args = len(args)
bests = dict()
bests_std = dict()
for i,arg in enumerate(args):
    print(f'[{i+1}/{num_args}]')
    parameters_values['cross_rate'] = arg
    
    for k, j in enumerate(multiple_run_range):
        print(f'\t [{j}/{num_executions}]')
        parameters_values['eid'] = j
        name = get_parameters_name(parameters_values)
        df = pd.read_json(DATA+name)
        fo_values[k] = df['Fo'].iloc[-1]
    # fo_mean /= len(multiple_run_range)
    bests[arg] = fo_values.mean()
    bests_std[arg] = fo_values.std()
    

fig = plt.figure()
ax=fig.add_subplot(111)
ax.errorbar(list(bests.keys()),list(bests.values()),yerr=list(bests_std.values()),capsize=6,
                    color='k',marker='o',markersize=6,markerfacecolor='red',linewidth=None)
ax.set_xlabel("Taxa de cruzamento")
ax.set_ylabel("Aptidão")
fig.savefig(f"{IMG}cross_rate.eps",bbox_inches="tight")
fig.savefig(f"{IMG}cross_rate.png",bbox_inches="tight")
parameters_values = bckp.copy()

-----------------------------------------------------
args = np.linspace(0.01,0.5,11)
num_args = len(args)
bests = dict()
bests_std = dict()
for i,arg in enumerate(args):
    print(f'[{i+1}/{num_args}]')
    parameters_values['mutation_rate'] = arg
    
    for k, j in enumerate(multiple_run_range):
        print(f'\t [{j}/{num_executions}]')
        parameters_values['eid'] = j
        name = get_parameters_name(parameters_values)
        df = pd.read_json(DATA+name)
        fo_values[k] = df['Fo'].iloc[-1]
    # fo_mean /= len(multiple_run_range)
    bests[arg] = fo_values.mean()
    bests_std[arg] = fo_values.std()
    

fig = plt.figure()
ax=fig.add_subplot(111)
ax.errorbar(list(bests.keys()),list(bests.values()),yerr=list(bests_std.values()),capsize=6,
                    color='k',marker='o',markersize=6,markerfacecolor='red',linewidth=None)
ax.set_xlabel("Taxa de mutação")
ax.set_ylabel("Aptidão")
fig.savefig(f"{IMG}mutation_rate.eps",bbox_inches="tight")
fig.savefig(f"{IMG}mutation_rate.png",bbox_inches="tight")
parameters_values = bckp.copy()


bits = [25]
generations = [50,100]
populations = [50,100]
cross_rates = [0.6,0.8,1.0]
mutation_rates = [0.01,0.05,0.1]
i = 0

result = {}
for bit in bits:
    for generation in generations:
        for population in populations:
            for cross_rate in cross_rates:
                for mutation_rate in mutation_rates:
                    parameters_values['num_bits']=bit
                    parameters_values['num_generations']=generation
                    parameters_values['num_pop']=population
                    parameters_values['cross_rate']=cross_rate
                    parameters_values['mutation_rate']=mutation_rate
                    for k,j in enumerate(multiple_run_range):
                        parameters_values['eid']=j
                        name = get_parameters_name(parameters_values)
                        print(DATA+name)
                        df = pd.read_json(DATA+name,lines=False)
                        fo_values[k] = df['Fo'].iloc[-1]
                        print(f'{i}')
                        i+=1
                    del parameters_values['eid']
                    result[tuple(parameters_values.values())] = (fo_values.mean(),fo_values.std())
print(parameters_values.keys())
for k,v in sorted(result.items(), key=lambda x: x[1])[:10]:
    print(k,v[0],',',v[1])
parameters_values = bckp.copy()


parameters_values['num_pop']=100
parameters_values['num_generations']=100
parameters_values['num_bits']=25
parameters_values['cross_rate']=0.8
parameters_values['mutation_rate']=0.01

fig, ax = plt.subplots()
for k,j in enumerate(multiple_run_range):
    parameters_values['eid']=j
    name = get_parameters_name(parameters_values)
    df = pd.read_json(DATA+name,lines=False)
    
    ax.plot(df['Fo'],label=f'Execução {k+1}')

ax.set_ylabel("Aptidão")
ax.set_xlabel("Geração")
ax.legend()
fig.savefig(f"{IMG}best_executions.eps",bbox_inches="tight")
fig.savefig(f"{IMG}best_executions.png",bbox_inches="tight")
parameters_values = bckp.copy()

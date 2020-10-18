from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
import os
import multiprocessing
import numpy as np

def dict_to_list_gen(d):
    for k, v in zip(d.keys(), d.values()):
        if v == None:
            continue
        yield k
        yield v

def dict_to_list(d):
    return list(dict_to_list_gen(d))

def get_parameters_name(parameters):
    # parameters = {k:v for k,v in parameters if v}
    list_parameters=list(map(str,dict_to_list(parameters)))
    return '_'.join(list_parameters)

def run_parallel(func, args,chunksize = None,use_tqdm=True):
    executor = ProcessPoolExecutor()
    num_args = len(args)
    if not chunksize:
        chunksize = int(num_args/multiprocessing.cpu_count())
    if use_tqdm:
        ff = tqdm
    else:
        ff = lambda x,*y,**z: x 
    results = [i for i in ff(executor.map(func,*list(zip(*args)),chunksize=chunksize),total=num_args)]
    return results


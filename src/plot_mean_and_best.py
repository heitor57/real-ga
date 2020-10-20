import argparse
from pathlib import Path
import yaml
from lib.utils import *
import pandas as pd
import matplotlib.pyplot as plt
parser = argparse.ArgumentParser()
config = yaml.load(open('config.yaml'), Loader=yaml.FullLoader)
parameters = config['parameters']
for k, v in parameters.items():
    parser.add_argument('--'+k,default=v['default'],
                        type=str2bool if type(v['default']) == bool else type(v['default']))

args = parser.parse_args()
for k,v in vars(args).items():
    locals()[k] = v
    parameters[k]['value'] = v


# dfs = []
# for i in range(1,NUM_EXECUTIONS+1):
#     parameters.update({'eid': i})
fig, ax = plt.subplots()
name=get_parameters_name({k: v['value'] for k,v in parameters.items()})

df = pd.read_json(DIRS['DATA']+name+'.json')
ax.plot(df['Best fitness'],label='Melhor aptidão')
ax.plot(df['Mean fitness'],label='Aptidão média')
ax.plot(df['Median fitness'],label='Aptidão mediana')
ax.plot(df['Worst fitness'],label='Pior Aptidão')
ax.set_ylabel("Aptidão")
ax.set_xlabel("Geração")
ax.legend()
fig.savefig(f"{DIRS['IMG']}{name}_mean_and_median_and_best.png",bbox_inches="tight")
# dfs.append(df)
    # Path(os.path.dirname(DIRS['DATA']+name)).mkdir(parents=True, exist_ok=True)

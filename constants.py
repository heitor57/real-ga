from pathlib import Path
class Colors:
    RESET = '\033[0m'
    DARK = '\033[30m'
    RESET_FOREGROUND = '\033[39m'
    RESET_BACKGROUND = '\033[49m'

    class Backgrounds:
        YELLOW = '\033[43m'
        WHITE = '\033[47m'
        RED = '\033[41m'
        GREEN = '\033[42m'
        BLUE = '\033[44m'
        MAGENTA = '\033[45m'
        CYAN = '\033[46m'

class Symbols:
    HOR = '─'
    VER = '│'
    RTOP = '┐'
    RBOT = '┘'

COLORS = [Colors.Backgrounds.RED, Colors.Backgrounds.GREEN, Colors.Backgrounds.YELLOW, Colors.Backgrounds.BLUE, Colors.Backgrounds.MAGENTA, Colors.Backgrounds.CYAN]

DIRS = {'DATA_DIR': 'data/', 'IMG': 'img/'}
for d in DIRS.values():
    Path(d).mkdir(parents=True, exist_ok=True)

parameters_pretty_name = {
    'num_pop': '#Population', 'num_generations': '#Generations', 'num_bits': '#Bits',
    'num_genes': '#Genes', 'cross_rate': 'Cross rate',
    'elitism_rate': 'Elitism rate',
    'mutateds_rate': 'Mutateds rate',
    'mutation_rate': 'Mutation rate',
    'eid': 'Execution id',
}

columns = ['#Generation','Best genome (bin)','Best genome (dec)','Fo']

X_MAX = 2 # Linear space maximum number
X_MIN = -2 # Linear space minimum number
NUM_POP = 50 # Population size
NUM_GENERATIONS = 50 # Number of generations
NUM_BITS = 6 # Number of bits of the discrete search space
NUM_GENES = 2 # Number of genes
CROSS_RATE = 1.0 # Rate of individuals who are going to be crossed instead of being preserved from previous generation, commonly it is going to stay in 1.0 but to be more flexible it is presented as a variable
ELITISM_RATE = 0.05 # Rate of best individuals to be preserved from the previous generation
MUTATION_RATE = 0.01 # Probability to cause a change in a bit of a gene of any individual
MUTATEDS_RATE = 1.0 # Rate of the population to be mutated - default to 1.0
MAINTAIN_WINNER_PROBABILITY = 0.9 # Probability to maintain the winner when getting parents


# Execution parameters

num_executions = 10
multiple_run_range = range(1,num_executions+1)

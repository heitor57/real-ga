import random
class Individual:
    def __init__(self,genome=[]):
        self.genome = genome
        self.ofv = None

    def rand_genome(self,num_genes,min_value,max_value):
        self.genome = []
        for i in range(num_genes):
            self.genome.append(random.uniform(min_value,max_value))
        return self.genome

    def __copy__(self):
        new_ind = Individual()
        new_ind.genome = self.genome.copy()
        new_ind.ofv = self.ofv
        return new_ind
    def __str__(self):
        return 'genome = '+','.join(map(lambda x: f'{x:.5f}',self.genome)) + f', fo = {self.ofv}'

class Individual:
    def __init__(self,genome=[]):
        self.genome = genome
        self.ofv = None

    def rand_genome(self):
        self.genome = []
        for i in range(num_genes):
            self.genome.append(random.uniform(X_MIN,X_MAX))
        return self.genome
    
    def __str__(self):
        return 'genome = '+''.join(self.genome) + f', fo = {self.ofv}'

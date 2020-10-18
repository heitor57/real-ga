import random
class MutationPolicy:
    pass

class UniformRandomSolutionSpace(MutationPolicy):
    def __init__(self,probability,min_value,max_value):
        self.probability = probability
        self.min_value = min_value
        self.max_value = max_value
    
    def mutate(self,ind):
        new_genome = [random.uniform(self.min_value,self.max_value)
                      if self.probability > random.random()
                      else
                      i
                      for i in ind.genome]
        ind.genome = new_genome
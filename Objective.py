import math
import numpy as np
class Objective:
    def compute(self,ind):
        f=self._compute(ind.genome)
        ind.ofv = f
        return f

    def _compute(self,x):
        n = float(len(x))
        f_exp = -0.2 * math.sqrt(1/n * sum(np.power(x, 2)))

        t = 0
        for i in range(0, len(x)):
                t += np.cos(2 * math.pi * x[i])

        s_exp = 1/n * t
        f = -20 * math.exp(f_exp) - math.exp(s_exp) + 20 + math.exp(1)
        return f

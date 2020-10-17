import numpy as np
class CrossPolicy:
    pass

class BLXa(CrossPolicy):
    def __init__(self,alpha=0.5):
        self.alpha=alpha
    def cross(self,ind1,ind2):
        nind1= Individual()
        nind2= Individual()
        i = 0
        for ofv1, ofv2 in zip(ind1.genome,ind2.genome):
            d= abs(ofv1-ofv2)
            min_value = min(ofv1,ofv2)
            max_value = max(ofv1,ofv2)
            nind1.genome[i] = random.uniform(min_value-self.alpha*d,max_value+self.alpha*d)
            nind2.genome[i] = random.uniform(min_value-self.alpha*d,max_value+self.alpha*d)
            i+=1

        return nind1, nind2

class BLXab(CrossPolicy):
    def __init__(self,alpha=0.75,beta=0.5):
        self.alpha=alpha
        self.beta=beta

    def cross(self,ind1,ind2):
        nind1= Individual()
        nind2= Individual()
        if ind1.ofv < ind2.ofv:
            ind1, ind2 = ind2, ind1

        i = 0
        for ofv1, ofv2 in zip(ind1.genome,ind2.genome):
            d= abs(ofv1-ofv2)
            if ofv1 <= ofv2:
                nind1.genome[i]=random.uniform(ofv1-self.alpha*d,ofv2+self.alpha*d)
                nind2.genome[i]=random.uniform(ofv1-self.alpha*d,ofv2+self.alpha*d)
            else:
                nind1.genome[i]=random.uniform(ofv2-self.beta*d,ofv1+self.alpha*d)
                nind2.genome[i]=random.uniform(ofv2-self.beta*d,ofv1+self.alpha*d)
            i+=1

        return nind1, nind2

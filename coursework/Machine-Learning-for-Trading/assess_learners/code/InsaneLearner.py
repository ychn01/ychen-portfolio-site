import numpy as np
import LinRegLearner as lrl
import BagLearner as bl
class InsaneLearner(object):
    def __init__(self, verbose=False):
        self.verbose = verbose   
        self.instances = 20
        self.learners = []
        self.learner = bl.BagLearner(learner=lrl.LinRegLearner,kwargs={},bags=self.instances,boost=False,verbose=self.verbose)
    def author(self):
        return "ychen3281"  
    def add_evidence(self, data_x, data_y): 
        for n in range(self.instances):
            self.learner.add_evidence(data_x, data_y)        
    def query(self, points): 
        preds = []
        for l in self.learners:
            preds.append(l.query(points))
        return np.mean(preds, axis=0) 

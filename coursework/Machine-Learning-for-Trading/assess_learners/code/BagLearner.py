import numpy as np

class BagLearner(object):
    def __init__(self, learner, kwargs = {}, bags = 20, boost = False, verbose = False):
        self.learner = learner
        self.learners=[]
        self.bags=bags
        self.kwargs={"k":10}
        self.boost=boost
        self.verbose=verbose
        for i in range(0,self.bags):  
            self.learners.append(self.learner(**kwargs)) 
            
    def author(self):
        return "ychen3281"
    
    def add_evidence(self, data_x, data_y):
        num_rows = data_x.shape[0]

        for l in self.learners:
            rand_row = np.random.randint(0, num_rows, size=num_rows)
            new_x = data_x[rand_row,:]
            new_y = data_y[rand_row] 
            
            l.add_evidence(new_x, new_y)
            
    def query(self, points):
        preds = []
        for l in self.learners:
            preds.append(l.query(points))
        return np.mean(preds, axis=0)

    
    if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
        print("the secret clue is 'zzyzx'") 


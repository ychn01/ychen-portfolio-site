""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
Test a learner.  (c) 2015 Tucker Balch  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import math  		  	   		  		 		  		  		    	 		 		   		 		  
import sys  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  		 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt  		  	   		  		 		  		  		    	 		 		   		 		  
import LinRegLearner as lrl  	
import DTLearner as dt
import RTLearner as rt
import BagLearner as bl
import InsaneLearner as it 
	  	   		  		 		  		  		    	 		 		   		 		  
np.random.seed(903566160) 		  	   		  		 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    if len(sys.argv) != 2:  		  	   		  		 		  		  		    	 		 		   		 		  
        print("Usage: python testlearner.py <filename>")  		  	   		  		 		  		  		    	 		 		   		 		  
        sys.exit(1)  		  	   		  		 		  		  		    	 		 		   		 		  
    inf = open(sys.argv[1])
    lines = inf.readlines()
    del lines[0]  		  	   		  		 		  		  		    	 		 		   		 		  
    data = np.array(  		  	   		  		 		  		  		    	 		 		   		 		  
        [list(map(float, s.strip().split(",")[1:])) for s in lines])  	
# with open('Istanbul.csv') as f:
#     lines = f.readlines()
#     del lines[0]
#     data = np.array(  		  	   		  		 		  		  		    	 		 		   		 		  
#         [list(map(float, s.strip().split(",")[1:])) for s in lines]  		  	   		  		 		  		  		    	 		 		   		 		  
#     )  		  	   		  		 		  		  		    	 		 		   		 		  
    
    new_rows = np.arange(data.shape[0])
    np.random.shuffle(new_rows)
    new_data = data[new_rows]
    
    # compute how much of the data is training and testing  		  	   		  		 		  		  		    	 		 		   		 		  
    train_rows = int(0.6 * new_data.shape[0])  		  	   		  		 		  		  		    	 		 		   		 		  
    test_rows = new_data.shape[0] - train_rows
          
    # separate out training and testing data  		  	   		  		 		  		  		    	 		 		   		 		  
    train_x = new_data[:train_rows, 0:-1]  		  	   		  		 		  		  		    	 		 		   		 		  
    train_y = new_data[:train_rows, -1]  		  	   		  		 		  		  		    	 		 		   		 		  
    test_x = new_data[train_rows:, 0:-1]  		  	   		  		 		  		  		    	 		 		   		 		  
    test_y = new_data[train_rows:, -1]  		  	  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  	  	   		  		 		  		  		    	 		 		   		 		  

    ### Experiment 1	
    #create dt learner
    def experiment_1(learner=dt.DTLearner, leaf_size = np.arange(1,51)):
        in_rmse = []
        out_rmse = []
        for n in leaf_size:
            dt_learner = learner(leaf_size=n, verbose=False) 	  	   		  		 		  		  		    	 		 		   		 		  
            dt_learner.add_evidence(train_x, train_y)  

            # evaluate in sample  		  	   		  		 		  		  		    	 		 		   		 		  
            in_pred_y = dt_learner.query(train_x)  # get the predictions  		  	   		  		 		  		  		    	 		 		   		 		  
            in_rmse.append(math.sqrt(((train_y - in_pred_y) ** 2).sum() / train_y.shape[0]))  		  	   		  		 		  		  		    	 		 		   		 		  
            in_c = np.corrcoef(in_pred_y, y=train_y)  		  	   		  		 		  		  		    	 		 		   		 		  

            # evaluate out of sample  		  	   		  		 		  		  		    	 		 		   		 		  
            out_pred_y = dt_learner.query(test_x)  # get the predictions  		  	   		  		 		  		  		    	 		 		   		 		  
            out_rmse.append(math.sqrt(((test_y - out_pred_y) ** 2).sum() / test_y.shape[0]))
            out_c = np.corrcoef(out_pred_y, y=test_y)

        print(in_rmse)
        print(out_rmse)
        #graph/chart
        plt.plot(leaf_size, in_rmse, label="In Sample RMSE")
        plt.plot(leaf_size, out_rmse, label="Out of Sample RMSE")
        plt.xlabel("Leaf Size")
        plt.ylabel("RMSE")
        plt.title("DTLearner: Leaf Size vs RMSE")
        plt.grid()
        plt.margins(x=0)
        plt.legend()
        plt.savefig("Experiment_1.png")
        plt.clf()
        
    ### Experiment 2
    def experiment_2(learner=bl.BagLearner, leaf_size = np.arange(1,51), bag=10):
        in_rmse = []
        out_rmse = []
        for n in leaf_size:
            bag_dt_learner = learner(learner=dt.DTLearner, kwargs={"leaf_size": n}, bags=bag, boost=False, verbose=False) 	  	   		  		 		  		  		    	 		 		   		 		  
            bag_dt_learner.add_evidence(train_x, train_y)  
        
            # evaluate in sample  		  	   		  		 		  		  		    	 		 		   		 		  
            in_pred_y = bag_dt_learner.query(train_x)  # get the predictions  		  	   		  		 		  		  		    	 		 		   		 		  
            in_rmse.append(math.sqrt(((train_y - in_pred_y) ** 2).sum() / train_y.shape[0]))  		  	   		  		 		  		  		    	 		 		   		 		  	  	   		  		 		  		  		    	 		 		   		 		  
            in_c = np.corrcoef(in_pred_y, y=train_y)  		 		  	   		  		 		  		  		    	 		 		   		 		  

            # evaluate out of sample  		  	   		  		 		  		  		    	 		 		   		 		  
            out_pred_y = bag_dt_learner.query(test_x)  # get the predictions  		  	   		  		 		  		  		    	 		 		   		 		  
            out_rmse.append(math.sqrt(((test_y - out_pred_y) ** 2).sum() / test_y.shape[0]))	  	   		  		 		  		  		    	 		 		   		 		  
            out_c = np.corrcoef(out_pred_y, y=test_y)  	
        
        #graph/chart
        plt.plot(leaf_size, in_rmse, label="In Sample RMSE")
        plt.plot(leaf_size, out_rmse, label="Out of Sample RMSE")
        plt.xlabel("Leaf Size")
        plt.ylabel("RMSE")
        plt.title(f"Bag size {bag} DTLearner: Leaf Size vs RMSE")
        plt.grid()
        plt.margins(x=0)
        plt.legend()
        plt.savefig(f"Experiment_2_bagsize{bag}.png")
        plt.clf()
        
        
    ### Experiment 3_1 using MAPE
    def experiment_3_1(learner_1=dt.DTLearner, learner_2=rt.RTLearner, leaf_size = np.arange(1,51)):
        rt_mape = []
        dt_mape = []
        for n in leaf_size:
            dt_learner = learner_1(leaf_size=n, verbose=False) 	  	   		  		 		  		  		    	 		 		   		 		  
            dt_learner.add_evidence(train_x, train_y)
            
            rt_learner = learner_2(leaf_size=n, verbose=False) 	  	   		  		 		  		  		    	 		 		   		 		  
            rt_learner.add_evidence(train_x, train_y)

            # evaluate DTLearner  		  	   		  		 		  		  		    	 		 		   		 		  
            dt_pred_y = dt_learner.query(test_x)  # get the predictions  		  	   		  		 		  		  		    	 		 		   		 		  
            dt_mape.append(np.mean(abs((test_y - dt_pred_y).sum() / test_y.shape[0]))*100)  		  		 		  		  		    	 		 		   		 		  

            # evaluate RTlearner		  	   		  		 		  		  		    	 		 		   		 		  
            rt_pred_y = rt_learner.query(test_x)  # get the predictions  		  	   		  		 		  		  		    	 		 		   		 		  
            rt_mape.append(np.mean(abs((test_y - rt_pred_y).sum() / test_y.shape[0]))*100)
        
        
        #graph/chart
        plt.plot(leaf_size, dt_mape, label="DTLearner MAPE")
        plt.plot(leaf_size, rt_mape, label="RTLearner MAPE")
        plt.xlabel("Leaf Size")
        plt.ylabel("MAPE")
        plt.title("DT vs RT with Mean Absolute Percentage Error (MAPE)")
        plt.grid()
        plt.margins(x=0)
        plt.legend()
        plt.savefig("Experiment_3_1.png")
        plt.clf()
        
    ### Experiment 3_2 using R^2
    def experiment_3_2(learner_1=dt.DTLearner, learner_2=rt.RTLearner, leaf_size = np.arange(1,51)):
        rt_r2 = []
        dt_r2 = []
        for n in leaf_size:
            dt_learner = learner_1(leaf_size=n, verbose=False) 	  	   		  		 		  		  		    	 		 		   		 		  
            dt_learner.add_evidence(train_x, train_y)
            
            rt_learner = learner_2(leaf_size=n, verbose=False) 	  	   		  		 		  		  		    	 		 		   		 		  
            rt_learner.add_evidence(train_x, train_y)

            # evaluate DTLearner  		  	   		  		 		  		  		    	 		 		   		 		  
            dt_pred_y = dt_learner.query(test_x)  # get the predictions  		  	   		  		 		  		  		    	 		 		   		 		 
            dt_r2.append(1-(((test_y - dt_pred_y)**2).sum())/((test_y - np.mean(test_y))**2).sum()) 		  		 		  		  		    	 		 		   		 		  

            # evaluate RTlearner		  	   		  		 		  		  		    	 		 		   		 		  
            rt_pred_y = rt_learner.query(test_x)  # get the predictions  		  	   		  		 		  		  		    	 		 		   		 		  
            rt_r2.append(1-(((test_y - rt_pred_y)**2).sum())/((test_y - np.mean(test_y))**2).sum())

    
        #graph/chart
        plt.plot(leaf_size, dt_r2, label="DTLearner R^2")
        plt.plot(leaf_size, rt_r2, label="RTLearner R^2")
        plt.xlabel("Leaf Size")
        plt.ylabel("R-Squared")
        plt.title("DT vs RT with Coefficient of Determination (R-Squared)")
        plt.grid()
        plt.margins(x=0)
        plt.legend()  
        plt.savefig("Experiment_3_2.png")
        plt.clf()
        
    experiment_1()
    experiment_2(bag=10)
    experiment_2(bag=25)
    experiment_2(bag=50)
    experiment_3_1()
    experiment_3_2()
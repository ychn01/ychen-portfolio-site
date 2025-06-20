import numpy as np

class DTLearner(object):
    def __init__(self, leaf_size=1, verbose=False): 
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.tree = None
    
    def author(self):
        return "ychen3281"
    
    def add_evidence(self, data_x, data_y):  
        """  		  	   		  		 		  		  		    	 		 		   		 		  
        Add training data to learner  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
        :param data_x: A set of feature values used to train the learner  		  	   		  		 		  		  		    	 		 		   		 		  
        :type data_x: numpy.ndarray  		  	   		  		 		  		  		    	 		 		   		 		  
        :param data_y: The value we are attempting to predict given the X data  		  	   		  		 		  		  		    	 		 		   		 		  
        :type data_y: numpy.ndarray  		  	   		  		 		  		  		    	 		 		   		 		  
        """ 
        # Putting back train data into 2D array for build_tree
        data = np.column_stack((data_x, data_y))
        self.tree = self.build_tree(data)
    
    def best_feature_index(self, data_x, data_y):
        feature_count = data_x.shape[1]
        abs_corr = np.zeros(feature_count)  
        for i in range(feature_count):
            corr = np.corrcoef(data_x[:, i], data_y)[0, 1]
            abs_corr[i] = np.abs(corr)
        return np.argmax(abs_corr)
        
    def build_tree(self, data):    
        #Spitting train data into X and y
        data_x = data[:, :-1]
        data_y = data[:, -1]
        
        if data.shape[0] <= self.leaf_size:
            return np.array([-1, np.mean(data_y), -1, -1])
        if len(set(data_y)) == 1:
            return np.array([-1, set(data_y).pop(), -1, -1])
        else:
            i = self.best_feature_index(data_x, data_y)
            split_val = np.median(data_x[:,i])
            if np.array_equal(data[data[:,i] <= split_val], data):
                return np.array([[-1, np.mean(data[:, -1]), -1, -1]])
            left_tree = self.build_tree(data[data[:,i] <= split_val])
            right_tree = self.build_tree(data[data[:,i] > split_val])
            root = np.array([i, split_val, 1, left_tree.shape[0]+1])

            return np.vstack((root, left_tree, right_tree))
     
    def query(self, points): 
        """  		  	   		  		 		  		  		    	 		 		   		 		  
        Estimate a set of test points given the model we built.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
        :param points: A numpy array with each row corresponding to a specific query.  		  	   		  		 		  		  		    	 		 		   		 		  
        :type points: numpy.ndarray  		  	   		  		 		  		  		    	 		 		   		 		  
        :return: The predicted result of the input data according to the trained model  		  	   		  		 		  		  		    	 		 		   		 		  
        :rtype: numpy.ndarray  		  	   		  		 		  		  		    	 		 		   		 		  
        """  
        predict = np.array([])
        for p in points:
            node_idx = 0
            while self.tree[node_idx, 0] != -1:
                node = self.tree[node_idx]
                feature_idx, split_val, left_idx, right_idx = node[0], node[1], node[2], node[3]
                #print(feature_idx, split_val, left_idx, right_idx)
                if p[int(feature_idx)] <= split_val:
                    node_idx += 1
                else:
                    node_idx += int(left_idx)
            predict = np.append(predict, node[1])
        return predict


if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    print("the secret clue is 'zzyzx'") 
    


#quinlann approach
'''
build_tree(data)
    if data.shape[0] == 1:
        return [leaf, data.y, NA, NA]
    
    if all data.y same:
        return [leaf, data.y, NA, NA]
    
    else:
        #determine best feature i to split on
        SplitVal = data[:, ].median()
        lefttree = build_tree(data(data[:,i<=SplitVal]))
        righttree = build_tree(data(data[:,i>SplitVal]))
        root = [i,SplitVal, 1, lefttree.shape[0]+1]
        return append(root,lefttree, righttree)
'''   
        
#determining the best feature
'''
    1.entrophy(most used method)
    2.correlation(for this project)
    3. gini index
'''
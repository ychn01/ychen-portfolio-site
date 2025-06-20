import numpy as np

class RTLearner(object):
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
        return np.random.randint(0, data_x.shape[1])
        
    def build_tree(self,data):

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
            
            if np.all(data_x[:,i] <= split_val):
                return np.array([[-1, np.mean(data_y), -1, -1]])
            
            left_tree = self.build_tree(data[data[:,i] <= split_val])
            right_tree = self.build_tree(data[data[:,i] > split_val])
            
            if len(left_tree.shape) <= 1:
                root = np.array([i, split_val, 1, 2])
            if len(left_tree.shape) > 1:
                root = np.array([i, split_val, 1, left_tree.shape[0]+1]) 
                
            dt = np.vstack((root, left_tree, right_tree))
            
            return dt


    def query(self, points): 
        predict= np.zeros((points.shape[0]))
        for i, p in enumerate(points):
            node_idx = 0
            while self.tree[node_idx, 0] != -1:
                node = self.tree[node_idx]
                feature_idx, split_val, left_idx, right_idx = node[0], node[1], node[2], node[3]
                if p[int(feature_idx)] <= split_val:
                    node_idx += int(left_idx)
                else:
                    node_idx += int(right_idx)
            predict[i] = self.tree[node_idx, 1]
    
        return predict 
    
#random tree by A cutler approach
'''
build_tree(data)
    if data.shape[0] == 1:
        return [leaf, data.y, NA, NA]
    
    if all data.y same:
        return [leaf, data.y, NA, NA]
    
    else:
        #determine random feature i to split on
        SplitVal = (data[random,i] + data[random,i])/2
        lefttree = build_tree(data(data[:,i<=SplitVal]))
        righttree = build_tree(data(data[:,i>SplitVal]))
        root = [i,SplitVal, 1, lefttree.shape[0]+1]
        return append(root,lefttree, righttree)
'''    
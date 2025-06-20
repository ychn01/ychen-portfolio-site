""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
Template for implementing QLearner  (c) 2015 Tucker Balch  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All RighT_table Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserT_table copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projecT_table assigned in this course. StudenT_table  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-studenT_table such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
studenT_table of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Student Name: Yu-Xi Chen 		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: ychen3281  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 903566160 		  	   		  		 		  		  		    	 		 		   		 		  
"""  	 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import random as rand  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
class QLearner(object):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    This is a Q learner object.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param num_states: The number of states to consider.  		  	   		  		 		  		  		    	 		 		   		 		  
    :type num_states: int  		  	   		  		 		  		  		    	 		 		   		 		  
    :param num_actions: The number of actions available..  		  	   		  		 		  		  		    	 		 		   		 		  
    :type num_actions: int  		  	   		  		 		  		  		    	 		 		   		 		  
    :param alpha: The learning rate used in the update rule. Should range between 0.0 and 1.0 with 0.2 as a typical value.  		  	   		  		 		  		  		    	 		 		   		 		  
    :type alpha: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :param gamma: The discount rate used in the update rule. Should range between 0.0 and 1.0 with 0.9 as a typical value.  		  	   		  		 		  		  		    	 		 		   		 		  
    :type gamma: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :param rar: Random action rate: the probability of selecting a random action at each step. Should range between 0.0 (no random actions) to 1.0 (always random action) with 0.5 as a typical value.  		  	   		  		 		  		  		    	 		 		   		 		  
    :type rar: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :param radr: Random action decay rate, after each update, rar = rar * radr. Ranges between 0.0 (immediate decay to 0) and 1.0 (no decay). Typically 0.99.  		  	   		  		 		  		  		    	 		 		   		 		  
    :type radr: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :param dyna: The number of dyna updates for each regular update. When Dyna is used, 200 is a typical value.  		  	   		  		 		  		  		    	 		 		   		 		  
    :type dyna: int  		  	   		  		 		  		  		    	 		 		   		 		  
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  		 		  		  		    	 		 		   		 		  
    :type verbose: bool  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    def __init__(  		  	   		  		 		  		  		    	 		 		   		 		  
        self,  		  	   		  		 		  		  		    	 		 		   		 		  
        num_states=100,  		  	   		  		 		  		  		    	 		 		   		 		  
        num_actions=4,  		  	   		  		 		  		  		    	 		 		   		 		  
        alpha=0.2,  		  	   		  		 		  		  		    	 		 		   		 		  
        gamma=0.9,  		  	   		  		 		  		  		    	 		 		   		 		  
        rar=0.5,  		  	   		  		 		  		  		    	 		 		   		 		  
        radr=0.99,  		  	   		  		 		  		  		    	 		 		   		 		  
        dyna=0,  		  	   		  		 		  		  		    	 		 		   		 		  
        verbose=False,  		  	   		  		 		  		  		    	 		 		   		 		  
    ):  		  	   		  		 		  		  		    	 		 		   		 		  
        """  		  	   		  		 		  		  		    	 		 		   		 		  
        Constructor method  		  	   		  		 		  		  		    	 		 		   		 		  
        """  		  	   		  		 		  		  		    	 		 		   		 		  
        self.verbose = verbose  	
        self.num_states = num_states	  	   		  		 		  		  		    	 		 		   		 		  
        self.num_actions = num_actions  		  	   		  		 		  		  		    	 		 		   		 		  
        self.s = 0  		  	   		  		 		  		  		    	 		 		   		 		  
        self.a = 0  	
        
        self.alpha = alpha
        self.gamma = gamma
        self.rar = rar
        self.radr = radr
        self.dyna = dyna
        
        self.Q_table = np.zeros((num_states, num_actions))	
        self.T_table = []  		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    def querysetstate(self, s):  		  	   		  		 		  		  		    	 		 		   		 		  
        """  		  	   		  		 		  		  		    	 		 		   		 		  
        Update the state without updating the Q-table  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
        :param s: The new state  		  	   		  		 		  		  		    	 		 		   		 		  
        :type s: int  		  	   		  		 		  		  		    	 		 		   		 		  
        :return: The selected action  		  	   		  		 		  		  		    	 		 		   		 		  
        :rtype: int  		  	   		  		 		  		  		    	 		 		   		 		  
        """  		  	   		  		 		  		  		    	 		 		   		 		  
        self.s = s  		  	   		  		 		  		  		    	 		 		   		 		  
        action = rand.randint(0, self.num_actions - 1)  		  	   		  		 		  		  		    	 		 		   		 		  
        if self.verbose:  		  	   		  		 		  		  		    	 		 		   		 		  
            print(f"s = {s}, a = {action}")  		  	   		  		 		  		  		    	 		 		   		 		  
        return action  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    def query(self, s_prime, r):  		  	   		  		 		  		  		    	 		 		   		 		  
        """  		  	   		  		 		  		  		    	 		 		   		 		  
        Update the Q table and return an action  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
        :param s_prime: The new state  		  	   		  		 		  		  		    	 		 		   		 		  
        :type s_prime: int  		  	   		  		 		  		  		    	 		 		   		 		  
        :param r: The immediate reward  		  	   		  		 		  		  		    	 		 		   		 		  
        :type r: float  		  	   		  		 		  		  		    	 		 		   		 		  
        :return: The selected action  		  	   		  		 		  		  		    	 		 		   		 		  
        :rtype: int  		  	   		  		 		  		  		    	 		 		   		 		  
        """  		  	
        
        if rand.uniform(0,1) < self.rar:
            action = rand.randint(0, self.num_actions - 1)
        else:
            action = np.argmax(self.Q_table[s_prime])
            
        self.T_table.append((self.s, self.a, s_prime, r))
        self.rar = self.rar * self.radr  		  		 	
             	   	 		 		   		 		  
        improved_est = r + self.gamma * np.max(self.Q_table[s_prime])
        self.Q_table[self.s, self.a] = (1 - self.alpha) * self.Q_table[self.s, self.a] + self.alpha * improved_est

        if self.dyna >= 1:
            for i in range(self.dyna):
                if len(self.T_table) >= 1:
                    ind = rand.randint(0, len(self.T_table) - 1)
                    r_s, r_a, r_s_prime, r_r = self.T_table[ind]
            
                    hallu_improved_est = r_r + self.gamma * np.max(self.Q_table[r_s_prime])
                    self.Q_table[r_s, r_a] = (1 - self.alpha) * self.Q_table[r_s, r_a] + self.alpha * hallu_improved_est
        
        self.s = s_prime
        self.a = action
        
        if self.verbose:
            print(f"s = {s_prime}, a = {self.a}, r = {r}")
            
        return action

    		  		  		    	 		 		   		 		  
    def author(self): 
        return 'ychen3281' 		
      		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    print("Remember Q from Star Trek? Well, this isn't him")  		  	   		  		 		  		  		    	 		 		   		 		  

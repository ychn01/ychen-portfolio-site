""""""  		  	   		  		 			  		 			 	 	 		 		 	
"""Assess a betting strategy.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
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
  		  	   		  		 			  		 			 	 	 		 		 	
Student Name: Yu-Xi Chen 		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: ychen3281"	  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 903566160

This code is was used previously in ML4T for the 2023 summer term, but I had dropped the course.  		  	   		  		 		  		  		    	 		 		   		 		  
"""  	  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
import numpy as np  		  	   		  		 			  		 			 	 	 		 		 	
import matplotlib.pyplot as plt		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def author():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    :return: The GT username of the student  		  	   		  		 			  		 			 	 	 		 		 	
    :rtype: str  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    return "ychen3281"  # replace tb34 with your Georgia Tech username.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def gtid():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    :return: The GT ID of the student  		  	   		  		 			  		 			 	 	 		 		 	
    :rtype: int  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    return 903566160  # replace with your GT ID number  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def get_spin_result(win_prob):  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    :param win_prob: The probability of winning  		  	   		  		 			  		 			 	 	 		 		 	
    :type win_prob: float  		  	   		  		 			  		 			 	 	 		 		 	
    :return: The result of the spin.  		  	   		  		 			  		 			 	 	 		 		 	
    :rtype: bool  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    result = False  		  	   		  		 			  		 			 	 	 		 		 	
    if np.random.random() <= win_prob:  		  	   		  		 			  		 			 	 	 		 		 	
        result = True  		  	   		  		 			  		 			 	 	 		 		 	
    return result  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def test_code():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    Method to test your code  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    win_prob = 0.60  # set appropriately to the probability of a win  		  	   		  		 			  		 			 	 	 		 		 	
    np.random.seed(gtid())  # do this only once  		  	   		  		 			  		 			 	 	 		 		 	
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		  		 			  		 			 	 	 		 		 	
    # add your code here to implement the experiments  	
    exp_1(n_bets=1000, n_episodes=10, win_prob=0.474)
    exp_2(n_bets=1000, n_episodes=1000, win_prob=0.474)
    exp_3(n_bets=1000, n_episodes=1000, win_prob=0.474)
    plot_fig1()
    plot_fig2()
    plot_fig3()
    plot_fig4()
    plot_fig5()
    
    
def exp_1(n_bets=1000, n_episodes=10, win_prob=0.474):
    ini = [[0]+[80]*n_bets]*n_episodes
    eps_arr = np.array(ini)

    for i in range(n_episodes):
        episode_winnings = 0
        j = 1

        while episode_winnings < 80:
            won = False
            bet_amount = 1
            while not won:

                won = get_spin_result(win_prob)
                if won == True:
                    episode_winnings += bet_amount
                    eps_arr[i][j] = episode_winnings
                    j+=1

                else:
                    episode_winnings -= bet_amount
                    bet_amount = bet_amount * 2
                    eps_arr[i][j] = episode_winnings
                    j+=1

    return eps_arr

def exp_2(n_bets=1000, n_episodes=1000, win_prob=0.474):
    ini = [[0]+[80]*n_bets]*n_episodes
    eps_arr = np.array(ini)

    for i in range(n_episodes):
        episode_winnings = 0
        j = 1

        while episode_winnings < 80:
            won = False
            bet_amount = 1
            while not won:

                won = get_spin_result(win_prob)
                if won == True:
                    episode_winnings += bet_amount
                    eps_arr[i][j] = episode_winnings
                    j+=1

                else:
                    episode_winnings -= bet_amount
                    bet_amount = bet_amount * 2
                    eps_arr[i][j] = episode_winnings
                    j+=1

    return eps_arr
    	  	   		  		 			  		 			 	 	 		 		 	
def exp_3(n_bets=1000, n_episodes=1000, win_prob=0.474):
    ini = [[0]+[80]*n_bets]*n_episodes
    eps_arr = np.array(ini)

    for i in range(n_episodes):
        episode_winnings = 0
        j = 1
        while (episode_winnings < 80) and (j<1001):
            won = False
            bet_amount = 1
            
            while (not won):
                won = get_spin_result(win_prob)
                #print(j, episode_winnings, bet_amount)
                if won == True:
                    episode_winnings += bet_amount
                    eps_arr[i][j] = episode_winnings
                else:
                    episode_winnings -= bet_amount
                      
                    if episode_winnings <= -256:
                        eps_arr[i][j:] = -256
                        
                    elif episode_winnings-bet_amount*2 < -256:
                        bet_amount = 256 + episode_winnings  
                        eps_arr[i][j] = episode_winnings        
            j+=1
                        

    return eps_arr

def plot_fig1():
    lines = exp_1()
    labels  = ('Episode_1','Episode_2','Episode_3','Episode_4','Episode_5','Episode_6','Episode_7','Episode_8','Episode_9','Episode_10')

    plt.plot(lines.T)
    plt.axis([0, 300, -256, 100])
    plt.title("Figure 1")
    plt.xlabel("Spins")
    plt.ylabel("Episodes Winnings")
    plt.legend(labels)
    plt.savefig('Figure_1.png')
    plt.clf()
    
def plot_fig2():
    lines = np.mean(exp_2(),axis=0)
    stdev = np.std(exp_2(),axis=0)
    labels  = ('Mean+Stdev', 'Mean', 'Mean-Stdev')

    plt.plot(lines.T+stdev)
    plt.plot(lines.T)
    plt.plot(lines.T-stdev)

    plt.axis([0, 300, -256, 100])
    plt.title("Figure 2")
    plt.xlabel("Spins")
    plt.ylabel("Episodes Winnings")
    plt.legend(labels)
    plt.savefig('Figure_2.png')
    plt.clf()
    
def plot_fig3():
    lines = np.median(exp_2(),axis=0)
    stdev = np.std(exp_2(),axis=0)
    labels  = ('Median+Stdev', 'Median', 'Median-Stdev')

    plt.plot(lines.T+stdev)
    plt.plot(lines.T)
    plt.plot(lines.T-stdev)

    plt.axis([0, 300, -256, 100])
    plt.title("Figure 3")
    plt.xlabel("Spins")
    plt.ylabel("Episodes Winnings")
    plt.legend(labels)
    plt.savefig('Figure_3.png')
    plt.clf()
     	
def plot_fig4():
    lines = np.mean(exp_3(),axis=0)
    stdev = np.std(exp_3(),axis=0)
    labels  = ('Mean+Stdev', 'Mean', 'Mean-Stdev')

    plt.plot(lines.T+stdev)
    plt.plot(lines.T)
    plt.plot(lines.T-stdev)

    plt.axis([0, 300, -256, 100])
    plt.title("Figure 4")
    plt.xlabel("Spins")
    plt.ylabel("Episodes Winnings")
    plt.legend(labels)
    plt.savefig('Figure_4.png')
    plt.clf()
      	  	   		  		 			  		 			 	 	 		 		 	
def plot_fig5():
    lines = np.median(exp_3(),axis=0)
    stdev = np.std(exp_3(),axis=0)
    labels  = ('Median+Stdev', 'Median', 'Median-Stdev')

    plt.plot(lines.T+stdev)
    plt.plot(lines.T)
    plt.plot(lines.T-stdev)

    plt.axis([0, 300, -256, 100])
    plt.title("Figure 5")
    plt.xlabel("Spins")
    plt.ylabel("Episodes Winnings")
    plt.legend(labels)
    plt.savefig('Figure_5.png')
    plt.clf()
      		  	   		  		 			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		  		 			  		 			 	 	 		 		 	
    test_code()  		  	   		  		 			  		 			 	 	 		 		 	

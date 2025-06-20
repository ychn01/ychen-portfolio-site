import random as rnd
import matplotlib.pyplot as plt
import pandas as pd
from deck import Deck
from player import Player

# define simulation function and decision to stand as limit parameter
def sim_one(limit):
    """Runs a simulation of a Blackjack game using soft strategy with 20,000 iterations. 
Outputs the win, loss and push rate for player and house
    """
    # define variables 
    n = 20000
    player_win = 0
    house_win = 0
    push = 0

    #start loop
    for game in range(n):
        
        deck = Deck()
        player = Player()
        house = Player()

        # Deal 2 initial cards each to player and dealer
        for i in range(2):
            player.hit(deck)
            house.hit(deck) 

        # define end of game
        gameover = False
        # loop game until gameover
        while(not gameover):
            player_stand = False
            house_stand = False

            #player game play decision
            if (1 in player.hand) and (player.total >= 9) and (player.total <= 11): # check if hand has Ace
                player.total += 10  # if has ace and hand total + 10 >= 19 and <=21 then stand
                player_stand = True     
            elif not player_stand and player.total <= limit:
                player.hit(deck)
            elif not player_stand and (player.total == 18) and (1 in player.hand) and (house.hand[-1] != 2 and (house.hand[-1] != 7 and (house.hand != 8))):
                player.hit(deck)
            else:
                player_stand = True
            
            #bust so count win and exit game
            if player.total > 21:
                house_win += 1
                break

            #house dealer game play decision
            if (1 in house.hand) and (house.total >= 8) and (house.total <= 11): # check if hand has Ace
                house.total += 10  # if has ace and hand total + 10 >= 18 and <=21 then stand
                house_stand = True 
            elif not house_stand and house.total < 17:
                house.hit(deck)
            else:
                house_stand = True

            #bust so count win and exit game
            if house.total > 21:
                player_win += 1
                break
            
            #when player and house are both standing, exit game
            if (player_stand and house_stand):
                break
        
        # Results of game
        if (player.total <= 21) and (house.total <= 21):
            if (player.total < house.total):
                house_win +=1
            elif (player.total > house.total):
                player_win +=1
            else:
                push += 1

    # calculate results as percentage
    win_rate = round(player_win/n * 100, 2)
    push_rate = round(push/n * 100, 2)
    loss_rate = round(house_win/n * 100, 2)

    print("Limit Value:", limit)
    print('Win Rate:', win_rate)
    print('Push Rate:', push_rate)
    print('Loss Rate:', loss_rate)

# define simulation function and decision to stand as limit parameter
def sim_two(limit):
    """Runs a simulation of a Blackjack game using hard strategy with 20,000 iterations. 
Outputs the win, loss and push rate for player and house
    """
    # define variables
    n = 20000
    player_win = 0
    house_win = 0
    push = 0

    #start loop
    for game in range(n):
        deck = Deck()
        player = Player()
        house = Player()

        # Deal 2 initial cards each to player and dealer
        for i in range(2):
            player.hit(deck)
            house.hit(deck) 

        # define end of game
        gameover = False
        # loop game until gameover
        while(not gameover):
            player_stand = False
            house_stand = False

            #player game play decision
            if not player_stand and player.total <= limit:
                player.hit(deck)
            elif not player_stand and (player.total >= 12) and (player.total <=16) and (house.hand[-1] >= 7):
                player.hit(deck)
            else:
                player_stand = True
            #bust so count win and exit game
            if player.total > 21:
                house_win += 1
                break
            
            #house dealer game play decision
            if (1 in house.hand) and (house.total >= 8) and (house.total <= 11): # check if hand has Ace
                house.total += 10  # if has ace and hand total + 10 >= 18 and <=21 then stand
                house_stand = True 
            elif not house_stand and house.total < 17:
                house.hit(deck)
            else:
                house_stand = True

            #bust so count win and exit game
            if house.total > 21:
                player_win += 1
                break
            
            #when player and house are both standing, exit game
            if (player_stand and house_stand):
                break
        
        # Results of game
        if (player.total <= 21) and (house.total <= 21):
            if (player.total < house.total):
                house_win +=1
            elif (player.total > house.total):
                player_win +=1
            else:
                push += 1

    # calculate results as percentage
    win_rate = round(player_win/n * 100, 2)
    push_rate = round(push/n * 100, 2)
    loss_rate = round(house_win/n * 100, 2)

    print("Limit Value:", limit)
    print('Win Rate:', win_rate)
    print('Push Rate:', push_rate)
    print('Loss Rate:', loss_rate)

# display results using limit of hand value 15 to 19
for i in range(15,20):
    sim_one(i)
    sim_two(i)

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 200)

data = {'Limit Value':[15,16,17,18,19],
        'Soft Win':[42.74,43.34,42.88,40.95,36.24],
        'Hard Win':[41.05,40.57,39.76,38.01,32.72],
        'Soft Push':[9.49,9.88,8.30,7.14,5.71],
        'Hard Push':[9.74,9.98,8.58,7.01,5.21],
        'Soft Loss':[47.77,46.78,48.82,51.91,58.05],
        'Hard Loss':[49.20,49.45,51.67,54.98,62.07]}

sim_results = pd.DataFrame(data)
sim_results = sim_results.set_index('Limit Value')
print(sim_results)

fig1 = plt.plot(sim_results)
plt.legend(['Soft Win', 'Hard Win', 'Soft Push', 'Hard Push', 'Soft Loss', 'Hard Loss'],
           loc='center', bbox_to_anchor=(0.5, 0.35),ncol=3)
plt.title('Standing Limits vs Outcome rates from Soft and Hard Strategy')
plt.xlabel('Outcome Rates')
plt.ylabel('Standing Limits')
plt.show()


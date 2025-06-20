import random as rnd
rnd.seed(10)

class Deck:
    def __init__(self) -> None:
        """intializing the deck with all possible cards and shuffling
        """
        self.deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
        rnd.shuffle(self.deck)
        

    def deal(self):
        """deals one card and return the card value

        Returns:
            int: card value
        """
        #
        card = self.deck.pop(0)
        return self.get_card_value(card)
    
    def get_card_value(self, card_string):
        """determine the value of card dealt

        Args:
            card_string (string): card value string

        Returns:
            int: card value
        """
        if card_string == 'J' or card_string == 'Q' or card_string == 'K' or card_string == '10':
            return 10
        elif card_string == 'A':
            return 1
        else:
            return int(card_string)    

class Player:
    def __init__(self) -> None:
        """intialize empty hand and starting total value of 0
        """
        self.hand = []
        self.total = 0

    def hit(self, deck):
        """When player chooses hit, take a card from deck, add it to player hand and add it to player total

        Args:
            deck (string): take a card from the deck
        """
        card = deck.deal()
        self.total += card
        self.hand.append(card)


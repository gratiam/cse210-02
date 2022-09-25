from random import randint

class Card():
    """The Card is a flat rectangle with the top having no distinguishing features, and the bottom having a number between 1 and 13.
    The purpose of Card is to keep track of the number on the bottom of the newest card. 
    """
    def __init__(self):
        """Constructs a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
    def draw(self):
        """Draws a card: Picks a number between 1 and 13, assigned to self.value"""
        self.value = randint(1, 13)

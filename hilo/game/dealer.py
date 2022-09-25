from game.card import Card

class Dealer():
    """A person who deals the cards and manages the game.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        # is playing
        self.is_playing = True
        # base score of 300
        self.total_score = 300
        # the guess of high or low
        self.hilo = "foo"
        # the previous card's value (placeholder)
        self.last_card = -1
        # current card value (placeholder)
        self.new_card = -1
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        # sets up the first card of play
        first_card = Card()
        first_card.draw()
        print(f"The card is: {first_card.value}")
        self.last_card = first_card.value

        # loop rounds of play
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        print(f"Final Score: {self.total_score}")

    def get_inputs(self):
        """Ask the user if they want to play, and if so, requests a guess of high or low.

        Args:
            self (Dealer): An instance of Dealer.
        """
        
        flip_card = input("Draw card? [y/n] ")
        # exits game if player so requests
        self.is_playing = (flip_card.lower() == "y")
        if not self.is_playing:
            return
        # asks if player thinks next card is going to be higher or lower
        high_low = input("High or Low? [high/low] ")
        self.hilo = high_low.lower()
        
       
    def do_updates(self):
        """Draws the Card and updates the player's score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return 

        # set score to 0
        self.score = 0
        # create card instance
        self.new_card = Card()
        # draw a new number from 1 to 13
        self.new_card.draw()
        ## add points if guessed correctly
        # if the current card value is less than previous
        if self.new_card.value < self.last_card:
            # if correct guess
            if self.hilo == "low":
                print("Correct! Low!")
                self.score = 100
            else: print("Incorrect. Low.");self.score = -75
        # if current is higher than last card
        elif self.new_card.value > self.last_card:
            # if correct guess
            if self.hilo == "high":
                print("Correct! High!")
                self.score = 100
            else: print("Incorrect. High."); self.score = -75
        # current card is equal to last card
        else:
            # no specification on what to do in this situation
            print("No Change.")

        self.total_score += self.score

    def do_outputs(self):
        """Displays the card and the new total score. 

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return
        
        print(f"Drawn card: {self.new_card.value}")
        print(f"Your score is: {self.total_score}\n")
        self.last_card = self.new_card.value
        self.is_playing = (self.total_score > 0)
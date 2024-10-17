import random

class Card:
    
    #Represents a playing card with a suit and rank.
    suits = ["♠", "♥", "♦", "♣"]
    rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    value = int()
    if rank == "A":
        value = 1
    elif rank == "2":
        value = 2
    elif rank == "3":
        value = 3
    elif rank == "4":
        value = 4
    elif rank == "5":
        value = 5
    elif rank == "6":
        value = 6
    elif rank == "7":
        value = 7
    elif rank == "8":
        value = 8
    elif rank == "9":
        value = 9
    elif rank == "10":
        value = 10
    elif rank == "J":
        value = 11
    elif rank == "Q":
        value = 12
    elif rank == "K":
        value = 13

    def __init__(self, suit, rank):

        if not (suit in Card.suits and rank in Card.ranks):
            raise ValueError("Invalid card: " + str(suit) + " " + str(rank))

        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def card_str(self):
        if self.rank == "10":
            return f"""
            ┌─────┐
            │10   │
            │  {self.suit}  │
            │   10│
            └─────┘
            """
        else:
            return f"""
            ┌─────┐
            │{self.rank}    │
            │  {self.suit}  │
            │    {self.rank}│
            └─────┘
            """

class Deck:

    #Initializes a Deck object with a full deck of 52 cards.
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def debug_print_deck(self):
        for card in self.cards:
            print(card.card_str())
    
    def deal(self, num_cards = 1):
        pass
    
    
class Game:
    
    def game(self, card):
        
        points = int()
        while True: 
            #randomly chooses a card from the deck
            return self.debug_print_deck(card)
            Initial = card in self.cards
            print(Initial)
            #asks the user to guess if the next card will be higher or lower
            choice = input(str("Higher or Lower?"))
            if choice in ["Higher", "higher", "h","high", "High", "H"]:
                final = random.Deck
                if final > Initial:
                    points = points + 1
                    print("Correct! Your score is:", points, "points.")
                elif final == choice:
                    print("Same card.")
                elif final < Initial:
                    print("Wrong! Your score was:", points, "points.")
                    points = 0
                    print("And now it's 0. Begin again!")
                else: 
                    print("what")
                    break
            elif choice in ["Lower", "lower", "low", "l", "Low", "L"]:
                final = random.Deck
                if final < Initial:
                    points = points + 1
                    print("Correct! Your score is:", points, "points.")
                elif final == choice:
                    print("Same Card")
                elif final > Initial:
                    print("Wrong! Your score was:", points, "points.")
                    points = 0
                    print("And now it's 0. Begin again!")
                else: 
                    print("what")
                    break
            else:
                print("Learn how to spell. dummy.")
            
            
        














































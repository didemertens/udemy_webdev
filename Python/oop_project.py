#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer.

from random import shuffle

suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:

  def __init__(self):
    self.allcards = [(s,r) for s in suite for r in ranks]

  def split_deck(self):
    return (self.allcards[:26],self.allcards[26:])

  def shuffle_deck(self):
    print("Shuffling cards")
    shuffle(self.allcards)


class Hand:

  def __init__self(self,cards):
    self.cards = cards

  def __str__(self):
    return f"Contains {(len(self.cards))} cards."

    def add_card(self,added_cards):
      self.cards.extend(added_cards)

    def remove_card(self,rem_cards):
      return self.cards.pop()


class Player:



# ######################
# #### GAME PLAY #######
# ######################
# print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!

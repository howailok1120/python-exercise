import random
from art import logo
from replit import clear

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
# cards = [11]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

def draw_cards(side): #side = player_cards or pc_cards
  new_card = int(random.choice(cards))
  side.append(new_card)


def fsum(deck): #cards = player_cards or pc_cards
    return sum(deck)

def calculation_score(deck): #deck = player_cards or pc_cards
  points = fsum(deck)
  if points > 21 and 11 in deck:
      deck.remove(11)
      deck.append(1)
      points = fsum(deck)
      if points == 21:
        return points
  return points

def compare(player_cards, pc_cards):
  print(f"Your final score is {calculation_score(player_cards)} and the cards on your hand {player_cards}")
  print(f"PC final score is {calculation_score(pc_cards)} and the cards on PC hand {pc_cards}")
  if calculation_score(pc_cards) > 21 and calculation_score(player_cards) > 21:
    print("Both PC and you burst, you loss")
  elif calculation_score(pc_cards) > 21:
    print("PC burst, you win.")
  elif calculation_score(pc_cards) < calculation_score(player_cards):
    print("You win")
  elif calculation_score(pc_cards) > calculation_score(player_cards):
    print("You lose.")
  elif calculation_score(pc_cards) == calculation_score(player_cards):
    print("Draw.")

def play_game(): 
  pick_card = True
  player_cards = []
  pc_cards = []
  keep_on = True
  draw_cards(player_cards)
  draw_cards(player_cards)
  print(f"Your score is {calculation_score(player_cards)} and the cards on your hand {player_cards}")
  draw_cards(pc_cards)
  print(f"PC first card is: {pc_cards}")
  
  while keep_on:
    if calculation_score(player_cards) == 21:
      keep_on = False
      print("Player win.")
    elif calculation_score(player_cards) > 21 :
      keep_on = False
      print("Bust ! You lose")  
    elif calculation_score(player_cards) < 21:
      pick_card = input("Pree 'y' to draw card, 'n' to end game.")
      if pick_card == 'y' :
        draw_cards(player_cards)
        print(f"Your score is {calculation_score(player_cards)} and the cards on your hand {player_cards}")
      if pick_card == 'n':
        keep_on == False
        while calculation_score(pc_cards) < 17:
          draw_cards(pc_cards)
        keep_on = False
        compare(player_cards, pc_cards)

gameover = True
while gameover == True:
  gameover = input("Do you want to play blackjack? Press 'y' to play, 'n' to quit.")
  clear()
  print(logo)
  if gameover == 'y':
    gameover = True
    play_game()
  else:
    gameover = False
    quit()

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
pc_choose = random.randint(0,2)
rps = [rock, paper, scissors]
if player_choose >= 3:
    print("Wrong input, still you lose")
else:
  print("You chose:\n" + rps[player_choose])
  print("PC choose:\n" + rps[pc_choose])
  
  if player_choose == 0 and pc_choose == 2:
    print("You win")
  elif pc_choose == 0 and player_choose == 2:
    print("You lose")
  elif player_choose > pc_choose:
    print("You win")
  elif player_choose < pc_choose:
    print("You lose")
  elif player_choose == pc_choose:
    print("Draw")

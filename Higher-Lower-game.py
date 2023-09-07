from game_data import data 
from replit import clear
import random
from art import logo, vs

def get_random_question():
  return random.choice(data)

def formatted_question(question):
  name = question["name"]
  description = question["description"]
  country = question["country"] 
  # followers = question["follower_count"] 
  return f'{name}, a {description} from {country}'
   # {followers}

def compare(follower_a, follower_b):
  if follower_a > follower_b:
    return "a"
  else:
    return "b"

score = 0
game_continue = True
print(logo)
question_a = get_random_question()
while game_continue == True:
  clear()
  print(logo)
  if score >= 1:
    print(f"You're right! Current score: {score}.")
  print(f'Compare A: {formatted_question(question_a)}.')
  print(vs)
  question_b = get_random_question()
  if question_b == question_a:
    question_b = get_random_question()
    
  print(f'Against B: {formatted_question(question_b)}.\n\n')
  
  follower_a = question_a["follower_count"]
  follower_b = question_b["follower_count"]
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  answer = compare(follower_a, follower_b)
  if question_a["follower_count"] > question_b["follower_count"]:
    next_question = question_a
  else:
    next_question = question_b
  
  if guess == answer:
    score += 1
    question_a = next_question
  else:
    game_continue = False
    clear()
    print(f"Sorry, that's wrong. Final score: {score}.")

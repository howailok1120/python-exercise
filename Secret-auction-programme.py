from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program.")

bid_record = {}
bid_continue = True
winner = ""

def result():
  highest_price = 0
  for bidder in bid_record:
    price = bid_record[bidder]
    if price >= highest_price:
      highest_price = price
      winner = bidder
  print(f"Winner is {winner} with the higest auction price of $ {bid_price}")    

while bid_continue == True:
  bidder = input("What is your name? ")
  bid_price = input("What is your bidding price? $")
  bid_record[bidder] = int(bid_price)
  if input("Any further bid? Enter 'yes' to continue, 'no' to end the bid.") == "no":
    bid_continue = False
  else:
    clear()
else:
  result()

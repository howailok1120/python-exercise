#calculator
from art import logo
def add (n1, n2):
  return n1 + n2

def substract (n1, n2):
  return n1 - n2

def multiply (n1, n2):
  return n1 * n2

def divide (n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  print(logo)
  keep_on = True
  first_calculation = True
  answer = 0
  while keep_on == True:
    if first_calculation == True:
      num1 = float(input("What is your first number?\n"))
    else:
      num1 = answer
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick your operator.\n")
    num2 = float(input("What is your next number?\n"))
    answer = operations[operation_symbol](num1, num2)
    first_calculation = False
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    keep_on_answer = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calcuation.:\n")
    if keep_on_answer == "n":
      calculator()
    elif keep_on_answer == "y":
      keep_on = True

calculator()

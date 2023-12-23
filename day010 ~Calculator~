from art import logo
#calculator

#addition
def add(n1, n2):
  return n1 + n2

#subtraction
def subtract(n1, n2):
  return n1 - n2

#multiplication
def multiply(n1, n2):
  return n1 * n2

#division
def divide(n1, n2):
  return n1 / n2

operations_dictionary = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
def calculator():
  print(logo)
  
  num1 = float(input("What's your first number?\n"))
  
  for symbol in operations_dictionary:
    print(f"{symbol}")
  
  user_input = "y"
  
  while user_input != "n":
    
    operation_symbol = input("Please, pick an operation:\n")
    operation_fuction = operations_dictionary[operation_symbol]
  
    num2 = float(input("Please pick another number?\n"))
    
    answer = operation_fuction(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    num1 = answer
    print(f"Type 'y' to continue calculation with {num1} or 'n' to reset the calculator")
    user_input = input()

    if user_input != 'y':
      calculator()

#main
calculator()

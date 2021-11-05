import random

def guess_game(number):
    number = random.randint(0,100) 
    guess = None
    
    while guess != number:  
         input_number= int(input("Enter a number = "))
         if number == input_number:
          print("You won the game!!!")
         
         elif input_number > number:
          print("Your number is greater than the result.Please decrease it.")
         else:
          print("Your number is less than the result.Please increase it.")

guess_game("number")



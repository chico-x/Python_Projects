#simple python program to make a guess game (project idea from automate the boring stuff book)

#import sys module
import sys
# import random module 
import random
# import randint function from random module
from random import randint
#maximum number of guesses allowed
max_guesses = 5
# i = number of attempts
i = 0
#generate the random number to be guessed
number = randint(1,20)
#program output starts
print("I am thinking of a number between 1 and 20.")
for i in range (1,max_guesses+1):
   guess=int(input("take a guess!"))
   if guess < number:
       print("Your guess is too low.")
   elif guess > number:
       print("Your guess is too high.")
   else:
       print("Good job! you guessed my number in ", i , "Guesses!")
       sys.exit()

print("Sorry, you are out of guesses!")
print("the number you had to guess was:",number)


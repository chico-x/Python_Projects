#import modules
import sys,random,time
# define r,p,s
r="rock"
p="paper"
s="scissors"
#define win,loss and tie values
W=0
L=0
T=0
# make a dictionary for rps so that we can lookup the variable value for the corresponding r,p,s string values
elements={
"r" : r,
"p" : p,
"s" : s,
}
# make a dictionary for the game win logic e.g: rock beats scissors so we map the key= rock to value = scissors
beats={
r : s,
s : p,
p : r,
}
# computer chooses the moves from this list
moves=[r,p,s]

# print game output
print("ROCK,PAPER,SCISSORS")

# Game loop
while True:
    #print the initial values and instructions
    print(f"{W}Wins,{L}Losses,{T}Ties")
    time.sleep(0.2)
    print("Enter your move: (r)ock (p)aper (s)cissors (q)uit")
    user_move=input()
    # if user enters "q" the game quits
    if user_move == "q":
        print("Exiting game...")
        time.sleep(0.3)
        sys.exit()
   #looks up the variable value for the user input from the elements dictionary we defined earlier
    if user_move in elements:
        user_move=elements[user_move]
   # if the user input is not found in the dictionary we know that user input is not valid
   # so we go back to start of the loop after prompting the user to enter valid move
    else:
        print("Enter a valid mover!")
        time.sleep(0.3)
        continue
   #prints the user's move
    print(f"{user_move} Versus...")
    time.sleep(0.3)
   #makes a random move for the computer and prints it
    computer_move=random.choice(moves)
    print(f"{computer_move}!")
    time.sleep(0.2)
   # checks if the condition for a tie is true annd updates the Tie counter
    if computer_move==user_move:
        print("It is a Tie!")
        T+=1
        time.sleep(0.3)
   # checks whether user beat the computer's move by using the beat's dictionary 
   # if the corresponding key's value in dictionary = computer_move then it prints that the user won and updates the win counter 
    elif beats[user_move]==computer_move:
        print("You Win!")
        W+=1
        time.sleep(0.3)
   # if both the Tie and Win conditions are false then the user losses the current game and loss counter gets updated
    else:
        print("You lose!")
        L+=1
        time.sleep(0.3)


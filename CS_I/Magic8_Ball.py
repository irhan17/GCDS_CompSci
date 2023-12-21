#Name: Irhan Iftikar
#Date: February 24, 2023
#Description: Simple, magic 8 ball program that randomly selects an answer from a list of four possible answers
#Credits: No outside sources used
#Bugs: No bugs found in program.

import random       #imports module random that will later be used in program
list = ["Yes", "No", "Maybe", "Ask Again Later"]    #Creates list of possible answers
print("Welcome to the Magic 8 Ball! Print 'quit' to exit.")     #Prints "Welcome to 8-Ball"
while True:         #Loop that runs continuously until stopped by user
    answer = input("What is your question? ")       #Question that user inputs 
    if answer == "quit":        #If user answers with 'quit'...
            break       #The program stops
    else:       #Otherwise the user asks a different question...
        print(random.choice(list))      #Magic 8-Ball answers with a random choice from the list
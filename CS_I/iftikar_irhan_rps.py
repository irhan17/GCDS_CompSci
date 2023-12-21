#Name: Irhan Iftikar
#Date: April 5, 2023
#Description: Rock, Paper, Scissor Program that plays a game between the user and computer
#Challenges: Game determines who the winner is after each round, game keeps track of the score, user errors are addressed

import sys      #Imports sys module that will be used to stop the program
import random       #imports random module that will randomize computer's answer
weapons = ["rock", "paper", "scissor"]     #List of possible answers for the computer
user_score = 0              #Initializes variable for user's score as 0
computer_score = 0          #Initializes variable for computer's score as 0
print("Welcome to the Rock, Paper, Scissor Game!")      #welcomes user to the program
while True:             #while loop that exists until user quits the program
    user_answer = input("Enter 'rock', 'paper', or 'scissor': ")        #prompts the user for choice of rock, paper, scissor
    computer_answer = random.choice(weapons)           #Randomly generates computer answer from the list of weapons
    
    if user_answer not in weapons:      #If the user's choice isn't in the list of possible answers...
        print("Option is invalid, please try again.")   #Prints option is invalid, restarts program
    elif user_answer == computer_answer:       #If the user's choice is the same as the computer's choice...
        print("Tie game!")                          #Prints tie game
    elif user_answer == "rock":               #If user enters rock...
        if computer_answer == "paper":         #If computer answer is paper...
            print("Computer wins!")             #prints computer wins
            computer_score += 1                 #Adds one to the computer's score
        elif computer_answer == "scissor":    #Otherwise computer answer is scissor...
            print("You win!")                   #Prints user wins
            user_score += 1                     #Adds one to the user's score
    elif user_answer == "paper":            #If user enters paper...
        if computer_answer == "scissor":       #If computer answer is scissor...
            print("Computer wins!")               #prints computer wins
            computer_score += 1                   #Adds one to the computer's score
        elif computer_answer == "rock":        #If computer answer is rock...
            print("You win!")                   #Prints user wins
            user_score += 1                     #Adds one to the user's score
    elif user_answer == "scissor":          #If user answers with scissor...
        if computer_answer == "rock":           #If computer answer was rock...
            print("Computer wins!")                 #prints computer wins
            computer_score += 1                     #Adds one to the computer's score
        elif computer_answer == "paper":        #Otherwise computer answer was paper...
            print("You win!")                       #Prints user wins
            user_score += 1                 #Adds one to the user's score 

    print("Your Answer: ", user_answer, " Computer Answer: ", computer_answer)  #prints answer of the user and computer
    print("User Score: ", user_score, ".", "Computer Score: ", computer_score)  #prints score of the game

    while True:     #Creates another while loop that asks if user wants to play again
        play_again = input("Would you like to play again? Enter 'yes' or 'no': ")   #Asks user if they would like to play again
        if play_again == "yes":            #If user answers yes...
            print("Continuing program!")        #Program continues
            break                            #Breaks nested while loop, continues program
        elif play_again == "no":        #If user answers no...
            sys.exit()              #Exits the program running in the system
        else:                       #Otherwise user answers a different answer...
            print("Response not understood. Try again.")    #Nested while loop continues and asks user if they want to continue again
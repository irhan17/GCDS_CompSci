#Name: Irhan Iftikar
#Due Date: April 28, 2023
#Description: Food-o-Matic program that randomly generates menu items from a combination of three different lists
#Challenges: Adds a cost calculation, allows multiple items from first and last column of lists, ensures no repeats of menu orders from first and last columns, accounts for user error when entering inputs
#Bugs: No bugs found in code
#Sources: No outside sources used

import sys      #Import sys module
import random   #Import random module to randomize choice of menu items
descriptions = ["local", "roasted", "grilled", "garlic mashed", "oven dried ", "spiced", "stewed", "assorted", "iced", "sliced", "braised", "free-range", "baby" , "teriyaki glazed", "steamed"]  #Creates list possible menu choices
main = ["cauliflower", "tilapia fillet", "pork loin", "green beans", "basmati rice", "rainbow carrots", "fingerling potatoes", "three color squash", "potatoes", "eggplant", "drumstick", "short rib", "duck breast", "eye round of beef", "baguette"]    #Creates list of possible main courses
toppings = ["with fennel", "gratin", "bengali style", "with peas", "pizza", "with balsamico", "with garlic and olive oil", "with pigeon peas", "with minted yogurt", "soup", "chutney", "salad", "with tropical fruit salsa", "over sticky rice", "au jus"]      #Creates list of possible side courses
cost_descriptions = [3, 3, 3, 2, 3, 3, 4, 3, 2, 0, 2, 3, 3, 4, 5]           #Creates a list with costs of the descriptions parallel to the items in the descriptions list
cost_main = [10, 15, 10, 8, 10, 8, 10, 10, 10, 12, 12, 15, 15, 15, 10]      #Creates a list with costs of food parallel to the menu items in the main list
cost_toppings = [2, 2, 4, 3, 7, 4, 3, 3, 2, 4, 3, 5, 5, 5, 4]               #Creates a list with costs of the toppings parallel to the toppings list

while True:     #Creates while loop that runs continuously
    print("Welcome to the Food-o-Matic program. Here, a randomly generated menu item will be created. ")    #Welcomes user to program
    number = input("Enter a number of menu items you want: ")      #Asks user for how many menu items they want
    if number.isnumeric() == True:  #Checks if the user entry is a valid number
        number = int(number)    #Saves user entry as an integer value
        total_cost = 0          #Initializes total cost of meal to $0

        for x in range (0, number):     #For loop that runs for how many times the user entered their meal choice
            choice_1 = random.choice(descriptions)    #Takes a random choice from the first list
            choice_1_2 = random.choice(descriptions)  #Takes a second choice from the first list - part of the bonus/challenge options
            choice_2 = random.choice(main)    #Randomly takes a choice from the second list
            choice_3 = random.choice(toppings)    #Takes a random choice from third list
            choice_3_2 = random.choice(toppings)    #Takes a second random choice from third list
            
            while True:                         #Creates a nested while loop
                if choice_3 == choice_3_2:          #If the second choice from list 3 was equal to the first...
                    choice_3_2 = random.choice(toppings)     #Randomly takes a new choice from list 3
                    break                               #Breaks nested while loop, continues program
                else:                               #If the two choices from list 3 are different...
                    break                           #Breaks nested while loop, continues program
            
            while True:                         #Creates a second nested while loop
                if choice_1_2 == choice_1:          #If the second choice from list 1 was equal to the first...
                    choice_1_2 == random.choice(descriptions)     #Randomly selects a new choice from list 1 for the second option
                    break                                   #Breaks nested while loop, continues program
                else:                               #Otherwise the choices were different...
                    break                       #Breaks nested while loop, continues program
            
            index_1 = descriptions.index(choice_1)      #Takes the index choice from the first choice from descriptions list
            index_1_2 = descriptions.index(choice_1_2)  #Takes the index choice from the second choice from descriptions list
            index_2 = main.index(choice_2)      #Stores index of the choice from main list
            index_3 = toppings.index(choice_3)      #Takes the index choice from the first choice from toppings list
            index_3_2 = toppings.index(choice_3)        #Takes the index choice from the second choice from toppings list
            cost = cost_descriptions[index_1] + cost_descriptions[index_2] + cost_main[index_2] + cost_toppings[index_3] + cost_toppings[index_3_2]     #Finds cost for the total choices from the three lists
            print("Menu selection: ", choice_1, choice_1_2, choice_2, choice_3, choice_3_2, ". Cost: $", cost)  #Prints out menu selection and cost for that item
            total_cost = cost + total_cost      #Updates total cost variable from the previous menu choice generated
    else:       #If user entry isn't a valid number
        print("Input isn't a number, try again. ")  #Tells user it isn't a valid number
        continue            #Restarts while loop
    print("Total cost of all menu items: $", total_cost)    #Prints total cost of the menu items ordered

    while True:     #Creates another while loop that asks if user wants to order again
        play_again = input("Would you like to order again? Enter 'yes' or 'no': ")   #Asks user if they would like to order again
        
        if play_again == "yes":            #If user answers yes...
            print("Continue new order!")        #Program continues
            break                            #Breaks nested while loop, continues program
        elif play_again == "no":            #If user answers no...
            print("Thank you for ordering.")       #Thanks user for ordering
            sys.exit()              #Exits the program running in the system
        else:                       #Otherwise user answers a different answer...
            print("Response not understood. Try again.")    #Nested while loop continues and asks user if they want to continue again
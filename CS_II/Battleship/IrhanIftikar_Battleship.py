#Name: Irhan Iftikar
#Date: April 2024
#Description: Simplified game of Battleship where the user and computer play a game of Battleship
#Criteria: Meets all details outlined on specification sheet
#Bonuses: Turns board dots into emojis, allows user to choose board size and number of ships, plays audio sounds for 'hit' and 'miss', accounts for user input error
#Bugs: No notable bugs found in program
#Sources: Various Internet Sources for Syntax (w3schools, Stack Overflow, GeeksForGeeks, etc.) and playsound installation

#Imports modules used in program and finds current directory path
import random
from playsound import playsound
from pathlib import Path
current_dir = Path(__file__).parent

def create_board(board_size):
    #Description: Function that creates the initial Battleship board at start of program execution
    #parameters - board size entered by user
    #returns - initial battleship board
    board = [["❔"] * board_size for column in range(board_size)]
    return board

def print_board(board):
    #Description: Function that prints current board at time of function being called
    #parameters - Battleship board
    #returns - null
    for row in board:
        print(" ".join(row))

def place_ships(number_of_ships, board):
    #Description: Function that places and saves coordinates of placed ships on the board
    #parameters - Number of ships on board entered by user, Battleship board
    #returns - list of the coordinates of the ships on the Battleship board
    coordinates_list = []
    count = 0
    while count < number_of_ships:
        temp_list = []
        ship_row = random.randint(0, len(board) - 1) #Randomly generates row and column indexes where ship is placed
        ship_column = random.randint(0, len(board[0]) - 1)
        temp_list.append(ship_row)
        temp_list.append(ship_column)
        if temp_list not in coordinates_list:
            coordinates_list.append(temp_list)
            count += 1
    return coordinates_list

def user_input():
    #Description: Function that asks the user for their initial inputs on board size and number of ships
    #parameters - null
    #returns - board size, number of ships
    while True:
        board_size = int(input("Enter a number for board size: "))
        number_of_ships = int(input("Enter number of ships for the board: "))
        if board_size < 1 or number_of_ships < 1 or number_of_ships > (board_size * board_size):
            print("Invalid input, try again.")
        else:
            break
    return board_size, number_of_ships

def user_move(current_dir, user_number_of_hits, user_board, user_coordinates_list, turn, board_size):
    #Description: Function that asks the user for their guess and processes the result of their guess
    #parameters - current directory, number of ships already hit, user's board, coordinates of user's ships, turn number, size of board
    #returns - turns left, number of ships sank
    guess_list = []
    turn -= 1
    print(f"{turn} turns left!")
    while True:
        row_guess = int(input(f"Guess row value (1 to {board_size}): "))
        column_guess = int(input(f"Guess column value (1 to {board_size}): "))
        if row_guess < 1 or row_guess > board_size or column_guess < 1 or column_guess > board_size:
            print("Invalid coordinates, try again.")
        else:
            row_guess -= 1
            column_guess -= 1
            break
    guess_list.append(row_guess)
    guess_list.append(column_guess)

    #If/elif/else functions below see if user correctly hit the ship on the board and prints outputs and sounds according to outcome
    if user_board[row_guess][column_guess] == "✔️ ":
        playsound(current_dir / "hit.mp3")
        print("You already hit a battleship in this location!")
    elif guess_list in user_coordinates_list:
        playsound(current_dir / "hit.mp3")
        print("You hit the battleship!")
        user_board[row_guess][column_guess] = "✔️ "
        user_number_of_hits += 1
    else:
        playsound(current_dir / "miss.mp3")
        print("You missed the battleship.")
        user_board[row_guess][column_guess] = "❌"
    #Prints the most updated board and returns variables
    print_board(user_board)
    return turn, user_number_of_hits

def computer_move(computer_number_of_hits, computer_board, computer_coordinates_list, board_size):
    #Description: Function that processes the computer's move and result of their randomly generated guess
    #parameters - number of ships already hit, computer's board, coordinates of computer's ships, size of board
    #returns - number of ships sank by computer
    guess_list = []
    row_guess = random.randint(0, board_size - 1)
    column_guess = random.randint(0, board_size - 1)
    guess_list.append(row_guess)
    guess_list.append(column_guess)
    #If/elif/else functions below see if computer correctly hit the ship on the board and prints outputs according to computer's guess
    if computer_board[row_guess][column_guess] == "✔️ ":
        print("Computer guessed a location they already hit!")
    elif guess_list in computer_coordinates_list:
        print("Computer hit your battleship!")
        computer_board[row_guess][column_guess] = "✔️ "
        computer_number_of_hits += 1
    else:
        print("Computer's guess missed your battleship!")
        computer_board[row_guess][column_guess] = "❌"
    return computer_number_of_hits

def main(current_dir, board_size, number_of_ships):
    #Description: Main function that executes program and calls on other functions
    #parameters - current directory, board size, number of ships
    #returns - null
    user_board = create_board(board_size) #Calls functions and initializes variables
    user_coordinates_list = place_ships(number_of_ships, user_board)
    computer_board = create_board(board_size)
    computer_coordinates_list = place_ships(number_of_ships, user_board)
    game_outcome = False
    user_number_of_hits = 0
    computer_number_of_hits = 0
    turn = 11
    #For loop that runs 10 times, as user has 10 turns to play the game (as described by spec sheet)
    for i in range(10):
        turn, user_number_of_hits = user_move(current_dir, user_number_of_hits, user_board, user_coordinates_list, turn, board_size)
        computer_number_of_hits = computer_move(computer_number_of_hits, computer_board, computer_coordinates_list, board_size)
        #Checks if either user or computer has won the game, and if so, loop breaks
        if user_number_of_hits == number_of_ships and computer_number_of_hits == number_of_ships:
            print("You tied the game of Battleship with the computer!")
            game_outcome = True
            break
        elif user_number_of_hits == number_of_ships and computer_number_of_hits != number_of_ships:
            print("You won the game of Battleship!")
            game_outcome = True
            break
        elif computer_number_of_hits == number_of_ships and user_number_of_hits != number_of_ships:
            print("Computer won the game of Battleship!")
            game_outcome = True
            break
        else:
            game_outcome = False
    if game_outcome == False:
        print("Game of battleship ends in a tie!")

while True:
    try: #Executes program
        print("Welcome to Battleship!")
        board_size, number_of_ships = user_input()
        main(current_dir, board_size, number_of_ships)
        break
    except ValueError:  #If ValueError or IndexError, program restarts
        print("Input error, restarting program.\n")
    except IndexError:
        print("Input error, restarting program.\n")
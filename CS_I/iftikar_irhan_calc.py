#Name: Irhan Iftikar
#Due Date: May 19, 2023
#Description: Basic calculator program that calculates various operations from two numbers that a user inputs
#Challenges: Creates an exponent function, creates a max function, adds to main function by calling all functions, creates a mod function, addresses for user integer input errors
#Bugs: No bugs found in code
#Sources: w3schools for syntax help

def check_int():   #Creates function that checks if inputs are valid integers
    while True: #While loop that runs continuously
        num = input("Enter a number: ")  #Asks user to enter a number
        try:    #Tries to see if the input is an integer
            return int(num) #If it is an integer, returns the input
        except ValueError:       #If input is not an integer...
            print("You didn't enter valid integers, try again.")   #Tells user they didn't enter a valid integer

def add(a,b):   #Function that adds the parameters
    return a + b    #Returns the sum of the integers

def subtract(a,b):  #Function that subtracts the parameters
    return a - b    #Returns the subtraction of the integers

def multiply():  #Function that multiplies the parameters
    a = check_int()    #Calls on check_int function and saves input as a
    b = check_int()  #Calls on check_int function and saves input as b
    return a * b    #Returns the product of the integers

def divide():   #Function that divides the parameters
    a = check_int() #Calls on check_int function and saves input as a
    b = check_int() #Calls on check_int function and saves input as b
    return a / b    #Returns the quotient of the integers

def exponent(a, b): #Function that finds exponent of the parameters
    return a ** b   #Returns the exponential value of the integers

def max(numbers):   #Function that finds maximum value of the parameters
    largest = numbers[0]    #Assumes largest value is the first in the list
    for i in range(1, len(numbers)):    #For loop that runs from 1 to the length of list
        if numbers[i] > largest:    #If there is a larger value in the list than the first
            largest = numbers[i]    #Saves largest value as the corresponding index value
    return largest  #Returns the largest value in list

def mod(a, b):      #Function that finds modulus of the parameters
    return a % b    #Returns the modulus value of the integers

def sum_list(numbers):  #Function that finds sum of the parameters from a list
    total = 0   #Sets total sum to 0
    for n in numbers:    #For loop that runs for length of the list
        total += n    #Adds the sum of each individual integer to the total sum
    return total    #Returns total sum from the list

def main(number1, number2): #Main function that calls all the other functions
    numbers = [number1, number2]    #Creates a list with the inputted numbers
    print("Sum: ", add(number1, number2))   #Calls the add function and prints the output
    print("Subtraction: ", subtract(number1, number2)) #Calls the subtract function and prints the output
    print("Exponent: ", exponent(number1, number2)) #Calls the exponent function and prints the output
    print("Largest Number Present: ", max(numbers)) #Calls the max function and prints the output
    print("Remainder when divided: ", mod(number1, number2)) #Calls the mod function and prints the output
    print("Sum of numbers from list: ", sum_list(numbers)) #Calls the sum_list function and prints the output
    print("Product: ", multiply())  #Calls the multiply function and prints the output
    print("Quotient: ", divide()) #Calls the divide function and prints the output

a = check_int()  #Calls on check_int function and saves the returned values as a
b = check_int()  #Calls on check_int function and saves the returned values as b
main(a, b)  #Calls the main function with values a and b from the check_int function
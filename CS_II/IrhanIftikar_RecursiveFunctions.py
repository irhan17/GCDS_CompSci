#Name: Irhan Iftikar
#Date: May 2024
#Description: Recursive functions for various mathematical identities. All functions run recursively.
#Criteria: Satisfies all identities listed on the specification sheet
#Challenges: Includes Euclid's GCD algorithm, compound interest, square root using bisection method, and combinations. The program also accounts for user input errors.
#Bugs: No notable bugs found in program
#Sources: Various Internet Sources (w3schools, Stack Overflow, GeeksForGeeks, etc.)

#imports sys module used if user wants to quit the program
import sys

def factorial(number):
    #Description: Function that recursively finds the factorial of a number
    #parameters - number
    #returns - factorial of the number
    if number == 1:
        return 1
    elif number > 1:
        return number*factorial(number - 1)
    
def summation(number):
    #Description: Function that recursively finds the summation of a number to 0
    #parameters - number
    #returns - summation of the number to 0
    if number == 1:
        return 1
    elif number > 1:
        return number + summation(number-1)
    
def exponential(number, exponent):
    #Description: Function that recursively finds exponential value of a number
    #parameters - number, exponent
    #returns - number^exponent
    if exponent == 0:
        return 1
    elif number == 0:
        return 0
    elif number > 0:
        return number * exponential(number, exponent - 1)

def fibonacci(number):
    #Description: Function that recursively finds the nth value of the Fibonacci Sequence
    #parameters - number
    #returns - nth value of Fibonacci Sequence
    if number == 1:
        return 0
    elif number == 2:
        return 1
    elif number > 2: 
        return (fibonacci(number - 1) + fibonacci(number - 2))
    
def sum_digits(number):
    #Description: Function that recursively finds the sum of digits in a number
    #parameters - number
    #returns - sum of digits in the number
    if number == 0:
        return 0
    elif number > 1:
        return (number % 10 + sum_digits(int(number / 10)))

def product_digits(number):
    #Description: Function that recursively finds the product of digits in a number
    #parameters - number
    #returns - product of digits in the number
    if 0 <= number < 10:
        return number
    else:
        last_digit = number % 10
        rest_of_number = number // 10
        return last_digit * product_digits(rest_of_number)

def product_numbers(number1, number2):
    #Description: Function that recursively finds the product of two numbers
    #parameters - number1, number2
    #returns - product of two numbers
    if number2 == 0:
        return 0
    else:
        return number1 + product_numbers(number1, number2 - 1)

def sum_in_range(number1, number2):
    #Description: Function that recursively finds the sum in range of two numbers
    #parameters - number1, number2
    #returns - sum of values between number1 and number2
    if number1 > number2:
        return("Improper interval range entered.")
    elif number1 < number2:
        return number1 + sum_in_range(number1 + 1, number2)
    else:
        return 0
    
def reverse_digits(number):
    #Description: Function that recursively reverses the digit of a number
    #parameters - number
    #returns - reversed digits of a number
    if 0 <= number < 10:
        return number
    else:
        last_digit = number % 10
        rest_of_number = number // 10
        reversed_rest_of_number = reverse_digits(rest_of_number) 
        return str(last_digit) + str(reversed_rest_of_number)

def euclid_GCD(number1, number2):
    #Description: Function that recursively finds the Euclid GCD of two numbers
    #parameters - number1, number2
    #returns - Euclid GCD of two numbers
    if number2 <= number1 & (number1 % number2 == 0):
        return number2
    else:
        return euclid_GCD(number2, (number1 % number2))

def compound_interest(principal, rate, time):
    #Description: Function that recursively finds compound interest
    #parameters - principal, rate, time
    #returns - compound interest value
    if time == 0:
        return principal
    elif time > 0:
        return ((1 + rate) * compound_interest(principal, rate, time - 1))

def square_root_Newton(number, lower_bound, upper_bound):
    #Description: Function that recursively finds the square root using bisectional/Newton's method
    #parameters - number, lower bound, upper bound
    #returns - square root using bisectional/Newton's method
    if (abs(upper_bound^2 - number) < lower_bound):
        return upper_bound
    else:
        return square_root_Newton((number, lower_bound, (upper_bound+number)/upper_bound)/2)
    
def combination(number1, number2):
    #Description: Function that recursively calculates combination
    #parameters - number1, number2
    #returns - number1 Combination number2 (n1 C n2)
    if number1 < number2:
        return("Invalid input, try again.")
    elif number1 == number2 or number2 == 0:
        return 1
    else:
        return combination(number1 - 1, number2 - 1) + combination(number1 - 1, number2)

def menu():
    #Description: Function that outputs the main screen menu options to the user
    #parameters - void
    #returns - void
    print('''
    Pick a mathematical identity to run:
    1 - Factorial of a number
    2 - Summation from a number to 0
    3 - Exponential function (n^k)
    4 - Nth value of Fibonacci Sequence
    5 - Sum of a number's digits
    6 - Product of a number's digits
    7 - Product of two whole numbers
    8 - Sum of numbers in range (n,k)
    9 - Reverse the digits of a number
    10 - Euclid's GCD of two numbers
    11 - Compound Interest
    12 - Square Root Bisection Method
    13 - Combination of nCk
    14 - Quit''') 

def main():
    #Description: Main function that executes the other functions
    #parameters - void
    #returns - void
    choice = int(input("Select an option from the menu (numbers 1-14): "))
    if choice not in range(1, 15): #Ensures user choice was between 1-14, otherwise restarts the program
        print("Input error, try again.")
        main()
    else:
        number = int(input("Enter a positive integer: "))
        if choice == 1:
            print(factorial(number))
        elif choice == 2:
            print(summation(number))
        elif choice == 3:
            exponent = int(input("Enter a positive exponent: "))
            print(exponential(number, exponent))
        elif choice == 4:
            print(fibonacci(number))
        elif choice == 5:
            print(sum_digits(number))
        elif choice == 6:
            print(product_digits(number))
        elif choice == 7:
            number2 = int(input("Enter a second positive integer: "))
            print(product_numbers(number, number2))
        elif choice == 8:
            number2 = int(input("Enter a second positive integer: "))
            print(sum_in_range(number, number2 + 1))
        elif choice == 9:
            print(reverse_digits(number))
        elif choice == 10:
            number2 = int(input("Enter a second positive integer: "))
            print(euclid_GCD(number, number2))
        elif choice == 11:
            principal = int(input("Enter principal: "))
            rate = int(input("Enter a rate (%): "))
            time = int(input("Enter a positive time duration: "))
            print(compound_interest(principal, rate, time))
        elif choice == 12:
            lower_bound = int(input("Enter a value for lower bound: "))
            upper_bound = int(input("Enter a value for upper bound: "))
            print(square_root_Newton(number, lower_bound, upper_bound))
        elif choice == 13:
            number2 = int(input("Enter another positive integer: "))
            print(combination(number, number2))
        elif choice == 14:
            sys.exit(0)

#Calls menu and executes program until the user quits. Program accounts for user input errors.
menu() 
while True:
    try:
        main()
    except TypeError:
        print("Input error, try again.")
    except ValueError:
        print("Input error, try again.")
    except RecursionError:
        print("Input error, try again.")
    except ZeroDivisionError:
        print("Input error, try again.")
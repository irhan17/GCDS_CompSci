#Name: Irhan Iftikar
#Date: February 2024
#Description: String manipulation program that allows user to make menu choices from their entered name without using global string helper classes
#Criteria: Meets spec criteria #1-15 (inclusive)
#Bonuses: Returns fullname as a sorted array of characters, contains a menu, returns boolean if name contains a title/distinction
#Bugs: No notable bugs found in program besides program only allows for a name with three parts (first, middle, last) to be entered
#Sources: Various Internet Sources for String Syntax (w3schools, Stack Overflow, GeeksForGeeks, etc.)

#Imports modules used in program
import random
import sys

def reverse(name):
    #Description: Function that reverses the entered name
    #parameters - name entered by user
    #returns - reversed name
    return name[::-1]

def vowels(name):
    #Description: Function that determines number of vowels in the name
    #parameters - name entered by user
    #returns - counted number of vowels in the name
    vowel_count = 0
    for i in name:
        if i in "aeiouyAEIOUY":
            vowel_count += 1
    return vowel_count

def consonants(name):
    #Description: Function that determines number of consonants in the name
    #parameters - name entered by user
    #returns - counted number of consonants in the name
    consonant_count = 0
    for i in name:
        if i in "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ":
            consonant_count += 1
    return consonant_count

def first_name(name):
    #Description: Function that returns first name
    #parameters - name entered by user
    #returns - first name
    index = 0
    while index < len(name):
        letter = name[index]
        if letter == " ":
            return(name[:index])
        else:
            index = index + 1

def last_name(name):
    #Description: Function that returns last name
    #parameters - name entered by user
    #returns - last name
    index = len(name) - 1
    while index <= len(name):
        letter = name[index]
        if letter == " ":
            return(name[index + 1:])
        else:
            index = index - 1

def middle_name(name):
    #Description: Function that returns middle name
    #parameters - name entered by user
    #returns - middle name
    first_index = 0
    while first_index < len(name):
        letter = name[first_index]
        if letter == " ":
            break
        else:
            first_index = first_index + 1

    last_index = len(name) - 1
    while last_index <= len(name):
        letter = name[last_index]
        if letter == " ":
            break
        else:
            last_index = last_index - 1

    return(name[first_index + 1:last_index]) #Returns letters of middle name starting with last index of first name and ends with first index of last name

def hyphen(name):
    #Description: Function that returns boolean if last name contains a hyphen
    #parameters - name entered by user
    #returns - Boolean (True or False)
    boolean = False
    index = len(name) - 1
    while index <= len(name):
        letter = name[index]
        if letter == " ":
            last_name = name[index + 1:] #Finds last name
            break
        else:
            index = index - 1

    for i in last_name: #Iterates through last name
        if i in "-":
            boolean = True
            return(boolean)
        else:
            boolean = False
    return(boolean)

def lowercase(name):
    #Description: Function that converts name to lowercase
    #parameters - name entered by user
    #returns - lowercase name
    lowercase_name = []
    index = -1
    for i in name:
        index += 1
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num = ord(i)
            num += 32 #Changes uppercase to lowercase using ASCII Table values
            letter = str(chr(num))
            lowercase_name.append(letter)
        else:
            lowercase_name.append(i)
    return(str(("".join(lowercase_name))))

def uppercase(name):
    #Description: Function that converts name to uppercase
    #parameters - name entered by user
    #returns - uppercase name
    uppercase_name = []
    index = -1
    for i in name:
        index += 1
        if i in "abcdefghijklmnopqrstuvwxyz":
            num = ord(i)
            num -= 32 #Changes lowercase to uppercase using ASCII Table values
            letter = str(chr(num))
            uppercase_name.append(letter)
        else:
            uppercase_name.append(i)
    return(str(("".join(uppercase_name))))

def modify(name):
    #Description: Function that modifies array to create a random name
    #parameters - name entered by user
    #returns - modified name
    letters = []
    removed_letters = []
    new_name = []
    length = 0
    for i in name: #Adds all letters in entered name to a list
        letters.append(i)
        removed_letters.append(i)
    while length < len(letters):
        choice = random.choice(removed_letters) #Randomly takes a letter from the list and adds it to new_name list
        new_name.append(choice)
        length += 1
        removed_letters.remove(choice)
    return(str(("".join(new_name))))

def palindrome(name):
    #Description: Function that returns boolean if first name is a palindrom
    #parameters - name entered by user
    #returns - Boolean
    is_palindrome = False
    first = first_name(name)    
    lowercase_first = lowercase(first)  #Finds first name and lowercases it for standardization
    
    front_index = 0
    back_index = 1
    while front_index < len(lowercase_first):
        if lowercase_first[front_index] == lowercase_first[-back_index]: #Checks to see if name is palindrome by comparing front and back letters
            is_palindrome = True
            front_index +=1
            back_index += 1
        else:
            is_palindrome = False
            break
    return is_palindrome

def sort_characters(name):
    #Description: Function that returns full name as a sorted array
    #parameters - name entered by user
    #returns - sorted array of characters in the name
    ascii_characters = []
    sorted_characters = []
    for letter in name:
        num = ord(letter)
        ascii_characters.append(num) #Converts letters to ASCII values
    
    index = 33
    while index < 127:
        if index in ascii_characters: #Cycles through ASCII values going upward in value
            for count in range (0, len(ascii_characters)):
                if ascii_characters[count] == index:
                    sorted_characters.append(str(chr(index))) #Converts ASCII value back to letter and adds to sorted_characters list
            index += 1
        else:
            index += 1 
    return(str(("".join(sorted_characters))))

def initials(name):
    #Description: Function that finds initials of the name
    #parameters - name entered by user
    #returns - Initials of name
    first = first_name(name)
    middle = middle_name(name)
    last = last_name(name)
    initials = first[0] + middle[0] + last[0]
    return initials

def title(name):
    #Description: Function that returns a boolean if name contains a title/distinction
    #parameters - name entered by user
    #returns - Boolean
    boolean = False
    if "Dr." in name or "Sir" in name or "Esq" in name or "Ph.d" in name:
        boolean = True
    else:
        boolean = False
    return boolean

def quit():
    #Description: Function that terminates the program
    #parameters - void
    #returns - void
    sys.exit(0)

def menu():
    #Description: Function that outputs the main screen menu options to the user
    #parameters - void
    #returns - void
    print('''
    String Manipulation Naming Menu:
    -------------------------------------------------------------
    1 - Reverse and display
    2 - Determine number of vowels
    3 - Determine number of consonants
    4 - Return first name
    5 - Return last name
    6 - Return middle name
    7 - Return boolean if last name contains hyphen
    8 - Function to convert to lowercase
    9 - Function to convert to uppercase
    10 - Modify array to create a random name
    11 - Return boolean if first name is a palindrome
    12 - Return fullname as a sorted array of characters
    13 - Make initials from name
    14 - Return boolean if name contains a title/distinction
    15 - Quit''')  

def main(name):
    #Description: Main function that executes the other functions
    #parameters - name entered by user
    #returns - void
    choice = input("Select an option from the menu (numbers 1-15): ")
    if choice == "1":
        print(reverse(name))
    elif choice == "2":
        print(vowels(name))
    elif choice == "3":
        print(consonants(name))
    elif choice == "4":
        print(first_name(name))
    elif choice == "5":
        print(last_name(name))
    elif choice == "6":
        print(middle_name(name))
    elif choice == "7":
        print(hyphen(name))
    elif choice == "8":
        print(lowercase(name))
    elif choice == "9":
        print(uppercase(name))
    elif choice == "10":
        print(modify(name))
    elif choice == "11":
        print(palindrome(name))
    elif choice == "12":
        print(sort_characters(name))
    elif choice == "13":
        print(initials(name))
    elif choice == "14":
        print(title(name))
    elif choice == "15":
        quit()
    else:
        print("Menu choice not valid, try again.")

def get_name():
    #Description: Function that gets the name to be used in the program from the user
    #parameters - void
    #returns - name entered by user
    while True:
        space_count = 0
        name = input("Enter a full name (Three parts, single space between them, no spaces in front of first name or after last name): ")  #Asks user to enter a name that can be split into three parts
        for i in name:
            if i in " ":
                space_count += 1

        if space_count == 2: #If there are a total of two spaces in the name entered, program continues
            return name
        else: #Else program reprompts user to enter a valid name
            print("Name entered doesn't contain three parts with exactly one space between them, try again.")

name = get_name()  #Calls function to get name from user
menu()  #Calls menu choices
while True:        
    try:
        main(name)      #Calls main function to execute program      
    except IndexError or ValueError:     
        pass    #Disregards if error occurs in the program
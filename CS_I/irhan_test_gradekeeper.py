#Name: Irhan Iftikar
#Date: April 28, 2023
#Description: Grade keeper program that saves grades, prints them out, and can find grade/partner of a specific student
#Challenges: Can add a student pair and their grade, change grade of specific student, addresses multiple user errors
#Bugs: No bugs found in code
#Sources: No outside sources used except my own code previously written

students1 = ["Kat", "Fred", "Sam", "Bob", "Lucy"]  #Creates list of the first students
students2 = ["Lex", "Hal", "Ann", "Greg", "Laura"]     #Creates list of corresponding student pair
grade = [95, 85, 93, 90, 88]    #List of grades for the students

import sys  #imports system module
import random #imports random module

while True:    #While loop that runs continuously 
    print('''Welcome to the Grade System Keeper. Here are your choices: 
            1: Print out every student pair and their grades
            2: Find the partner and grade for a specific student
            3: Add a student pair and their grade
            4: Change the grade of a specific student
    ''')        #Enters user to the program and gives them their choices
    choice = input("Enter your choice: ")   #Saves user input in a variable

    if choice == "1":   #If the user enters 1 as their choice...
        number = int(len(students1))    #Takes the length of the list
        for i in range (0, number):     #For loop that runs for length of the list
            print("Student pair:", students1[i], "and", students2[i], ". Grade: ", grade[i])  #prints student pair and corresponsing grade

    elif choice == "2": #If the user enters 2 as their choice...
        specific_student = input("Enter the name of the student you wish to find: ")    #Asks user for the student they wish to find
        if specific_student in students1:   #If the student is found in the first list...
            position = int(students1.index(specific_student))   #Takes index position of the student
            print("Pair of students: ", students1[position], " and ", students2[position], ". Grade: ", grade[position])    #Prints corresponding pair and grade of the student
        elif specific_student in students2: #If the student is found in the second list...
            position = int(students2.index(specific_student))   #Takes index position of the student
            print("Pair of students: ", students1[position], " and ", students2[position], ". Grade: ", grade[position]) #Prints corresponding pair and grade of the student
        else:   #Otherwise student not found...
            print("Student not found in directory.")    #Prints student not found

    elif choice == "3": #If user enters 3 as their choice...
        add_student1 = input("Enter the name of the student you want to add: ") #Asks user for the first student they want to add
        students1.append(add_student1)  #Adds student to the list
        add_student2 = input("Enter the name of the other student partner you want to add: ")#Asks user for the second student they want to add
        students2.append(add_student2) #Adds student to the list
        add_grade = input("Enter their grade: ")  #Asks user for the student grade
        grade.append(add_grade) #Adds grade to the list

    elif choice == "4": #If user enters choice as 4...
        specific_student = input("Enter the name of the student whose grade you want to change: ")  #Asks user for the student name they want to change
        if specific_student in students1:   #If the student is found in the first list...
            position = int(students1.index(specific_student))#Takes index position of the student
            new_grade = input("Enter your new grade for this student: ") #Asks user for new grade
            grade[position] = new_grade #Updates grade in the grade list
            print("Grade updated.") #Prints grade has been updated
        elif specific_student in students2: #If the student is found in the second list...
            position = int(students2.index(specific_student))   #Takes index position of the student
            new_grade = input("Enter your new grade for this student: ")    #Asks user for new grade
            grade[position] = new_grade #Updates grade in the grade list
            print("Grade updated.") #Prints grade has been updated
        else:   #Otherwise student not found in either list...
            print("Student not found.") #Prints student not found

    else:   #Otherwise user entry wasn't valid...
        print("Input not found, try again.")    #Prints user input wasn't found

    while True:     #Creates another while loop that asks if user wants to order again
        play_again = input("Would you like to continue? Enter 'yes' or 'no': ")   #Asks user if they would like to order again
        
        if play_again == "yes":            #If user answers yes...
            break                            #Breaks nested while loop, continues program
        elif play_again == "no":            #If user answers no...
            sys.exit()              #Exits the program running in the system
        else:                       #Otherwise user answers a different answer...
            print("Response not understood. Try again.")    #Nested while loop continues and asks user if they want to continue again
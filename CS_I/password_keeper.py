#Name: Irhan Iftikar
#Date: April 4, 2023
#Description: Password Keeper program
#Challenges: Stores a list of passwords, allows user to change passwords, allows a user to view/access a specific website in list

websites = ["netflix", "youtube", "hulu"]       #Creates a default list for websites
usernames = ["user123", "irhan", "iiftikar"]    #Creates a default list for usernames
passwords = ["2023!", "youtube123", "hulu123"]  #Creates a default list for passwords

while True:     #Creates while loop that runs continuously
    statement = print('''Welcome to the password keeper. Enter your choice below:   
        Enter "1" to view passwords.
        Enter "2" to add a password.
        Enter "3" to view/access a specific password.
        Enter "4" to change a specific password.
        Enter "5" to quit program.
    ''')    #Prints welcome statement for the program
    answer = input("Enter your choice: ")      #Asks user for choice in program

    if answer == "1":       #If user chooses 1 to view a password...
        number = int(len(websites))     #Takes the total number of values in the lists
        for n in range (0,number):          #For loop that iterates from index 0 to the last index in the list
            print("Website: ", websites[n], "Username: ", usernames[n], "Password: ", passwords[n]) #Prints all the websites, usernames, and passwords stored in the list
    elif answer == "2":     #If user chooses 2 to add a password
        website_input = input("Enter a website: ").lower()  #Asks user to enter a new website
        usernames_input = input("Enter your username: ").lower()    #Asks user to enter a new username
        password_input = input("Enter your password: ").lower() #Asks user to enter a new password
        websites.append(website_input)  #Adds new website to the list websites
        usernames.append(usernames_input)   #Adds new username to the list usernames
        passwords.append(password_input)       #Adds new password to the list passwords
    elif answer == "3":     #If user chooses 3 to access a specific password...
        answer = input("Enter name of website that you want to access: ").lower()   #Asks user for which website they want to specifically view
        if answer in websites:  #If the website is found in the list...
            position = int(websites.index(answer))  #Locates index position of the website
            print("Website: ", websites[position], "Username: ", usernames[position], "Password: ", passwords[position])    #Prints the website, username, and password for the specific index of website entered
        else:   #Otherwise website not found in list...
            print("Website not found in list, try again.")  #Prints that website wasn't found
    elif answer == "4":
        answer = input("Enter name of website whose password you would like to change: ").lower()   #Asks user for which website they want to specifically view
        if answer in websites:  #If the website is found in the list...
            position = int(websites.index(answer))  #Locates index position of the website
            new_password = input("Enter a new password: ")
            passwords[position] = new_password      #Updates the password in the list passwords
            print("Password updated.")      #Tells user that the password had been updated
        else:           #If the website isn't found in the list...
            print("Website not found in list, try again.")  #Tells user the website isn't found in the list
    elif answer == "5": #If user enters 4 to quit the program...
        break   #Breaks the while loop
    else:   #Otherwise the user's input isn't understood...
        print("Answer not understood. Try again.")      #Prints answer wasn't understood and restarts program
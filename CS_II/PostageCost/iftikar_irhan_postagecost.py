#Name: Irhan Iftikar
#Date: September 2023
#Description: Program that determines postage cost for mail using five entered inputs
#Bonuses: Rounds all values to two decimal points, adds a catch in case of an error and program continues, removes leading '0' in values less than 1
#Bugs: None found
#Sources: StackOverflow for syntax

def postage_class(length, height, thickness):       #Function classifies package using its dimensions
    distance = 2*length + 2*height + 2*thickness             
    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and 0.007 <= thickness <= 0.016:
        return "Regular Post Card"
    elif 4.25 <= length <= 6 and 6 <= height <= 11.5 and 0.007 <= thickness <= 0.015:
        return "Large Post Card"
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and 0.016 <= thickness <= 0.25:
        return "Envelope"
    elif 6.125 <= length <= 24 and 11 <= height <= 18 and 0.25 <= thickness <= 0.5:
        return "Large Envelope"
    elif 0 < length and 0 < height and 0 < thickness and 0 <= distance <= 84:
        return "Package"
    elif 0 < length and 0 < height and 0 < thickness and 84 <= distance <=130:
        return "Large Package"
    else:
        return "Unmailable"

def zone_number(zone):                    #Function classifies zone number of a given zipcode
    if 1 <= zone <= 6999:
        return 1
    elif 7000 <= zone <= 19999:         
        return 2
    elif 20000 <= zone <= 35999: 
        return 3
    elif 36000 <= zone <= 62999: 
        return 4
    elif 63000 <= zone <= 84999: 
        return 5
    elif 85000 <= zone <= 99999: 
        return 6
    else :
        return "Unmailable"                  
    
def total_cost(postage, total_zones):           #Function calculates total cost of shipping the package using its postage class and zones travelled
    if postage == "Regular Post Card":
        cost = .2 + .03*total_zones
    elif postage == "Large Post Card":
        cost = .37 + .03*total_zones
    elif postage == "Envelope":
        cost = .37 + .04*total_zones
    elif postage == "Large Envelope":
        cost = .6 + .05*total_zones
    elif postage == "Package":
        cost = 2.95 + .25*total_zones
    elif postage == "Large Package":
        cost = 3.95 + .35*total_zones
    elif postage == "Unmailable":
        cost = "Unmailable"

    if type(cost) == str:           #Returns cost if it is unmailable
        return cost
    else:
        cost = format(cost, '.2f')              #If the cost is a float, rounds it to two decimal points
        if cost[0] == "0":      
            cost = cost[1:]                 #Removes the 0 is the value is less than one to match the specs
            return cost
        else:
            return cost

def main():                    #Main function that executes the entire program and calls on the other functions
    #Code below prompts user for inputs and executes the program, and prints the cost to ship the package
    length, height, thickness, start_zipcode, end_zipcode = input("").split(",", 5)
    length = float(length)
    height = float(height)
    thickness = float(thickness)
    start_zipcode = int(start_zipcode)
    end_zipcode = int(end_zipcode)
    postage = postage_class(length, height, thickness)
    start_zone = zone_number(start_zipcode)
    end_zone = zone_number(end_zipcode)
    if isinstance(start_zone, int) and isinstance(end_zone, int):       #Checks for zones having a zone number as an integer
        total_zones = abs(start_zone - end_zone)
        cost = total_cost(postage, total_zones)
        print(cost)
    else:
        print("Unmailable")


for i in range (0, 5):                                      #Program runs five times
    try:                                                    #Tests the code below for errors
        main()
    except ValueError:              #If an error occurs, the program assumes it is a user entry and disregards it, and continues the program
        print("User input error, try again.")
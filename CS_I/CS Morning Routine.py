print("In this program, enter 'Yes', or 'No'.")

while True: 
    a = str.lower(input("Is today a school day?" ))
    if a == "yes":
        print("Wake up.")
        break
    elif a == "no":
        print("Sleep in longer.")
        break
    else:
        print("I didn't understand, please retry the program.")

while True:
    b = str.lower(input("Is it raining?" ))
    if b == "yes":
        print("Get a jacket.")
        break
    elif b == "no":
        print("Don't get a jacket.")
        break
    else:
        print("I didn't understand, please retry the program.")

while True:
    c = str.lower(input("Is it warm outside (over 60 degrees)?" ))
    if c == "yes":
        print("Wear a short-sleeve shirt.")
        break
    elif c == "no":
        print("Wear a longer-sleeve shirt/jacket.")
        break
    else:
        print("I didn't understand, please retry the program.")

while True:
    d = str.lower(input("Am I still tired?" ))
    if d == "yes":
        print("Drink some coffee.")
        break
    elif d == "no":
        print("Drink water, not coffee.")
        break
    else:
        print("I didn't understand, please retry the program.")

while True:
    e = str.lower(input("Do I have soccer practice today?" ))
    if e == "yes":
        print("Get my soccer gear.")
        break
    elif e == "no":
        print("Don't get my soccer gear.")
        break
    else:
        print("I didn't understand, please retry the program.")

print("End of program!")

import random 
import string



#Main Program

password = []
total_letters_needed = 0 
letters_needed = 0 
numbers_needed = 0 
symbols_needed = 0 
capital_letters_needed = 0 
password_possible = False
symbols = ["!", "@", "#", "$", "%", "&", "?"]
good  = False

#Function for checking if the password is possible to mkae
def check():
    global password_possible
    if int(numbers_needed) + int(letters_needed) + int(symbols_needed) <= int(total_letters_needed):

            if int(capital_letters_needed) <= int(letters_needed):
                return True 
            else:
                return False 


    else:
        return False 
        

#Function for generating the password
def generate():
    global letters_needed
    global capital_letters_needed
    global numbers_needed
    global symbols_needed
    global symbols
    global my_numbers
    for i in range(int(total_letters_needed)):
        password.append(" ")
    chosennum = 0
    while int(letters_needed) != 0:
        chosennum = random.randint(0, int(total_letters_needed)) - 1
        if password[chosennum] == " ":
            letters_needed = int(letters_needed) - 1
            if int(capital_letters_needed) > 0:
                password[chosennum] = random.choice(string.ascii_uppercase)
                capital_letters_needed = int(capital_letters_needed) - 1
            else:
                password[chosennum] = random.choice(string.ascii_lowercase)

    while int(numbers_needed) != 0:
        chosennum = random.randint(0, int(total_letters_needed)) - 1
        if password[chosennum] == " ":
            numbers_needed = int(numbers_needed) - 1
            password[chosennum] = random.randint(0, 9)

    while int(symbols_needed) != 0:
        chosennum = random.randint(0, int(total_letters_needed)) - 1
        if password[chosennum] == " ":
            symbols_needed = int(symbols_needed) - 1
            password[chosennum] = symbols[random.randint(0, 6)]

    while " " in password:
        chosennum = random.randint(0, int(total_letters_needed)) - 1
        if password[chosennum] == " ":
            password[chosennum] = random.choice(string.ascii_lowercase)
    my_numbers = [1, 2, 3, 4, 5]
    result_string = "".join(str(num) for num in password)
    print(result_string)
    print("This is your secure and strong password! Enjoy!")
 

#This gets input for each parameter for making the password
while password_possible == False:
    while good == False:
        total_letters_needed = input("How long should your password be?\n")
        if total_letters_needed.isdigit() == True:
            good = True
    good  = False
    while good == False:
        letters_needed = input("How many letters are needed?\n")
        if letters_needed.isdigit() == True:
            good = True
    good  = False
    while good == False:
        numbers_needed = input("How many numbers are needed?\n")
        if numbers_needed.isdigit() == True:
            good = True
    good  = False
    while good == False:
        symbols_needed = input("How many special symbols are needed?\n")
        if symbols_needed.isdigit() == True:
            good = True
    good  = False
    while good == False:
        capital_letters_needed = input("How many capital letters are needed?\n")
        if capital_letters_needed.isdigit() == True:
            good = True
    good  = False
    password_possible = check()
    if password_possible == False:
        print("Sorry that didnt work try again!")

#Finally generates the password and outputs it
generate() 
import random 
import string



#Main Program

password = []
length = 0 
letters_needed = 0 
numbers = 0 
symbols_needed = 0 
capitals = 0 
possible = False
symbols = ["!", "@", "#", "$", "%", "&", "?"]
good  = False
        

#Function for generating the password
def generate(letters_needed, capitals, numbers, symbols_needed, symbols):
    for i in range(length):
        password.append(" ")
    chosennum = 0
    while letters_needed != 0:
        chosennum = random.randint(0, length) - 1
        if password[chosennum] == " ":
            letters_needed = letters_needed - 1
            if capitals > 0:
                password[chosennum] = random.choice(string.ascii_uppercase)
                capitals -= 1
            else:
                password[chosennum] = random.choice(string.ascii_lowercase)

    while numbers != 0: 
        chosennum = random.randint(0, length) - 1
        if password[chosennum] == " ":
            numbers -= 1
            password[chosennum] = random.randint(0, 9)

    while symbols_needed != 0:
        chosennum = random.randint(0, length) - 1
        if password[chosennum] == " ":
            symbols_needed -= 1
            password[chosennum] = symbols[random.randint(0, 6)]

    while " " in password:
        chosennum = random.randint(0, length) - 1
        if password[chosennum] == " ":
            password[chosennum] = random.choice(string.ascii_lowercase)
    result_string = "".join(str(num) for num in password)
    print(result_string)
    print("This is your secure and strong password! Enjoy!")
 
def get_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Please enter a valid input\n")


#This gets input for each parameter for making the password
while not possible:

    length = get_int("How long should your password be?\n")
    letters_needed = get_int("How many letters are needed?\n")
    numbers = get_int("How many numbers are needed?\n")
    symbols_needed = get_int("How many special symbols are needed?\n")
    capitals = get_int("How many capital letters are needed?\n")
    
    if numbers + letters_needed + symbols_needed > length or capitals > letters_needed:
        print("Please enter a possible password")
    else:
        possible = True

#Finally generates the password and outputs it
generate(letters_needed, capitals, numbers, symbols_needed, symbols) 
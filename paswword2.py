if __name__ == "__main__":
    #import python random module for our project
    import random

    #Declaring variable to hold the characters will want to use for our password
    upercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = upercase.lower()
    digit = "1234567890"
    special_ch = "|<>?,./~@:;'#}{[]+_)(*&^%$£"

    #creating a variable and boolean to represent each state of the characters 
    upper, lower, numbers, symbols = True, True, True, True

    #hold the values for the password generated
    all_characters = ""

    #If statements to check if certain character is to be choosen for the password
    if upper:
        all_characters += upercase
    if lowercase:
        all_characters += lowercase
    if digit:
        all_characters += digit
    if special_ch:
        all_characters += special_ch
    
    #Gives the number of characters to be generated    
    lenght = 15
    #Give how many times the passwords to be generated
    amount =1

    #for loop to create a password within the range of the amount
    #and join each characters without leaving any space in between
    #with the length of password specified
    for x in range(amount):
        password = "".join(random.sample(all_characters, lenght))
        print(password)
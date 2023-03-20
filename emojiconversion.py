if __name__ == "__main__":
    # Take inputs from the user
    emoji = input("Enter your emoji characters here! ")

    #split every words the users enter
    word = emoji.split()

    #The group of list where our emojis will be selected from
    symbols ={"(=^..^=)": "😺",
        ":)": "☺️",
        ":-p": "😛",
        "=)": "😊",
        "</3": "💘",
        "<3": "❤️",
        ":-(": "☹️" }
    
    #Holds the value of our output/result
    output=""

    #The loop gets each of the word from the user and merge it with the values in our dictionary
    #it will now return the value of each key as emojis and then return not available for any
    #word that is not in our dictionary
    for letters in word:
        output += symbols.get(letters, "not available" )

    #print out the output
    print(output)
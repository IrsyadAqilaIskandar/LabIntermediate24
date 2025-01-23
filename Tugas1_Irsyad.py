secretWord = "mobil"

while True:

    inputUser = input("Enter a single letter: ")

    if len(inputUser) == 1 and ('a' <= inputUser <= 'z' or 'A' <= inputUser <= 'Z'):
        if inputUser in secretWord or inputUser in secretWord.upper():
            print("this letter is in the secret word")
            continue
        else:
            print("this letter is not in the secret word")
            break
    else:
        print("invalid input")
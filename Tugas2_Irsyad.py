secretWord = "lab"
attemps = 0
maximalAttemps = 6
guessedWord = []
correctGuesses = 0

while attemps < maximalAttemps:
    inputLetter = input("Masukkan satu buah huruf= ")
    if len(inputLetter) == 1 and ('a' <= inputLetter <= 'z' or 'A' <= inputLetter <= 'Z'):
        if inputLetter in guessedWord:
            print("Anda sudah memasukkan huruf tersebut !")
        elif inputLetter in secretWord:
            print("Selamat huruf anda ada di kata tersembunyi !")
            guessedWord.append(inputLetter)
            attemps += 1
            correctGuesses += 1
        else:
            print("Maaf huruf anda tidak ada di kata tersembunyi !")
            attemps += 1
        if correctGuesses == len(secretWord):
            print("Selamat, anda telah menebak semua huruf!", secretWord, "adalah kata tersembunyinya!")
            break
    else:
        print("Error, masukkan yang benar !")
    print("anda mempunyai ", maximalAttemps - attemps, "attemps lagi")
if attemps == maximalAttemps:
    print("Maaf anda telah menggunakan semua attemps")

secret_word = "milk"

def hangman():
    guessess = " "
    chances = 6
    while chances > 0:
        word_display = " "
        for letter in secret_word:
            if letter in guessess:
                word_display += letter
            else:
                word_display += "-"
        print("kataa:", {word_display})  

        if word_display == secret_word: 
            print("anda menang, katanya adalah", {secret_word})
            return

        print("Chances left:", {chances})
        guess = input("masukkan satu huruf: ").lower()
        if len(guess) != 1:
            print("masukkan satu huruf saja")
            continue
        if not ('a' <= guess <= 'z'):
            print("masukkan huruf saja")
            continue
        if guess in guessess:
            print("sudah mencoba huruf tersebut")
            chances -= 1  
            continue

        guessess += guess

        if guess in secret_word:
            print("bener")
        else:
            print("salah.")
            chances -= 1  

    print("You lose! The word was:", {secret_word}) 

hangman()
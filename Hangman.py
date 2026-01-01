import random as r
import os
os.system('cls')

words = [
    "pineapple",
    "guitar",
    "volcano",
    "marble",
    "wizard",
    "pencil",
    "ocean",
    "puzzle",
    "rocket",
    "jungle",
    "butterfly",
    "castle",
    "pirate",
    "planet",
    "cactus",
    "dragon",
    "shadow",
    "tunnel",
    "cookie",
    "meteor"
]

def game(lives):
    guessed = False
    letters_used = []
    word = r.choice(words)
    word_letters = list(word)
    word_gaps = list(len(word_letters) * "_")
    while lives > 0 :
        print("\nWord: ",*word_gaps)
        if word_gaps == word_letters:
            guessed = True
            break
        print("Lives left: " ,lives)
        while True:
            letter = input("\nGuess a first letter: ").lower()
            if len(letter) == 1:
                if letter in letters_used:
                    print("\nLetter has already been used!\n")
                else:
                    letters_used.append(letter)
                    break
            else:
                print("\n1 Letter only!\n")
        os.system('cls')
        if letter in word_letters:
            for letter_index in range(len(word)):
                if word_letters[letter_index] == letter:
                    word_gaps[letter_index] = word_letters[letter_index]
            print("Good Guess!")
        else:
            print("Wrong Guess!")
            lives -= 1
    os.system('cls')
    if guessed == False:
        print("\n\nThe word was " + word.upper() + "!")
    else:
        print("\n...\n\nCongratulations! You guessed the word: ",word.upper())

while True:
    print("Welcome to Hangman!")
    game_mode = input("Easy mode or Hard mode (Easy/Hard): ")
    if game_mode.lower() == "easy":
        os.system('cls')
        game(10)
        break
    elif game_mode.lower() == "hard":
        os.system('cls')
        game(5)
        break
    else:
        os.system('cls')
        print("Respond with Easy/Hard only!\n")
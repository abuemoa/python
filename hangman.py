import random
from words import word_list
import string

# Define a random choice variable that gets rid
# of any words that contain spaces and/or dashes.
def get_valid_word(word_list):
    word = random.choice(word_list) # chooses a word randomly
    while "-" in word or "  " in word:
        word = random.choice(word_list)

    return word.upper()

# Gets a word in the variable word and then 
# stores the word letters of that word in a
# variable called word_letters.
# The variable alphabet is to have the words in uppercase

def hangman():
    word = get_valid_word(word_list)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    user_letter = input("Guess a letter: ").upper

    lives = int(7)

    while len(word_letters) > 0 and lives > 0:
        word_lists = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_lists))
        print("You have used these letters ", "".join(used_letters))


        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if used_letters in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_letters:
            print("You have used it already, please try again\n")
        else:
            print("invalid character, please try again.\n")
    if lives == 0:
        print("You lost, the word was", word)
    else:
        print("yout guessed the word", word, "!!")

hangman()
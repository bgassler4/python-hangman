# create classic hangman game using Python
import random


def random_word(word_list: list):
    """
    :return: returns a random word from the list
    """
    return random.choice(word_list).lower();


def is_letter_in_word(word: str, letter: str):
    """
    :param word: the word being guessed
    :param letter: The user guessed letter that needs to be checked
    :return: True if letter is in the word, false if not
    """
    if letter in word:
        return True
    else:
        return False


def update_progress(word, guessed_letters):
    """
    :return: returns the current progress of the guessed word with blanks for all
    letters not yet guessed (ex: w_rd)
    """
    guessed_progress = ""
    for letter in word:
        # add the letter if it's been guessed, otherwise add a _ for letters that haven't been guessed yet
        if letter == " ":
            guessed_progress += "  "
        elif letter in guessed_letters:
            guessed_progress += letter + " "
        else:
            guessed_progress += "_ "

    return guessed_progress


def print_game_data(guessed_letters: str, guesses: int, progress: str):
    print(hanger_graphics[guesses])
    print(progress)
    if len(guessed_letters) > 0:
        print(f"Letters You've Guessed: {guessed_letters}")


def end_game(success: bool, word: str):
    """
    this function ends the game and prints out a message based on whether the user
    successfully guessed the word or not
    :param word: the secret word being guessed
    :param success: was the word guessed successfully
    """
    if success:
        # print the winner graphic (last graphic)
        print(hanger_graphics[len(hanger_graphics) - 1] + "\n")
        print(f"YOU WON! The word was {word}\n")
    else:
        # print the losing graphic (second to last graphic)
        print(hanger_graphics[len(hanger_graphics) - 2] + "\n")
        print(f"You lost. The word was: {word}\n")

    play_again()


def play_again():
    print("Wanna play again?")
    print("")
    again = str(input("Type y for yes and n for no: "))
    if again.lower() == "y":
        play_hangman()

    quit()


# found the graphics online from an example: https://code.sololearn.com/cooDpbbEc1VK/#py
hanger_graphics = ['''
                 _____
                |     |
                      |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                |     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
                     _|_''', ''' 
                 _____
                |     |
                O     |
               /|\    |
                |     |
               /     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
               / \   _|_''', '''
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    

                    \O/      
          ~WINNER~   |   ~WINNER~        
                     |    
                    / \ 

       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']


def play_hangman():
    game_over = False  # flag for whether the game is still ongoing
    guesses = 0  # total number of unsuccessful guesses
    possible_words = ["pizza", "pasta", "pickle", "cucumber", "banana", "onion",
                      "apple", "ribs", "hummus", "taco", "burrito", "hot sauce",
                      "DOUBLE BURGER", "one triple Burger", "two pizzas pies", "chocolate"]
    word = random_word(possible_words)
    guessed_letters = ""  # the letters that the user has guessed
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # acceptable characters for user to guess
    progress = update_progress(word, guessed_letters)

    while not game_over:
        print_game_data(guessed_letters, guesses, progress)
        guess = input("Please guess a letter: ")
        print("")
        guess = guess.strip().lower()

        if len(guess) > 1:
            print("You can only guess one letter at a time!")
        elif guess == "":
            print("Please enter a letter.")
        elif guess not in alphabet:
            print("Please Enter a letter a-z")
        elif guess in guessed_letters:
            print("You've already guessed that letter")

        else:
            guessed_letters += guess + " "
            # update the game data based on whether the guessed letter is
            # in the word or not
            if is_letter_in_word(word, guess):
                progress = update_progress(word, guessed_letters)
                if "_" not in progress:
                    # if there are no more blanks the user has successfully guessed the word
                    end_game(True, word)
                    game_over = True

            else:
                guesses += 1
                # end the game if there are no more hanger graphics
                if guesses == len(hanger_graphics) - 1:
                    end_game(False, word)
                    game_over = True
                else:
                    print("Your letter was not found")


play_hangman()

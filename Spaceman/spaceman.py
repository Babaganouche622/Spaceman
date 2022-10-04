import random
import re

wrong_letters = []
correct_letters = []

COLOUR_BLUE = '\033[94m'
COLOUR_CYAN = '\u001b[36m'
COLOUR_GREEN = '\033[92m'
COLOUR_YELLOW = '\u001b[33m'
COLOUR_RED = '\u001b[31m'
COLOUR_MAGENTA = '\u001b[35m'
COLOUR_END = '\033[0m'
colour_array = [COLOUR_BLUE, COLOUR_CYAN, COLOUR_MAGENTA, COLOUR_GREEN, COLOUR_YELLOW, COLOUR_RED]

def load_word():
    """
    Description: opening list_of_words.txt, reading the lines and grabbing a random word.

    Parameters: No passthrough parameters, but we do need to make sure we import random.

    Return: We will return our randomly generated secret word.
    """
    f = open('list_of_words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, correct_letters):
    """
    Description: Here we are checking our correct letters array against our secret word
    to find out if we have guessed the full word.

    Parameters: We pass through our secret_word, and our array of correct_letters guessed.

    Return: We then return a true/false value if the word has been guessed.
    """
    word = ""
    word_is_guessed = False
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            word += secret_word[i]
            if word == secret_word:
                word_is_guessed = True
    return word_is_guessed


def get_guessed_word(secret_word, correct_letters):
    """
    Description: Here we are looping through the secret word to print either _Underscores or the correct letters from our guesses.
    The printing should be happening in correct letter placement for the secret word.

    Parameters: We pass through the secret_word and our correct_letters array.

    Return: We return the final "Hidden word" which should display missing letters with "_" or the correct letters guessed so far.
    """
    hidden_word = ""
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters :
            hidden_word += f'{secret_word[i]} '
        else:
            hidden_word += "_ "
    return hidden_word


def is_guess_in_word(guessed_letter, secret_word):
    """
    Description: Here we are checking if the user's guess is in the secret word or not. 
    If it is we push the letter into the correct letters array.
    If not we push the letter into the wrong letters array.

    Parameters: We pass through the guessed_letter from user's input, and the secret_word.

    Return: We don't return anything here because we are just appending the arrays depending on our conditional statement.
    """
    if guessed_letter in secret_word:
        correct_letters.append(guessed_letter)
    else:
        wrong_letters.append(guessed_letter)


def guess_checker(guessed_letter, correct_letters, wrong_letters):
    """
    Description: Here we are validating our user input. We need to check for 3 things:
    1) Has the user entered a special character. example (!?{})*&^ ...)
    2) Has the user entered multiple letters.
    3) Has the user entered a letter already guessed.
    If all of these are false, we then accept the input and end the loop.

    Parameters: We nee to pass through our guessed_letter, the list of correct_letters, and the list of wrong_letters

    Return: We should only be returning a single valid letter.
    """
    garbage = re.compile("[a-z]*")
    while True:
        if guessed_letter in correct_letters or guessed_letter in wrong_letters:
            guessed_letter = input(f"\n{COLOUR_YELLOW}Already guessed this letter.\nPlease enter a new one: {COLOUR_END}\n").lower()
            continue
        if garbage.fullmatch(guessed_letter) is None or len(guessed_letter) != 1:
            guessed_letter = input(f"\n{COLOUR_YELLOW}Sorry, guess not valid.\nPlease enter a new one: {COLOUR_END}\n").lower()
            continue
        if garbage.fullmatch(guessed_letter) is not None:
            pass

        return guessed_letter


def page_break():
    """
    Description: This was just a fun idea to create a page break for clarity sake between guesses.
    This will loop 60 times and build a string of randomly coloured ^hats.

    Parameters: No need to pass through any paramaters.

    Return: We will return a string of randomly coloured ^hats.
    """
    break_page = ""
    i = 0
    
    while i < 60:
        break_page += f"{random.choice(colour_array)}^{COLOUR_END}"
        i += 1
    return break_page

def instructions():
    """
    Description: Here we just ask the user if they want to hear instructions. If yes display them, if no skip. 
    Made an exit option for smartasses who aren't ready to play.

    Parameters: No parameters because we aren't passing anything through here.

    Return: No return but we do print to screen the instructions.
    """
    instruction = input(f"\n{COLOUR_BLUE}Would you like to see the instructions?{COLOUR_END} {COLOUR_YELLOW}(yes/no){COLOUR_END}  ").lower()
    if instruction == "yes":
        print(f"\n{page_break()}\n\n{COLOUR_BLUE}How to play this Spaceman game:{COLOUR_END}\n\n{COLOUR_CYAN}Guess letters every round until you complete the word or run out of guesses.{COLOUR_END}\n\n{COLOUR_MAGENTA}You have 7 attempts to guess correctly before losing.{COLOUR_END}\n\n{COLOUR_GREEN}If you guess all the letters you get a cookie.{COLOUR_END}\n\n{COLOUR_YELLOW}Well, a space cookie, but you can eat it when you get to space.{COLOUR_END}\n\n{COLOUR_RED}I recommend calling Musk, or Bezos about this cookie.{COLOUR_END}\n")
        stop = input(f"{COLOUR_BLUE}Ready to start?{COLOUR_END}\n").lower()
        if stop == "no":
            exit()
    else:
        print(f"{COLOUR_BLUE}Okay lets play!{COLOUR_END}\n")


def win_condition(secret_word, wrong_letters):
    """
    Description: Here we are just determining once the gameplay loop has found a win/lose condition, we come in here to find out which one it is and what we need to print to the user.

    Parameters: We are using our secret_word and wrong_letters.

    Return: We return a false value to end the gameplay loop.
    """
    if len(wrong_letters) == 7:
        print(f"\n{COLOUR_RED}Musk called, fatal crash of driverless delivery while enroute. No cookie for you.{COLOUR_END}\n")
        print(f"\n{COLOUR_MAGENTA}The secret word is: {COLOUR_END}{COLOUR_YELLOW}{secret_word}{COLOUR_END}\n")
        return False
    else:
        print(f"\n{COLOUR_GREEN}Bezos called, said your cookie will arrive with next day shipping.{COLOUR_END}\n")
        print(f"\n{COLOUR_MAGENTA}The secret word is:{COLOUR_END} {COLOUR_YELLOW}{secret_word}{COLOUR_END}\n")
        return False


def guess_word_line(secret_word, correct_letters, wrong_letters):
    """
    Description: Here we are printing our line at the top of the page break.
    I wanted to catch the plural/singular that happens as you get incorrect guesses.

    Parameters: We pass through secret_word, correct_letters, and wrong_letters.

    Return: We aren't returning anything, only printing to the user.
    """
    if (7 - len(wrong_letters)) == 1:
        print(f"\n{COLOUR_BLUE}Guess this word: {COLOUR_END}{COLOUR_GREEN}{get_guessed_word(secret_word, correct_letters)}{COLOUR_END}{COLOUR_BLUE} You will lose your cookie in {COLOUR_END}{COLOUR_RED}{7 - len(wrong_letters)}{COLOUR_END}{COLOUR_BLUE} wrong try!{COLOUR_END}\n")
    else:
        print(f"\n{COLOUR_BLUE}Guess this word: {COLOUR_END}{COLOUR_GREEN}{get_guessed_word(secret_word, correct_letters)}{COLOUR_END}{COLOUR_BLUE} You will lose your cookie in {COLOUR_END}{COLOUR_RED}{7 - len(wrong_letters)}{COLOUR_END}{COLOUR_BLUE} wrong tries!{COLOUR_END}\n")


def spaceman():
    """
    Description: Here we run our game. We load a random secret word, and start interacting with the user.
    We first ask about instructions. We need to have a reason for playing, and a clear explenation of how to play.
    We then start the main loop, first grabbing the user input guess and running our checker.
    Then we run our other functions to move the guess into the correct arrays.
    Then check to see if the WIN/LOSE conditions are met.
    If yes display win/lose info and break loop.
    If no then we should loop back.
    The whole time the user should be able to see:
    How many words guessed right/wrong, the hidden word starting to reveal with correct guesses.
    The total failed attempts decreasing with every wrong guess.
    Parameters: We don't need to pass through any parameters because everything is happening inside this function.
    Return: No return, once the loop ends the game is over.
    """
    secret_word = load_word()
    game_state = True
    guessed_letter = ""
    instructions()
    while game_state is True:
        print(page_break())
        # Uncomment this line to test win
        # print(secret_word)
        guess_word_line(secret_word, correct_letters, wrong_letters)
        print(f"{COLOUR_YELLOW}Your incorrect guesses: {COLOUR_END}{COLOUR_RED}{wrong_letters}{COLOUR_END}\n")
        print(f"{COLOUR_CYAN}Your correct guesses:{COLOUR_END} {COLOUR_GREEN}{correct_letters}{COLOUR_END}\n")
        guessed_letter = input(f"{COLOUR_BLUE}Guess a letter:{COLOUR_END} ").lower()
        guessed_letter = guess_checker(guessed_letter, correct_letters, wrong_letters)
        is_guess_in_word(guessed_letter, secret_word)
        if is_word_guessed(secret_word, correct_letters) is True or len(wrong_letters) == 7:
            game_state = win_condition(secret_word, wrong_letters)

spaceman()

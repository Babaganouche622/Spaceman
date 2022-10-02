import random
import re

wrong_letters = []
correct_letters = []

colour_blue = '\033[94m'
colour_cyan = '\u001b[36m'
colour_green = '\033[92m'
colour_yellow = '\u001b[33m'
colour_red = '\u001b[31m'
colour_magenta = '\u001b[35m'
colour_end = '\033[0m'
colour_array = [colour_blue, colour_cyan, colour_magenta, colour_green, colour_yellow, colour_red]

def load_word():
    f = open('list_of_words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, correct_letters):
    word = ""
    word_is_guessed = False
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            word += secret_word[i]
            if word == secret_word:
                word_is_guessed = True
    return word_is_guessed


def get_guessed_word(secret_word, correct_letters):
    hidden_word = ""
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters :
            hidden_word += secret_word[i] 
        else:
            hidden_word += "_"
    return hidden_word


def is_guess_in_word(guessed_letter, secret_word):
    if guessed_letter in secret_word:
        correct_letters.append(guessed_letter)
    else:
        wrong_letters.append(guessed_letter)

    #TODO: check if the letter guess is in the secret word


def guess_checker(guessed_letter):
    garbage = re.compile("[a-z]*")
    while True:
        if garbage.fullmatch(guessed_letter) == None or len(guessed_letter) > 1 or guessed_letter == "":
            guessed_letter = input(f"\n{colour_yellow}Sorry, guess not valid.\nPlease enter a new one: {colour_end}\n").lower()
            continue
        elif garbage.fullmatch(guessed_letter) != None:
            pass
        return guessed_letter


def page_break():
    break_page = ""
    i = 0
    
    while i < 60:
        break_page += f"{random.choice(colour_array)}^{colour_end}"
        i += 1
    return break_page


def spaceman():
    secret_word = load_word()
    game_state = True
    guessed_letter = ""
	# INSTRUCTIONS 
    instructions = input(f"\n{colour_blue}Would you like to see the instructions?{colour_end} {colour_yellow}(yes/no){colour_end}  ").lower()
    if instructions == "yes":
        print(f"\n{page_break()}\n\n{colour_blue}How to play this Spaceman game:{colour_end}\n\n{colour_cyan}Guess letters every round until you complete the word or run out of guesses.{colour_end}\n\n{colour_magenta}You have 7 attempts to guess correctly before losing.{colour_end}\n\n{colour_green}If you guess all the letters you get a cookie.{colour_end}\n\n{colour_yellow}Well, a space cookie, but you can eat it when you get to space.{colour_end}\n\n{colour_red}I recommend calling Musk, or Bezos about this cookie.{colour_end}\n")
        stop = input(f"{colour_blue}Ready to start?{colour_end}\n").lower()
        if stop == "no":
            exit()
    else:
        print(f"{colour_blue}Okay lets play!{colour_end}\n")

    while game_state == True:
        print(page_break())
        print(f"\n{colour_blue}Guess this word: {colour_end}{colour_green}{get_guessed_word(secret_word, correct_letters)}{colour_end}{colour_blue} You have {colour_end}{colour_red}{7 - len(wrong_letters)}{colour_end}{colour_blue} guesses left!{colour_end}\n")
        print(f"{colour_yellow}Your incorrect guesses: {colour_end}{colour_red}{wrong_letters}{colour_end}\n")
        print(f"{colour_cyan}Your correct guesses:{colour_end} {colour_green}{correct_letters}{colour_end}\n")
        guessed_letter = input(f"{colour_blue}Guess a letter:{colour_end} ").lower()
        guessed_letter = guess_checker(guessed_letter)
        is_guess_in_word(guessed_letter, secret_word)
        if is_word_guessed(secret_word, correct_letters) == True or len(wrong_letters) == 7:
            if len(wrong_letters) == 7:
                print(f"\n{colour_red}You lose!{colour_end}\n")
                print(f"\n{colour_magenta}The secret word is: {secret_word}{colour_end}\n")
                game_state = False
            else:
                print(f"\n{colour_green}You win!!!!{colour_end}\n")
                print(f"\n{colour_magenta}The secret word is:{colour_end} {colour_yellow}{secret_word}{colour_end}\n")
                game_state = False

spaceman()

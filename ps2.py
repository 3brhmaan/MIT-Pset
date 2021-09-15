# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    check = True
    for letter in secret_word:
        if letter not in letters_guessed:
            check = False
            break
        else:
            letters_guessed.pop(letter)
    return check




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    the_word = ""
    for letter in secret_word:
         if letter in letters_guessed:
             the_word+=letter
             #letters_guessed.remove(letter)
         else:
             the_word+='_ '
    return the_word




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            word+=letter
    return word
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    list_secret_word=[]
    list_secret_word.extend(secret_word)


    number_of_guesses = 6

    print("Welcome to the game Hangman!")

    print("I am thinking of a word that is",len(list_secret_word),"letters long.")
    print("-------------")

    all_letter = []
    all_letter.extend(string.ascii_lowercase)
    idx = 0

    the_guessed_word = []
    for i in range(len(secret_word)):
        the_guessed_word.append('_ ')

    str_the_guessed_word = ""
    for letter in the_guessed_word:
        str_the_guessed_word += letter

    number_of_warning = 3
    print("You have", number_of_warning, "warnings left.")

    temp_letter = ""



    while(number_of_guesses>0 and len(list_secret_word)>0):

        print("u have",number_of_guesses,"guesses left.")

        str_all_letter = ""
        for letter in all_letter:
            str_all_letter+=letter
        print("Available letters:",str_all_letter)
        
        Letter = input("Please guess a letter: ")


        if Letter >='a' and Letter <='z' or Letter>='A'and Letter<='Z':
            Letter=str.lower(Letter)
            check = False

            for i in range(len(list_secret_word)):
                if Letter == list_secret_word[i]:
                    the_guessed_word[i+idx]=list_secret_word[i]
                    check = True
                    idx+=1
                    list_secret_word.remove(Letter)
                    break

            str_the_guessed_word = ""
            for letter in the_guessed_word:
                str_the_guessed_word += letter

            if check == True:
                print("Good guess: ", str_the_guessed_word)
                all_letter.remove(Letter)
                number_of_guesses+=1
            else:
                if Letter==temp_letter:
                    number_of_warning-=1
                    if number_of_warning <= 0:
                        number_of_warning = 0

                    print("Oops! You've already guessed that letter. You now have",number_of_warning,"warnings",str_the_guessed_word)
                    temp_letter=Letter
                else:
                    print("Oops! That letter is not in my word:",str_the_guessed_word)
                    temp_letter = Letter

        elif Letter == '*':
            print("Possible word matches are:")
            show_possible_matches(str_the_guessed_word)


        else:
            number_of_warning -= 1
            print("Oops! That is not a valid letter. You have",number_of_warning,"warnings left:",str_the_guessed_word)

            if number_of_warning<=0:
                number_of_warning=0
            else:
                number_of_guesses-=1
        print("------------")
        number_of_guesses-=1

    num_of_unique_letter = 0

    for letter in string.ascii_lowercase:
        if letter in the_guessed_word:
            num_of_unique_letter+=1

    if (len(list_secret_word) == 0):
        print("Congratulations, you won!")
        print("Your total score for this game is:",number_of_guesses*num_of_unique_letter)
    else:
        print("Sorry, you ran out of guesses. The word was",secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    new_word=strip(my_word)
    check = True
    for i in range(len(new_word)):
        if new_word[i] >='a'and new_word[i]<='z':
            if new_word[i]!=other_word[i]:
                check=False
    return check



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    new_word=strip(my_word)
    for word in wordlist:
        check = True
        if len(word)==len(new_word):
            for i in range(len(new_word)):
                if new_word[i]>='a'and new_word[i]<='z'and word[i]!=new_word[i]:
                    check=False
        else:
            check=False
        if check == True:
            print(word)




def strip(my_word):
    new_word = ""
    for letter in my_word:
        if letter != ' ':
            new_word+=letter
    print(new_word)
    return new_word


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    hangman(secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)

    #letters_guessed=['e', 'i', 'k', 'p', 'r', 's']
    #check = is_word_guessed('apple',letters_guessed)
    #print(check)

    #print(get_guessed_word('apple', letters_guessed))

    #hangman(secret_word)

    #print(show_possible_matches("t_ _ t"))
    #hangman_with_hints('apple')

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

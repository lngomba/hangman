import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomlly chooses something from the list of words
    while "-" in word or ' 'in word:
        word = random.choice(words)

    return word.upper() #for words to be capitalised return word.upper()

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)#letters in the word
    alphabet = set(string.ascii_uppercase) #contain all uppercase letters o the english alphabet
    used_letters = set() #what the user has guessed

    lives = len(word)*2
    print(f"The word has {len(word)} letters. You start with {lives} lives.")
    

    hints_used = 0
    max_hints = 2 #limit hints to keep 

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        #' '.join(['a', 'b', 'd']) --> 'a b cd'
        print('You have', lives,'lives left and you have used these letter: ', ' '.join(used_letters))

        #what current word is ( ie W-RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        user_letter = input("Guess a letter or type 'hint': ").upper()
        
        #HINT FEATURE
        if user_letter == "hint":
            if hints_used < max_hints:
                remaining_letters = list(word_letters)
                if remaining_letters:
                    hint_letter = random.choice(remaining_letters)
                    print(f"HINT: The word continues the letter '{hint_letter}'")
                    used_letters.add(hint_letter)
                    word_letters.remove(hint_letter)
                    hints_used +=1
                else:
                    print("No hints available!")
            else:
                print("You have used all your hints.")
            continue


        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives -1 #takes aay a life if wrong
                print('Letter is not in word.')    
                
        elif user_letter in used_letters:
            print('You have already used the character. Please try again.')
        else:
            print('Invalid character. Please try again.')   

  #gets here whe len(word_letters) == 0 OR when lives ==0          
    if lives ==0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessd the word', word, '!!')
hangman()
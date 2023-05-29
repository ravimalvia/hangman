# THIS IS HANGMAN GAME 
import hangman_words
from hangman_symbol import hangman, stage, lost
import random

print(hangman)


chosen_word=random.choice(hangman_words.word_list)

#print(chosen_word)


empty_list=["_"]*len(chosen_word)
#print(empty_list)
print(f"there are {len(list(chosen_word))} letters in the Word\n")
print(f"{' '.join(empty_list)}\n")

lives=6


end_of_game=False

while not end_of_game:
  
    given_letter=input("Guess the letter :  ")
    
    if given_letter in empty_list:
      print("You've already guessed this letter")
      
    for position in range(len(chosen_word)):
        if chosen_word[position]==given_letter:
            empty_list[position]=given_letter
    print(f"\n{' '.join(empty_list)}\n")
        
        
    if given_letter not in chosen_word:
        lives-=1
        print("Guessed letter is not in the word, So you lose a life\n")
        print("You can have Three hints")
        print(stage[lives])
        if lives==0:
            end_of_game=True    
            print(lost)
                

    if '_' not in empty_list:
        end_of_game = True
        print('''
            +---+  +---+  +---+   
            |   |  |   |  |   |     
            | Y |  | O |  | U |     
            |   |  |   |  |   |         
            +---+  +---+  +---+
            +---+  +---+  +---+
            |   |  |   |  |   |
            | W |  | I |  | N |
            |   |  |   |  |   |
            +---+  +---+  +---+
            
              Congratulation
            ''')
    
            
    
        


import random
import hangman_words
import hangman_art

end_of_game = False;
lives = 6
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

word = []
for _ in chosen_word:
  word += "_"
  
print(f"{' '.join(word)}\n")

while not end_of_game:

  guess = input("Guess a letter: ").lower()
  if guess in word:
    print(f"You've already guessed {guess}")
    
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if(guess == letter):
      word[position] = letter

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life!")
    print(hangman_art.stages[lives])
    lives -= 1
    if (lives == 0):
      end_of_game = True
      print("You Lose")

  print(f"{' '.join(word)}\n")
    

  if "_" not in word:
    end_of_game = True
    print("You Win!")

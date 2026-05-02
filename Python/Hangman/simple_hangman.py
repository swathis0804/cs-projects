import random
word_bank = ['rizz', 'ohio', 'sixseven', 'skibidi', 'yeet']
word = random.choice(word_bank)
guessed_word = '_' * len(word)
attempts = 10; 
while (attempts > 0):
    print("Current word: ", guessed_word);
    print("You have ", attempts, " attempts remaining")
    guess = input("Guess a letter: ").lower()
    if guess in word: 
        for i in range(len(word)): 
            if guess == word[i]:
                guessed_word = guessed_word[:i] + word[i] + guessed_word[(i+1):]
        print("Good guess!")
        attempts -= 1
    else:
        print("Wrong guess! Attempt again...")
        attempts -= 1
    if '_' not in guessed_word:
        print("Congratulations! You have guessed the word!")

if attempts == 0 and '_' in guessed_word:
    print('Oh no! You have run out of guesses.')
    print('The word was', word)
    print('Try again!')

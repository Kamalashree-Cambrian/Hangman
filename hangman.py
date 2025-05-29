#import random

with open("words.txt") as f:
    word = f.read().splitlines()

word = random.choice(word)
tries = 6
guessed = set()

while tries>0:
    display = "".join([c if c in guessed else "_ " for c in word])
    print("word: ",display)

    if "_" not in display:
        print("you won !")
    guess = input("enter a letter: ")
    if guess in word:
        guessed.add(guess)
    else:
        tries -=1

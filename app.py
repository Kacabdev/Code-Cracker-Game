import random
from words import word_list
from assets import logo

print(logo)
print("Welcome to the Code Cracker Game! by @KACABDEV")
word = random.choice(word_list).lower()
print("The word has been selected. Start guessing!")

attempts = 6
game_over = False
guessed_letters = []
display = ["_" for _ in word]

while not game_over:
    print("Current word: " + " ".join(display))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for index in range(len(word)):
            if word[index] == guess:
                display[index] = guess
        print("✅ Good job!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! You have {attempts} attempts left.")

    if "_" not in display:
        print("🎉 Congratulations! You cracked the code: " + word)
        game_over = True

    if attempts == 0:
        print("💀 Game Over! The word was: " + word)
        game_over = True

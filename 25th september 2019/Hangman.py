guessesTaken = 0
print("Welcome to Hangman ")
player_name = input("Write your name here : ")
another_player_guess = input("What do you want the first player to guess? : ")
guesses = []
word = []
while guessesTaken < 11:
    print("Guess a letter")
    guess = input()
    guesses.append(guess)
    guessesTaken = guessesTaken + 1
    if ''.join(word) == another_player_guess:
        print('Congratulation you guess the right thing')
        break
    elif len(guess) > 1 and another_player_guess == guess:
        print (another_player_guess)
        print ('Congratulation you guess the right thing')
        break
    else:
        for char in another_player_guess:
            if char in guesses:
                word.append(char)
                print(char)
            else:
                print('_')
else:
    print("you didnt guess in time")
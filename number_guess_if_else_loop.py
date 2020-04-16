# Computer guesses number

import random

target = int(input("Enter a number between 1 and 100\n do you want the comunter to guess? "))

if target > 100 or target < 1:
    target = int(input("Enter a number between 1 and 100\n do you want the comunter to guess? "))

count = 0
mnm = 1
mxm = 100

guess = random.randint(mnm,mxm)

while guess != target:
    guess = random.randint(mnm,mxm)
    print("guessing", guess)
    if guess == target:
        print("Got it!")
        break

    if guess < target:
        print(guess, "is too low")
        nmn = guess + 1
    else:
        mxm = guess -1
        print(guess,"is too high")

    count += 1


print("guessed", guess, "in", count, "tries")
input("press enter to exit")

input("\n\ Press enter to end the program")

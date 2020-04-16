# Flip a Coin
import random

flips = 0
flip = 0
heads = 0
tails = 0

while flips < 100:
    flip = random.randint(0,1)
    if flip:
        heads += 1
    else:
        tails += 1
    flips += 1

print(heads, "heads and", tails, "tails")

input ("\n\ Press enter to quit program")

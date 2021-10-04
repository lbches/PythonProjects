import random
import math

# taking inputs
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# generating the random number between the lower and uppper bound

randomnum = random.randint(lower, upper)
print("\n\tYou have only",
      round(math.log(upper-lower+1, 2)),
      "chances to guess the integer ! \n"
      )

# intializing the number of guesses
count = 0

# calculaton depends on ranges
while count < math.log(upper-lower+1, 2):
    count += 1
    # taking guessing number as input
    guess = int(input("Guess a number : "))

    # condition testing
    if randomnum == guess:
        print('congratulation you did it in ', count, 'try.')
        break
    elif randomnum > guess:
        print("You guessd to small !.")
    elif randomnum < guess:
        print("You guessed to high !.")

# show the output
if count >= math.log(upper-lower+1, 2):
    print(" You failed ! ")
    print("\nThe numeber is %d" % randomnum)
    print("\tbetter luck next time ")

import sys
import random
from enum import Enum
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    print(RPS(2))
    print(RPS.ROCK)
    print(RPS["ROCK"])
    print(RPS.ROCK.value)

    print("")
    playerchoice = input("Enter value .....\n1 for Rock\n2 for paper\n3 for scissors\n\n")
    player = int(playerchoice)
    if player < 1 or player >3:
        sys.exit("must be 1,2 or 3")

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("")

    print("you choose " + str(RPS(player)).replace("RPS.", ""))
    print("python choose " + str(RPS(computer)).replace("RPS.", "") + ".")
    print("")
    if player == 1 and computer == 3:
        print("player win 🎉")
    elif player == 2 and computer == 1:
        print("player win 🎉")
    elif player == 3 and computer == 2:
        print("player win 🎉")
    elif player == computer :
        print("game tied 🙌")
    else:
        print("python wins 🐍")


    playagain = input("\nPlay again? \n Y for Yes  \n Q to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\ncelebrate 🎉")
        print("Thanks \n")
        playagain = False

sys.exit("Bye 🙋‍♂️ !")
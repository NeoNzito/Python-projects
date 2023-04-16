import random

diceType = input("Qual dado você quer jogar? \n(d20, d12, d10, d8, d6, d4) \n")
diceAmout = int(input("Quantos dados você quer jogar? \n"))

diceRolls = 0
diceRollsList = ""

for diceTurns in range(1, diceAmout + 1):

    d20 = int((random.randrange(1, 20)))
    d12 = int((random.randrange(1, 12)))
    d10 = int((random.randrange(1, 10)))
    d8 = int((random.randrange(1, 8)))
    d6 = int((random.randrange(1, 6)))
    d4 = int((random.randrange(1, 4)))

    if diceType == "d20":
        diceRolls += d20
        diceRollsList += str(d20) + ", "
    elif diceType == "d12":
        diceRolls += d12
        diceRollsList += str(d12) + ", "
    elif diceType == "d10":
        diceRolls += d10
        diceRollsList += str(d10) + ", "
    elif diceType == "d8":
        diceRolls += d8
        diceRollsList += str(d8) + ", "
    elif diceType == "d6":
        diceRolls += d6
        diceRollsList += str(d6) + ", "
    elif diceType == "d4":
        diceRolls += d4
        diceRollsList += str(d4) + ", "
    else:
        print("Seus dados foram inválidos!")
        break

print(f"Seus dados foram {diceRollsList} \nAo todo somaram {diceRolls}!")
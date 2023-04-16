import random
words = ["cristiano ronaldo", "nadar", "cantar", "comer", "fome", "bater penalti"]
ammountWords = int(input("Quantas palavras deseja para jogar?\n"))
randomWords = ""

for roundOfWords in range(1, ammountWords): 
    randomNumber = int(random.randint(0, len(words)))
    indexW = words[randomNumber]
    randomWords += indexW

print(randomWords)
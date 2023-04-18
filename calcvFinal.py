print("Insira a conta aqui: \n")

class calculationAll():
    def boot():
        calculations = input()
        global opr
        opr = eval(calculations)
        print(opr)
        calculationAll.wannaLoop()
    
    def wannaLoop():
        global runAgain
        runAgainInp = input(f"Seu resultado foi: {opr}! Deseja continuar?\n\nSim\nNão\n")
        if runAgainInp == "Sim" or "S":
            runAgain = True
            calculationAll.calculationLooping()
        elif runAgainInp == "Não" or "N":
            print("Muito obrigado, volte sempre!")
        else:
            print("Muito obrigado, volte sempre!")

    def calculationLooping():
        while runAgain == True:
            calculations = input("Insira uma conta:\n\n")
            opr = eval(calculations)
            print(opr)

calculationAll.boot()

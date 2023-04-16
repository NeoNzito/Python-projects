nome, peso, altura = input("Digite seu nome, seu peso e sua altura (Separados por espaço): \n").split()
peso = float(peso)
altura = float(altura)
imc = peso/(altura*altura)

imcbom = 18.0 < imc < 24.5
imcbaixo = imc <= 18.0
imcalto = imc >= 24.5

print("Bom dia,", nome + "!" "\n", 
"Seu peso é:", str(peso) + "Kg" "\n", 
"Sua altura é:", str(altura) + "m" "\n",
"Entre 24.5 e 18.0 seu IMC está BOM!, \n",
"Abaixo de 18.0 seu IMC está BAIXO!, \n",
"Acima de 24.5 seu IMC está ALTO! \n",
"Seu IMC é:", round(imc, 2), "\n")

if (imcbom):
    print("Parabéns, seu IMC está na média!")
else:
    if (imcbaixo):
        print("Tome cuidado! Seu IMC está ABAIXO da média!")
    elif (imcalto):
        print("Tome cuidado! Seu IMC está ACIMA da média!")
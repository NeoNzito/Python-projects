print("Calculadora Python \n")

number1, sign, number2 = input("Faça sua conta com até dois números, os separando com ESPAÇOS: \n").split()
number1 = float(number1)
number2 = float(number2)

if sign == "+":
    calc = number1 + number2
elif sign == "-":
    calc = number1 - number2
elif sign == "*":
    calc = number1 * number2
elif sign == "/":
    calc = number1 / number2
elif sign == "**":
    calc = number1 ** number2

functioning = True

while functioning == True:

    looping = str(calc)
    print(calc, "\n")
    sign, number2 = input(looping).split()
    number2 = float(number2)

    if sign == "+":
        calc = calc + number2
    elif sign == "-":
        calc = calc - number2
    elif sign == "*":
        calc = calc * number2
    elif sign == "/":
        calc = calc / number2
    elif sign == "**":
        calc = calc ** number2
    elif (sign == "Não"):
        functioning = False

else:
    print("Muito obrigado!")
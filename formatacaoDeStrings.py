print("RS {:07.2f}".format(34.5), "\n")
#0 - o que deverá ser preenchido, por padrão será um espaço vazio
#7 - quantos caracters deverá ter na variavel
#.2 - quantas casas depois da vírgula deverá ter
#f - qual o tipo do valor que deverá ser atribuido àquele espaço, neste caso float
print("RS {:7d}".format(4), "\n") 
#d - digital, ou número inteiro

dia, mes, ano = input("Digite uma data separado por barras: ").split("/")
print("Data {:2s}/{:2s}/{:4s}".format(dia, mes, ano))

nome = input("Digite seu nome: ")
print(f"Seu nome é {nome}")
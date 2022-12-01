#top 10 calculadoras
entrada = input("qual operacao voce quer ")

#valor ta em int pra fazer op matematica
valor1 = int(input("valor 1 "))
valor2 = int(input("valor 2 "))

if entrada == "multiplicar":

    total = valor1 * valor2

elif entrada == "somar":

    total = valor1 + valor2

elif entrada =="subtrair":

    total = valor1 - valor2 

elif entrada =="dividir":

    total = valor1/valor2

#int pra string
totalstr = str(total)

print("O valor é " + totalstr) 
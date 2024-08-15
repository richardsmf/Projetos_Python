number_1 = int(input("Digite um número"))
number_2 = int(input("Digite outro número"))

operacao = input ('''Digite qual é a operação pretendida:
+ para soma
- para subtração
* para multiplicação
/ para divisão
''')

if operacao == "+":
    print ("A resposta é: ", number_1 + number_2,)

if operacao == "-":
    print("A resposta é: ", number_1 - number_2,)

elif operacao == "*":
    print("A resposta é: ", number_1 * number_2,)

else:
    print("A resposta é: ", number_1 / number_2,)
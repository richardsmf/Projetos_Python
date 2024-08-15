shop = int (input ("Digite o valor da sua conta em R$"))

desconto = 200 * 0.20

DescApli = shop - desconto

if shop < 200:
    print ("Você não recebe um desconto de 20%")

if shop >= 200:
    print (f"Parabéns, você ganhou um desconto , por isso você pagará", DescApli,)
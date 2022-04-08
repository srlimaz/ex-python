assinatura = input("Qual a sua assinatura ? A resposta deve ser toda em letra minúscula (basic, silver, gold, platinum) ")
fat_anual = float(input("Qual seu faturamento anual ? "))
resultado = float

if assinatura == "basic":
    resultado = fat_anual * 0.3
    print("Sua assinatura BASIC representa um cobrança de 30 porcento do seu faturamento, e o valor a pagar é de R$" + str(resultado))
elif assinatura == "silver":
    resultado = fat_anual * 0.2
    print("Sua assinatura SILVER representa um cobrança de 20 porcento do seu faturamento, e o valor a pagar é de R$" + str(resultado))
elif assinatura == "gold":
    resultado = fat_anual * 0.1
    print("Sua assinatura GOLD representa um cobrança de 10 porcento do seu faturamento, e o valor a pagar é de R$" + str(resultado))
elif assinatura == "platinum":
    resultado = fat_anual * 0.05
    print("Sua assinatura PLATINUM representa um cobrança de 5 porcento do seu faturamento, e o valor a pagar é de R$" + str(resultado))
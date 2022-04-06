valor_bruto = float(input("Qual o valor do pacote ? "))
cat_assento = input("Qual a categoria do assento ? (Responda 'eco' para ECONOMICA, 'ex' para EXECUTIVA e 'pc' para PRIMEIRA CLASSE) ")
quant_viajantes = float(input("Quantas pessoas irão viajar ? "))
desconto = 0
economico = False
executivo = False
p_classe = False

if cat_assento == "eco":
    economico = True
elif cat_assento == "ex":
    executivo = True
elif cat_assento == "pc":
    p_classe = True

liquido = valor_bruto - desconto
medio = liquido / quant_viajantes

if quant_viajantes < 2 and economico == True:
    desconto = 0
    print("A sua viagem na classe economica no valor de R$" + str(valor_bruto) + ", não obteve um desconto, fazendo com que o valor da viagem não sofresse alteração (R$" + str(liquido) + "), e o valor médio por viajante é de R$" + str(medio))
elif quant_viajantes == 2 and economico == True:
    desconto = valor_bruto * 0.03
    print("A sua viagem na classe economica no valor de R$" + str(valor_bruto) + ", obteve um desconto de R$" + str(desconto) + ", fazendo que sua viagem custasse apenas R$" + str(liquido) + ", e o valor médio por viajante é de R$" + str(medio))
elif quant_viajantes == 3 and economico == True:
    desconto = valor_bruto * 0.04
    print("A sua viagem na classe economica no valor de R$" + str(valor_bruto) + ", obteve um desconto de R$" + str(desconto) + ", fazendo que sua viagem custasse apenas R$" + str(liquido) + ", e o valor médio por viajante é de R$" + str(medio))
elif quant_viajantes >= 4 and economico == True:
    desconto = valor_bruto * 0.05
    print("A sua viagem na classe economica no valor de R$" + str(valor_bruto) + ", obteve um desconto de R$" + str(desconto) + ", fazendo que sua viagem custasse apenas R$" + str(liquido) + ", e o valor médio por viajante é de R$" + str(medio))

elif quant_viajantes < 2 and executivo == True:
    desconto = 0
    print("A sua viagem na classe executiva no valor de R$" + str(valor_bruto) + ", não obteve um desconto, fazendo com que o valor da viagem não sofresse alteração (R$" + str(liquido) + "), e o valor médio por viajante é de R$" + str(medio))
elif quant_viajantes == 2 and executivo == True:
    desconto = valor_bruto * 0.05
    print("A sua viagem na classe executiva no valor de R$" + str(valor_bruto) + ", obteve um desconto de R$" + str(desconto) + ", fazendo que sua viagem custasse apenas R$" + str(liquido) + ", e o valor médio por viajante é de R$" + str(medio))
elif quant_viajantes == 3 and executivo == True:
    desconto = valor_bruto * 0.07
    print("A sua viagem na classe executiva no valor de R$" + str(valor_bruto) + ", obteve um desconto de R$" + str(desconto) + ", fazendo que sua viagem custasse apenas R$" + str(liquido) + ", e o valor médio por viajante é de R$" + str(medio))
elif quant_viajantes >= 4 and executivo == True:
    desconto = valor_bruto * 0.08
    print("A sua viagem na classe executiva no valor de R$" + str(valor_bruto) + ", obteve um desconto de R$" + str(desconto) + ", fazendo que sua viagem custasse apenas R$" + str(liquido) + ", e o valor médio por viajante é de R$" + str(medio))

elif quant_viajantes < 2 and p_classe == True:
    desconto = 0
    print("A sua viagem na primeira classe no valor de R$" + str(valor_bruto) + ", não obteve um desconto, fazendo com que o valor da viagem não sofresse alteração (R$" + str(liquido) + "), e o valor médio por viajante é de R$" + str(medio))
elif quant_viajantes == 2 and p_classe == True:
    desconto = valor_bruto * 0.10
    print("A sua viagem na primeira classe no valor de R$" + str(valor_bruto) + ", obteve um desconto de R$" + str(desconto) + ", fazendo que sua viagem custasse apenas R$" + str(liquido) + ", e o valor médio por viajante é de R$" + str(medio))
elif quant_viajantes == 3 and p_classe == True:
    desconto = valor_bruto * 0.15
    print("A sua viagem na primeira classe no valor de R$" + str(valor_bruto) + ", obteve um desconto de R$" + str(desconto) + ", fazendo que sua viagem custasse apenas R$" + str(liquido) + ", e o valor médio por viajante é de R$" + str(medio))
elif quant_viajantes >= 4 and p_classe == True:
    desconto = valor_bruto * 0.20
    print("A sua viagem na primeira classe no valor de R$" + str(valor_bruto) + ", obteve um desconto de R$" + str(desconto) + ", fazendo que sua viagem custasse apenas R$" + str(liquido) + ", e o valor médio por viajante é de R$" + str(medio))




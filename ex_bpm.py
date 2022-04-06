idade = float(input("Informe sua idade: "))
crianca = 0
adolescente = 0 
adulto = 0
idoso = 0

if idade <= 2:
    crianca = True
else:
    crianca = False

if idade > 2 and idade <= 17:
    adolescente = True
else:
    adolescente = False

if idade >= 18 and idade <= 60:
    adulto = True
else:
    adulto = False

if idade > 60:
    idoso = True
else:
    idoso = False

bpm = int(input("Informe o seu número de BATIMENTOS POR MINUTO (BPM): "))

if crianca == True:
    if bpm >=120 and bpm <= 140:
        print("A criança encontra-se DENTRO da faixa adequada!")
    else:
        if bpm <120:
            print("A criança encontra-se ABAIXO da faixa adequada!")
        else:
            print("A criança encontra-se ACIMA da faixa adequada!")

elif adolescente == True:
    if bpm >=80 and bpm <= 100:
        print("O Adolescente encontra-se DENTRO da faixa adequada!")
    elif bpm <80:
        print("O Adolescente encontra-se ABAIXO da faixa adequada!")
    elif bpm >100:
        print("O Adolescente encontra-se ACIMA da faixa adequada!")

elif adulto == True:
    if bpm >=70 and bpm <= 80:
        print("O adulto encontra-se DENTRO da faixa adequada!")
    elif bpm <70:
        print("O adulto encontra-se ABAIXO da faixa adequada!")
    elif bpm >80:
        print("O adulto encontra-se ACIMA da faixa adequada!")

elif idoso == True:
    if bpm >=50 and bpm <= 60:
        print("O idoso encontra-se DENTRO da faixa adequada!")
    elif bpm <50:
        print("O idoso encontra-se ABAIXO da faixa adequada!")
    elif bpm >60:
        print("O idoso encontra-se ACIMA da faixa adequada!")
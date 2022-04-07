segunda = int(input("Quantos votos segunda-feira recebeu ? "))
terca = int(input("Quantos votos terça-feira recebeu ? "))
quarta = int(input("Quantos votos quarta-feira recebeu ? "))
quinta = int(input("Quantos votos quinta-feira recebeu ? "))
sexta = int(input("Quantos votos sexta-feira recebeu ? "))

if segunda > terca or segunda > quarta or segunda > quinta or segunda > sexta:
    print("Segunda foi o dia mais votado!")
elif terca > segunda or terca > quarta or terca > quinta or terca > sexta:
    print("Terça foi o dia mais votado!")
elif quarta > terca or quarta > segunda or quarta > quinta or quarta > sexta:
    print("Quarta foi o dia mais votado!")
elif quinta > terca or quinta > quarta or quinta > quinta or quinta > sexta:
    print("Quinta foi o dia mais votado!")
elif sexta > terca or sexta > quarta or sexta > quinta or sexta > sexta:
    print("Sexta foi o dia mais votado!")

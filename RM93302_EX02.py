segunda = int(input("Quantos votos segunda-feira recebeu ? "))
terca = int(input("Quantos votos terça-feira recebeu ? "))
quarta = int(input("Quantos votos quarta-feira recebeu ? "))
quinta = int(input("Quantos votos quinta-feira recebeu ? "))
sexta = int(input("Quantos votos sexta-feira recebeu ? "))

resultado = 0

if segunda > terca or segunda > quarta or segunda > quinta or segunda > sexta:
    resultado = "Segunda foi o dia mais votado!"
if terca > segunda or terca > quarta or terca > quinta or terca > sexta:
    resultado = "Terça foi o dia mais votado!"
if quarta > terca or quarta > segunda or quarta > quinta or quarta > sexta:
    resultado = "Quarta foi o dia mais votado!"
if quinta > terca or quinta > quarta or quinta > quinta or quinta > sexta:
    resultado = "Quinta foi o dia mais votado!"
if sexta > terca or sexta > quarta or sexta > quinta or sexta > sexta:
    resultado = "Sexta foi o dia mais votado!"

print(resultado)



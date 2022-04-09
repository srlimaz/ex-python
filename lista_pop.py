#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#Removendo o último valor inserido na lista
jedi.pop()
#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)
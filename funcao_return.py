#Função que calcula a velocidade média
def calcularVelocidadeMedia(distancia, tempo):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    return velocidade_media
#aqui começa o programa principal
dist = float(input("Informe a distância"))
temp = float(input("Informe o tempo"))
#chamando a função com valores definidos pelo usuário
print("A velocidade média é {} km/h".format(calcularVelocidadeMedia(dist, temp)))
numero = int(input("Digite os minutos do seu computador: ") )

resultado=1
for n in range(1,numero+1):
    resultado = resultado * n

senha = "LIBERDADE" + str(resultado)

print("A senha para desbloquear é: " + str(senha))
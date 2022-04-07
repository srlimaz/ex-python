soma_impar = 0
soma1 = 1
for impar in range (1,50,2):
    nota_impar = int(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPAR, POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO " + str(soma1) + ": "))
    soma_impar = soma_impar + nota_impar
    int(soma1)
    soma1 = soma1 + 2

soma_par = 0
soma2 = 2 
for par in range (2,51,2):
    nota_par = int(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PAR, POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO " + str(soma2) + ": "))
    soma_par = soma_par + nota_par
    int(soma2)
    soma2 = soma2 + 2

media_impar = soma_impar / 25
media_par = soma_par / 25
print("A média dos alunos impar foi: " + str(media_impar) + ". E a média dos alunos par foi: " + str(media_par) + ".")

if media_impar > media_par:
    print("A turma impar obteve a maior nota comparado com a turma par.")
else:
    print("A turma par obteve a maior nota comparado com a turma impar")
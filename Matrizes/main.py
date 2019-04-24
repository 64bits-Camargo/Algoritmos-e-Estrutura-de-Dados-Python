import os


clear = lambda : os.system('clear')         # Utilizando o Lambda, para criar uma função para limpar a tela.

notas = []                                  # Um vetor que receberá outrs vetores dentro, e nesse conjunto forma uma matriz.

# Loop para receber as notas do aluno.
count = 0   
while count < 2:
    clear()
    nome = str(input("Nome do aluno: "))
    notas.append([nome])                    # adiciona um vetor como primeiro elemento o nome do aluno, dentro do vetor notas.
    
    for i in range(2):
        nota = float(input("Nota: "))
        notas[count].append(nota)           # adiciona a nota do aluno, conforme o valor da variavel count.
    
    count += 1                              # incrementa a variavel, e passa novamento no loop.
    
# Imprimi a matriz, colunas e linhas.
clear()
for linha in notas:
    for coluna in linha:
        print(str(coluna) + '\t', end = ' ')
    print('')
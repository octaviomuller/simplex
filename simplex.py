file = open('exemplo.txt', 'r') #Rotina de leitura do arquivo
table = []
for line in file:
    line = line.replace('\n', '').split(' ')
    for i in range(len(line)):
        line[i] = int(line[i]) # Transformar o vetor de strings em um vetor de números
    table.append(line) #Adiciona a linha no vetor, formando uma matriz

matrix = []

b = table[1].pop()
table[1].extend([1, 0, 0])
table[1].append(b)
matrix.append(table[1])


b = table[2].pop()
table[2].extend([0, 1, 0])
table[2].append(b)
matrix.append(table[2])

b = table[3].pop()
table[3].extend([0, 0, 1])
table[3].append(b)
matrix.append(table[3])

for line in matrix:
    print(line)
    print('\n')

file.close()
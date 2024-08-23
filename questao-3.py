numerosPares = []
quadradoPerfeito = []
i = int(input())
j = int(input())
k = int(input())
contador = 2
numbersList = [j, k]

while contador < i:
    nextNumber = int(numbersList[-1] + int(numbersList[-2]))
    numbersList.append(nextNumber)

    contador += 1


print(numbersList)



for i in range(len(numbersList)):
    if numbersList[i] % 2 == 0:
        numerosPares.append(numbersList[i])

if len(numerosPares) == 0:
    print(f'Não há elementos pares na sequência até a posição {i}')
else:
    print(f'Os elementos pares da sequência são: {numerosPares}')


for i in range(len(numerosPares)):
    raizQuadrada = int((numerosPares[i]) ** (1/2))
    if (raizQuadrada ** 2) == (numerosPares[i]):
        quadradoPerfeito.append(numerosPares[i])


if len(quadradoPerfeito) == 0:
    print('Não há elemento par quadrado perfeito')
else:
    print(f'Dentre esses, os que são quadrados perfeitos são: {quadradoPerfeito}')




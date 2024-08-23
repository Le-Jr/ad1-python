# Variáveis
numbers = []
primos = []

# Subprogramas
def main():
    converteInteiro()

def converteInteiro():
    for i in range(len(listaInteiros)):
        number = int(listaInteiros[i])
        numbers.append(number)
    soma = somaInteiros(numbers)
    print(f'A soma da sequência {numbers} é: {soma}')
    numerosPrimos()

def somaInteiros(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + somaInteiros(numbers[1:])

def numerosPrimos():
    for n in range(len(numbers)):
        if numbers[n] > 1:
            ehPrimo = True
            if numbers[n] == 2:
                primos.append(numbers[n])
                continue
            if numbers[n] % 2 == 0:
                ehPrimo = False
            for i in range(3, int(numbers[n]**0.5) + 1, 2):
                if numbers[n] % i == 0:
                    ehPrimo = False
                    break
            if ehPrimo:
                primos.append(numbers[n])
    if primos:
        print(f'Os números primos na sequência {numbers} são: {primos}')
    else:
        print(f'Não há elementos primos na sequência {numbers}')

# Programa Principal
print('Escreva aqui sua sequência de inteiros:\n')
listaInteiros = input().split()

# Chamada Função principal
main()

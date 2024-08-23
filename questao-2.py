#Variaveis Escopo Global
numbers = []
i = 0

def adicionaNumero():
    inputUser = str(input('Digite um número inteiro: '))
    try:
        number = int(inputUser)
        numbers.append(number)
        print('Número adicionado com sucesso!')
    except ValueError:
        print('Valor não é do tipo inteiro, tente novamente!')

def visuNumeros():
    print(f'Números na lista:{numbers}')

def calculaMedia():
    valorLista = float(len(numbers))
    media = float(sum(numbers) / valorLista)
    print(f'A media dos números é igual a {media:.2f}')

def calculaSoma():
    soma = int(sum(numbers))
    print(f'A soma dos números é igual a {soma}')


while i < 1:
    print('1. Adicionar Número')
    print('2. Visualizar Números')
    print('3. Calcular Média')
    print('4. Calcular Soma')
    print('5. Sair')
    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:
        adicionaNumero()
    elif escolha == 2:
        visuNumeros()
    elif escolha == 3:
        calculaMedia()
    elif escolha == 4:
        calculaSoma()
    elif escolha == 5:
        i += 1


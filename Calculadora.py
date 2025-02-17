2# Definindo função para soma
def somar(x, y):
    return x + y

# Função para subtração
def subtrair(x, y):
    return x - y

# Função para multiplicação
def multiplicar(x, y):
    return x * y

# Função para dividir
def dividir(x, y):
    if y == 0:
        return "Erro! Não é possível dividir por zero."
    else:
        return x / y

# Função principal para executar a calculadora
def calculadora():
    while True: # Cria um loop para repetir a calculadora sem que o programa se encerre.
     print("Selecione a operação:")
     print("1. Somar")
     print("2. Subtrair")
     print("3. Multiplicar")
     print("4. Dividir")

    # Pede ao usuário para escolher uma operação
     escolha = input("Digite o número da operação (1/2/3/4): ")

    # Pede os números para o cálculo
     num1 = float(input("Digite o primeiro número: "))
     num2 = float(input("Digite o segundo número: "))

    # Verifica a operação e chama a função correspondente
     if escolha == '1':
        print(f"{num1} + {num2} = {somar(num1, num2)}")
     elif escolha == '2':
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
     elif escolha == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
     elif escolha == '4':
        print(f"{num1} / {num2} = {dividir(num1, num2)}")
     else:
        print("Opção inválida!")

# Chama a função da calculadora para iniciar um novo cálculo sem que o programa se encerre após o resultado.
calculadora()

# Importa as bibliotecas necessárias
import math

# Define as funções matemáticas básicas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

# Define a função principal
def main():
    # Obtém os valores dos operandos
    a = float(input("Digite o primeiro operando: "))
    b = float(input("Digite o segundo operando: "))

    # Exibe o menu de operações
    print("Operações disponíveis:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    # Obtém a operação escolhida pelo usuário
    operacao = int(input("Escolha uma operação: "))

    # Realiza a operação escolhida
    if operacao == 1:
        resultado = soma(a, b)
    elif operacao == 2:
        resultado = subtracao(a, b)
    elif operacao == 3:
        resultado = multiplicacao(a, b)
    elif operacao == 4:
        resultado = divisao(a, b)
    else:
        print("Operação inválida.")
        return

    # Exibe o resultado
    print("Resultado:", resultado)

# Chama a função principal
main()

import random

def obter_escolha_usuario():
    """Obtém a escolha do usuário."""
    escolha = input("Escolha pedra, papel ou tesoura: ").lower()
    while escolha not in ["pedra", "papel", "tesoura"]:
        print("Escolha inválida. Tente novamente.")
        escolha = input("Escolha pedra, papel ou tesoura: ").lower()
    return escolha

def obter_escolha_computador():
    """Obtém a escolha aleatória do computador."""
    opcoes = ["pedra", "papel", "tesoura"]
    return random.choice(opcoes)

def determinar_vencedor(escolha_usuario, escolha_computador):
    """Determina o vencedor do jogo."""
    if escolha_usuario == escolha_computador:
        return "Empate!"
    elif (
        (escolha_usuario == "pedra" and escolha_computador == "tesoura") or
        (escolha_usuario == "papel" and escolha_computador == "pedra") or
        (escolha_usuario == "tesoura" and escolha_computador == "papel")
    ):
        return "Você venceu!"
    else:
        return "O computador venceu!"

def jogar():
    """Função principal para executar o jogo."""
    escolha_usuario = obter_escolha_usuario()
    escolha_computador = obter_escolha_computador()

    print(f"Você escolheu: {escolha_usuario}")
    print(f"O computador escolheu: {escolha_computador}")

    resultado = determinar_vencedor(escolha_usuario, escolha_computador)
    print(resultado)

jogar()

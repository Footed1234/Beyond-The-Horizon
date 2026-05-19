from core.game_state import GameState
from entities.player import Player

def novo_jogo():
    game_state = GameState()

    nome = input("Digite seu nome: ")

    print("Classes: ")
    print("1. Guerreiro")
    print("2. Mago")
    print("3. Ladino")

    classe = input("Escolha sua classe: ")

    if classe in ["1", "2", "3"]:
        if classe == "1":
            classe = "guerreiro"
        if classe == "2":
            classe = "mago"
        if classe == "3":
            classe = "ladino"
    
    player = Player(nome, classe)

    game_state.player = player

    return game_state
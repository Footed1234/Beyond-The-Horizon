import os

def estatísticas_player(game_state):
    player = game_state.player

    print(player.nome)
    print(f"HP: {player.hp}/{player.hp_max}")
    
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
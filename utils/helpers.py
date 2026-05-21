def estatísticas_player(game_state):
    player = game_state.player

    print(player.nome)
    print(f"HP: {player.hp}/{player.hp_max}")
    
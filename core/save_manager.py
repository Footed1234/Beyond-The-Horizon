import json

def salvar_jogo(game_state):
    player = game_state.player

    dados = {
        "player": {
            "nome": player.nome,
            "classe": player.classe,
            "nivel": player.nivel,
            "xp": player.xp,
            "hp": player.hp,
            "hp_max": player.hp_max,
            "recurso": player.recurso,
            "recurso_max": player.recurso_max,
            "recurso_gasto": player.recurso_gasto,
            "forca": player.forca,
            "defesa": player.defesa,
            "moedas": player.moedas,
            "inventario": player.inventario,
            "arma": player.arma,
            "armadura": player.armadura,
            "quests": player.quests
        },
        "position": game_state.position,
        "dungeons": {
            f"{x},{y}": dungeon_id for (x, y), dungeon_id in game_state.dungeons.items()
        }
    }

    with open("save.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        print("\nJogo Salvo!")

def carregar_jogo():
    from core.game_state import GameState
    from entities.player import Player

    try:
        with open("save.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        print("\nNenhum save encontrado")
        return None
    
    game_state = GameState()

    player_data = dados["player"]

    player = Player(player_data["nome"], player_data["classe"])

    # Stats
    player.nivel = player_data["nivel"]
    player.xp = player_data["xp"]
    player.hp = player_data["hp"]
    player.hp_max = player_data["hp_max"]
    player.recurso = player_data["recurso"]
    player.recurso_max = player_data["recurso_max"]
    player.recurso_gasto = player_data["recurso_gasto"]
    player.forca = player_data["forca"]
    player.defesa = player_data["defesa"]
    player.moedas = player_data["moedas"]

    # Inventário
    player.inventario = player_data["inventario"]

    # Equipamentos
    player.arma = player_data["arma"]
    player.armadura = player_data["armadura"]

    # Quests
    player.quests = player_data["quests"]

    game_state.player = player

    # Posição
    game_state.position = dados["position"]

    # Dungeons
    game_state.dungeons = {
        tuple(map(int, chave.split(","))): valor

        for chave, valor in dados ["dungeons"].items()
    }

    print("\nSave Carregado")

    return game_state
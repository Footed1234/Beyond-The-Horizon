import random
from data.dungeons import DUNGEONS
from data.world_map import WORLD_MAP

def gerar_dungeons(game_state):
    dungeon_ids = list(DUNGEONS.keys())

    quantidade = 5

    while len(game_state.dungeons) < quantidade:
        x = random.randint(0, 9)
        y = random.randint(0, 5)

        tile = WORLD_MAP[y][x]

        # Não pode ser cidade
        if tile["tipo"] == "cidade":
            continue

        posicao = (x, y)

        # Evita sobreposição
        if posicao in game_state.dungeons:
            continue

        dungeon_id = random.choice(dungeon_ids)

        game_state.dungeons[posicao] = dungeon_id

def obter_dungeon_atual(game_state):
    posicao = tuple(game_state.position)

    return game_state.dungeons.get(posicao)

def entrar_na_dungeon(game_state):
    dungeon_id = obter_dungeon_atual(game_state)

    if not dungeon_id:
        return
    
    dungeon = DUNGEONS[dungeon_id]

    print("\n====================")
    print(dungeon["nome"])
    print("====================")
    print(f"Dificuldade: {dungeon['dificuldade']}")
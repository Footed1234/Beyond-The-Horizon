from data.world_map import WORLD_MAP
from systems.dungeon_system import obter_dungeon_atual

def obter_tile(x, y):
    return WORLD_MAP[y][x]

def mover_player(game_state, direcao):
    x, y = game_state.position

    if direcao == "w":
        y -= 1

    elif direcao == "s":
        y += 1
    
    elif direcao == "a":
        x -= 1

    elif direcao == "d":
        x += 1

    else:
        return False
    
    # Limites do mapa
    if x < 0 or y < 0:
        return False
    
    if y >= len(WORLD_MAP):
        return False
    
    if x >= len(WORLD_MAP[y]):
        return False
    
    game_state.position = [x, y]

    return True

def mostrar_local_atual(game_state):
    x, y = game_state.position

    tile = obter_tile(x, y)

    print("\n====================")
    print(f"Posição: {x}, {y}")
    if tile["tipo"] == "cidade":
        print(f"Cidade de {tile["cidade"]}")
    else: 
        print(f"Região: {tile["tipo"]}")
    print("====================")

    dungeon_id = obter_dungeon_atual(game_state)

    if dungeon_id:
        print("\nDungeons serão implementadas")
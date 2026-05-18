from data.cities import CITIES

def obter_cidade_atual(game_state):
    from systems.world_system import obter_tile

    x, y = game_state.position

    tile = obter_tile(x, y)

    if tile["tipo"] == "cidade":
        return tile["cidade"]
    
    return None

def entrar_na_cidade(game_state):
    nome_cidade = obter_cidade_atual(game_state)

    if not nome_cidade:
        return
    
    cidade = CITIES[nome_cidade]

    print("\n====================")
    print(f"{nome_cidade}")
    print(cidade["descricao"])
    print("====================")

def menu_cidade(game_state):
    nome_cidade = obter_cidade_atual(game_state)

    if not nome_cidade:
        return
    
    cidade = CITIES[nome_cidade]

    while True:
        print(f"\n===== {nome_cidade} =====")

        print("1. Descansar")

        if cidade["loja"]:
            print("2. Loja")

        if cidade["ferreiro"]:
            print("3. Ferreiro")

        print("0. Sair da Cidade")

        escolha = input("> ")

        if escolha == "0":
            break

        elif escolha == "1":
            player = game_state.player

            player.hp = player.hp_max
            player.recurso = player.recurso_max

            print("\nVocê descansou!")
        
        elif escolha == "2" and cidade["loja"]:
            print("\nLoja será implementada")
        
        elif escolha == "3" and cidade["ferreiro"]:
            print("\nFerreiro será implementado")


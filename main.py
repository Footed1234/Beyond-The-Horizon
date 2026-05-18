from core.game_state import GameState
from entities.player import Player
from entities.enemy import Enemy
from systems.combat_system import iniciar_combate
from systems.inventory_system import adicionar_item, remover_item, mostrar_inventario
from systems.item_system import equipar_item, mostrar_equipamento
from systems.world_system import mover_player, mostrar_local_atual
from systems.city_system import obter_cidade_atual, menu_cidade
from systems.quest_system import aceitar_quest, mostrar_quests
from systems.dungeon_system import gerar_dungeons, entrar_na_dungeon, obter_dungeon_atual
from core.save_manager import salvar_jogo, carregar_jogo


while True:
    print("1. Novo jogo")
    print("2. Carregar Jogo")

    escolha = input("> ")

    if escolha == "1":
        game_state = GameState()

        dungeons = gerar_dungeons(game_state)

        nome = input("Digite seu nome: ")

        classe = input("Digite sua classe: ")

        player = Player(nome, classe)

        game_state.player = player

        gerar_dungeons(game_state)

        print("1. Salvar")

        comando = input("> ")

        if comando == "1":
            salvar_jogo(game_state)

    elif escolha == "2":
        game_state = carregar_jogo()

        if not game_state:
            game_state = GameState()
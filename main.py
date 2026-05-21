import random
from core.game_state import GameState
from core.save_manager import salvar_jogo, carregar_jogo
from core.new_game import novo_jogo
from entities.player import Player
from entities.enemy import Enemy
from systems.combat_system import iniciar_combate, verificar_combate
from systems.inventory_system import adicionar_item, remover_item, mostrar_inventario
from systems.item_system import equipar_item, mostrar_equipamento
from systems.world_system import mover_player, mostrar_local_atual
from systems.city_system import obter_cidade_atual, entrar_na_cidade, menu_cidade
from systems.quest_system import aceitar_quest, mostrar_quests
from systems.dungeon_system import gerar_dungeons, entrar_na_dungeon, obter_dungeon_atual
from data.enemies import ENEMIES
from utils.helpers import estatísticas_player


def iniciar_jogo(game_state):
    while game_state.running:
        cidade = obter_cidade_atual(game_state)
        dungeon = obter_dungeon_atual(game_state)

        print("Mapa Placeholder")
        mostrar_local_atual(game_state)
        estatísticas_player(game_state)
        print("C. Configurações")
        print("I. Inventário")
        if cidade or dungeon:
            print("E. Interagir")
        print("W. Norte")
        print("A. Oeste")
        print("S. Sul")
        print("D. Leste")

        comando = input("> ").lower()

        if comando in ["w", "a", "s", "d"]:
            moveu = mover_player(game_state, comando)
            if moveu:
                if verificar_combate():
                    enemy_id = random.choice(list(ENEMIES.keys()))
                    inimigo = Enemy(enemy_id)
                    iniciar_combate(game_state.player, inimigo)
        elif comando == "i":
            mostrar_inventario(game_state.player)
        elif comando == "c":
            print("0. Salvar")
            print("1. Salvar e Sair")
            print("2. Sair sem Salvar")

            escolha = input("> ")

            if escolha in ["0", "1", "2"]:
                if escolha == "0":
                    salvar_jogo(game_state)
                if escolha == "1":
                    salvar_jogo(game_state)
                    game_state.running = False
                if escolha == "2":
                    game_state.running = False
            else:
                print("Opção inválida!")
                input()
        elif comando == "e":
            if cidade:
                entrar_na_cidade(game_state)
            elif dungeon:
                entrar_na_dungeon(game_state)


def main():
    print("1. Novo Jogo")
    print("2. Carregar Jogo")

    escolha = input("> ")

    if escolha == "1":
        game_state = novo_jogo()
        
        gerar_dungeons(game_state)

        iniciar_jogo(game_state)

    if escolha == "2":
        game_state = carregar_jogo()

        iniciar_jogo(game_state)


if __name__ == "__main__":
    main()
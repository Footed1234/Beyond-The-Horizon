import random
from core.game_state import GameState
from core.save_manager import salvar_jogo, carregar_jogo
from core.new_game import novo_jogo
from entities.player import Player
from entities.enemy import Enemy
from systems.combat_system import iniciar_combate, achar_combate
from systems.inventory_system import adicionar_item, remover_item, mostrar_inventario
from systems.item_system import equipar_item, mostrar_equipamento
from systems.world_system import mover_player, mostrar_local_atual
from systems.city_system import obter_cidade_atual, entrar_na_cidade, menu_cidade
from systems.quest_system import aceitar_quest, mostrar_quests
from systems.dungeon_system import gerar_dungeons, entrar_na_dungeon, obter_dungeon_atual
from data.enemies import ENEMIES
from utils.helpers import estatísticas_player, limpar_tela
from ui.main_screen import exibir_tela_inicial


def iniciar_jogo(game_state):
    # Enquanto o player está jogando
    while game_state.running:
        # Verifica se está numa cidade
        cidade = obter_cidade_atual(game_state)
        # Verifica se está numa dungeon
        dungeon = obter_dungeon_atual(game_state)

        limpar_tela()
        # Menu principal do game_loop
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
                if achar_combate():
                    # Pega um inimigo da lista de inimigos
                    enemy_id = random.choice(list(ENEMIES.keys()))
                    inimigo = Enemy(enemy_id)
                    iniciar_combate(game_state, inimigo)
        elif comando == "i":
            mostrar_inventario(game_state.player)
        elif comando == "c":
            print("0. Salvar")
            print("1. Salvar e Sair")
            print("2. Sair sem Salvar")

            escolha = input("> ")

            if escolha in ["0", "1", "2"]:
                if escolha == "0":
                    # Fica no jogo e salva os stats do game_state
                    salvar_jogo(game_state)
                if escolha == "1":
                    # Salva os stats do game_state e sai do jogo
                    salvar_jogo(game_state)
                    game_state.running = False
                if escolha == "2":
                    # Sai do jogo sem salvar os stats do game_state
                    game_state.running = False
            else:
                print("Opção inválida!")
                input()
        elif comando == "e":
            # Se o player está numa cidade
            if cidade:
                entrar_na_cidade(game_state)
            # Se o player está numa dungeon
            elif dungeon:
                entrar_na_dungeon(game_state)


def main():
    tela_inicial = True
    # Enquanto o player está na tela principal do jogo
    while tela_inicial:
        limpar_tela()
        exibir_tela_inicial()

        escolha = input("> ")

        # Novo jogo
        if escolha == "1":
            tela_inicial = False

            # Cria o game_state pela função novo_jogo()
            game_state = novo_jogo()
            
            # Gera as dungeons daquele game e salva no game_state
            gerar_dungeons(game_state)

            # Inicia o loop principal do jogo
            iniciar_jogo(game_state)

        # carregar jogo
        if escolha == "2":
            tela_inicial = False

            # Cria o game_state, puxando os dados do save.json pela função carregar_jogo()
            game_state = carregar_jogo()

            # Inicia o loop principal do jogo
            iniciar_jogo(game_state)


if __name__ == "__main__":
    main()
from systems.quest_system import atualizar_progresso
from utils.helpers import limpar_tela
import random


# Verifica se o player vai achar um monstro naquele tile
def achar_combate():
    chance = random.randint(1, 100)
    if chance <= 30:
        return True
    return False

def iniciar_combate(game_state, enemy):
    batalha = True
    player = game_state.player
    player_defesa_max = player.defesa
    player_recurso_max = player.recurso
    enemy_hp_max = enemy.hp
    
    limpar_tela()
    print(f"{player.nome} se depara com um {enemy.nome}")
    input("> ")
    
    # Enquanto o player e o inimigo estão vivos e a batalha está acontecendo, entra no loop principal do combate
    while player.esta_vivo() and enemy.esta_vivo() and batalha:
        limpar_tela()

        # Se o player não está em recuperação e o recurso atual dele é menor do que ele vai gastar
        if not player.esta_em_recuperacao() and player.recurso < player.recurso_gasto:
            # Inicia a recuperação por 5 turnos
            player.iniciar_recuperacao()
            print(f"\n{player.nome} não tem recurso suficiente e entra em recuperação por {player.recuperacao_turnos} turnos!")
            input("> ")
            limpar_tela()

        # Mostra o loop principal da batalha
        print(f"{player.nome} enfrenta um {enemy.nome}!")
        print(f"{enemy.nome}: HP {enemy.hp}/{enemy_hp_max} | Força {enemy.forca} | Defesa {enemy.defesa}")
        print(f"{player.nome}: HP {player.hp}/{player.hp_max} | Força {player.forca} | {player.recurso_nome}: {player.recurso}/{player_recurso_max} | Defesa {player.defesa}")
        if player.esta_em_recuperacao():
            print(f"=== EM RECUPERAÇÃO: {player.recuperacao_turnos} turno(s) restantes ===\n")
        print("Escolha uma ação")
        print("1- Atacar")
        print("2- Usar item")
        print("3- Fugir")
        comando = input("> ").strip()

        if comando == "1":
            if player.esta_em_recuperacao():
                print("\nVocê está em recuperação e não pode atacar.")
            elif player.recurso >= player.recurso_gasto:
                dano_defesa, dano_hp, bool_dano_hp = enemy.receber_dano(player.forca)
                # Se o player deu dano apenas na defesa
                if dano_defesa > 0 and not bool_dano_hp:
                    print(f"\n{player.nome} causou {dano_defesa} de dano na Defesa de {enemy.nome}!")
                # Se o player deu dano na defesa e HP
                elif bool_dano_hp and dano_defesa > 0:
                    print(f"\n{player.nome} causou {dano_defesa} de dano na Defesa de {enemy.nome}!")
                    print(f"{player.nome} causou {dano_hp} de dano no HP de {enemy.nome}!")
                # Se o player deu dano apenas no HP
                elif bool_dano_hp:
                    print(f"\n{player.nome} causou {dano_hp} de dano no HP de {enemy.nome}!")
                player.recurso -= player.recurso_gasto
            else:
                player.iniciar_recuperacao()
                print(f"\nRecurso insuficiente! {player.nome} entra em recuperação por {player.recuperacao_turnos} turnos.")
        elif comando == "2":
            print("\nUsar item ainda não implementado.")
        elif comando == "3":
            batalha = False
            break
        else:
            print("\nComando inválido.")

        # Se a batalha está contecendo e o inimigo está vivo
        if batalha and enemy.esta_vivo():
            # Player toma dano
            dano_defesa, dano_hp, bool_dano_hp = player.receber_dano(enemy.forca)
            # Se o player deu dano apenas na defesa
            if dano_defesa > 0 and not bool_dano_hp:
                print(f"\n{enemy.nome} causou {dano_defesa} de dano na Defesa de {player.nome}!")
            # Se o player deu dano na defesa e HP
            elif bool_dano_hp and dano_defesa > 0:
                print(f"\n{enemy.nome} causou {dano_defesa} de dano na Defesa de {player.nome}!")
                print(f"{enemy.nome} causou {dano_hp} de dano no HP de {player.nome}!")
            # Se o player deu dano apenas no HP
            elif bool_dano_hp:
                print(f"\n{enemy.nome} causou {dano_hp} de dano no HP de {player.nome}!")
            # Verifica se o player está em recuperação ainda
            if player.esta_em_recuperacao():
                # Ve se saiu da recuperação, se não atualiza 1 turno na função processar_recuperacao()
                terminou = player.processar_recuperacao()
                # Se saiu da recuperação
                if terminou:
                    print(f"\n{player.nome} concluiu a recuperação e restaura {player.recurso_nome} para {player.recurso}/{player.recurso_max}.")
        input("> ")

    # Vitória do player
    if player.hp > 0 and batalha:
        limpar_tela()
        print(f"{player.nome} derrotou {enemy.nome}!")

        print(f"+{enemy.xp} XP")
        print(f"+{enemy.moedas} moedas")

        # Ganho de recompensas da batalha de acorso com o inimigo
        player.ganhar_xp(enemy.xp)
        player.moedas += enemy.moedas

        # Atualiza uma missão do player se ele tiver uma ativa, com base no inimigo que ele derrotou
        atualizar_progresso(player, "matar", enemy.id)
        
    
    # Derrota do player
    elif player.hp <= 0 and batalha:
        limpar_tela()
        print("\nVocê foi derrotado...")
        print("Voltando para a cidade de Eldor")
        game_state.position = [5, 5]
        player.hp = player.hp_max
    
    # Player foge da batalha
    elif batalha == False:
        limpar_tela()
        print("Você fugiu!")
    
    # Reseta a defesa e o recurso do player antes de voltar para o game_loop
    player.defesa = player_defesa_max
    player.recurso = player_recurso_max
    
    input("> ")
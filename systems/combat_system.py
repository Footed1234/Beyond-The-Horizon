from systems.quest_system import atualizar_progresso
import random

def verificar_combate():
    chance = random.randint(1, 100)
    if chance <= 30:
        return True
    return False

def iniciar_combate(player, enemy):
    batalha = True
    player_defesa_max = player.defesa
    player_recurso_max = player.recurso
    enemy_hp_max = enemy.hp
    print(f"{player.nome} se depara com um {enemy.nome}")
    input("> ")
    
    while player.esta_vivo() and enemy.esta_vivo() and batalha:
        if not player.esta_em_recuperacao() and player.recurso < player.recurso_gasto:
            player.iniciar_recuperacao()
            print(f"\n{player.nome} não tem recurso suficiente e entra em recuperação por {player.recuperacao_turnos} turnos!")

        print(f"{player.nome} enfrenta um {enemy.nome}!")
        print(f"{enemy.nome}: HP {enemy.hp}/{enemy_hp_max} | Força {enemy.forca} | Defesa {enemy.defesa}")
        print(f"{player.nome}: HP {player.hp}/{player.hp_max} | Força {player.forca} | {player.recurso_nome}: {player.recurso}/{player_recurso_max} | Defesa {player.defesa}")
        if player.esta_em_recuperacao():
            print(f"=== EM RECUPERAÇÃO: {player.recuperacao_turnos} turno(s) restantes ===\n")
        print("Escolha uma ação")
        print("1- Atacar")
        print("2 - Usar item")
        print("3- Fugir")
        comando = input("> ").strip()

        if comando == "1":
            if player.esta_em_recuperacao():
                print("\nVocê está em recuperação e não pode atacar.")
            elif player.recurso >= player.recurso_gasto:
                dano = enemy.receber_dano(player.forca)
                print(f"\n{player.nome} causou {dano} de dano!")
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

        if batalha and enemy.esta_vivo():
            dano = player.receber_dano(enemy.forca)
            print(f"{enemy.nome} causou {dano} de dano!")
            if player.esta_em_recuperacao():
                terminou = player.processar_recuperacao()
                if terminou:
                    print(f"\n{player.nome} concluiu a recuperação e restaura {player.recurso_nome} para {player.recurso}/{player.recurso_max}.")

    # Vitória
    if player.hp > 0 and batalha:
        print(f"{player.nome} derrotou {enemy.nome}!")

        print(f"+{enemy.xp} XP")
        print(f"+{enemy.moedas} moedas")

        player.ganhar_xp(enemy.xp)

        player.moedas += enemy.moedas

        atualizar_progresso(player, "matar", enemy.id)
    
    # Derrota
    elif player.hp <= 0 and batalha:
        print("\nVocê foi derrotado...")
        player.hp = player.hp_max
    
    elif batalha == False:
        print("Você fugiu!")
    
    player.defesa = player_defesa_max
    player.recurso = player_recurso_max
    
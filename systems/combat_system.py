from systems.quest_system import atualizar_progresso

def iniciar_combate(player, enemy):
    print(f"\nUm {enemy.nome} apareceu!")
    
    while player.esta_vivo() and enemy.esta_vivo(): 
        print("\n====================")
        print(f"{player.nome} HP: {player.hp}/{player.hp_max}")
        print(f"{enemy.nome} HP: {enemy.hp}/{enemy.hp_max}")
        print("====================")

        input("\n> ")

        # Turno jogador
        dano = enemy.receber_dano(player.forca)

        print(f"\n{player.nome} causou {dano} de dano!")

        # Turno Inimigo
        dano = player.receber_dano(enemy.forca)

        print(f"{enemy.nome} causou {dano} de dano!")

    # Vitória
    if player.hp > 0:
        print(f"\nVocê derrotou {enemy.nome}!")

        print(f"+{enemy.xp} XP")
        print(f"+{enemy.moedas} moedas")

        player.ganhar_xp(enemy.xp)

        player.moedas += enemy.moedas

        atualizar_progresso(player, "matar", enemy.id)
        
        return True
    
    # Derrota
    else:
        print("\nVocê foi derrotado...")

        return False
    
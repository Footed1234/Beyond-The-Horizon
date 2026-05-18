from data.quests import QUESTS

def aceitar_quest(player, quest_id):
    if quest_id in player.quests:
        return False
    
    player.quests[quest_id] = {
        "progresso": 0,
        "completa": False,
        "entregue": False
    }

    quest = QUESTS[quest_id]

    print(f"\nNova missão: {quest["nome"]}")

    return True

def atualizar_progresso(player, tipo, alvo):
    for quest_id, progresso in player.quests.items():
        if progresso["completa"]:
            continue

        quest = QUESTS[quest_id]

        objetivo = quest["objetivo"]

        if objetivo["tipo"] != tipo:
            continue

        if objetivo["alvo"] != alvo:
            continue

        progresso["progresso"] += 1

        print(
            f"\nProgresso da missão "
            f"{quest['nome']}: "
            f"{progresso['progresso']}/"
            f"{objetivo['quantidade']}"
        )

        if progresso["progresso"] >= objetivo["quantidade"]:
            progresso["completa"] = True

            print(f"\nMissão concluída: {quest['nome']}")

def entregar_recompensa(player):
    for quest_id, progresso in player.quests.items():
        if not progresso["completa"]:
            continue

        if progresso["entregue"]:
            continue

        quest = QUESTS[quest_id]

        recompensas = quest["recompensas"]

        player.ganhar_xp(recompensas["xp"])

        player.moedas += recompensas["moedas"]

        print(f"\nRecompensas recebidas:")
        print(f"+{recompensas['xp']} XP")
        print(f"+{recompensas['moedas']} moedas")

        progresso["entregue"] = True

def mostrar_quests(player):
    print("\n===== MISSÕES =====")

    if not player.quests:
        print("Nenhuma missão ativa.")
        return
    
    for quest_id, progresso in player.quests.items():
        quest = QUESTS[quest_id]

        objetivo = quest["objetivo"]

        if progresso["completa"]:
            status = "Concluída"
        
        else:
            status = "Em andamento"

        print(f"\n{quest['nome']}")
        print(quest["descricao"])
        print(
            f"{progresso['progresso']}/"
            f"{objetivo['quantidade']}"
        )
        print(f"Status: {status}")
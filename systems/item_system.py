from data.items import ITEMS
from systems.inventory_system import possui_item

def equipar_item(player, item_id):
    if not possui_item(player, item_id):
        return False
    
    item = ITEMS[item_id]

    # Verifica se é equipamento
    if item["tipo"] not in ["arma", "armadura"]:
        return False
    
    # Verifica classe
    if item["classe"] != player.classe:
        return False
    
    slot = item["slot"]

    # Equipar arma
    if slot == "arma":
        if player.arma:
            desequipar_item(player, player.arma)

        player.arma = item_id

        if "forca" in item:
            player.forca += item["forca"]

    # Equipar armadura
    elif slot == "armadura":
        if player.armadura:
            desequipar_item(player, player.armadura)

        player.armadura = item_id

        if "defesa" in item:
            player.defesa += item["defesa"]

    return True

def desequipar_item(player, item_id):
    item = ITEMS[item_id]

    slot = item["slot"]

    # Desequipar arma
    if slot == "arma":
        if "forca" in item:
            player.forca -= item["forca"]

        player.arma = None

    # Desequipar armadura
    elif slot == "armadura":
        if "defesa" in item:
            player.defesa -= item["defesa"]
        
        player.armadura = None

def mostrar_equipamento(player):
    print("\n===== EQUIPAMENTOS =====")

    # Arma
    if player.arma:
        arma = ITEMS[player.arma]["nome"]
    else:
        arma = "Nenhuma arma equipada"

    # Armadura
    if player.armadura:
        armadura = ITEMS[player.armadura]["nome"]
    else:
        armadura = "Nenhuma armadura equipada"
    
    print(f"Arma: {arma}")
    print(f"Armadura: {armadura}")
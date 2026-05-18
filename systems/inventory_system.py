from data.items import ITEMS

def possui_item(player, item_id):
    return item_id in player.inventario

def adicionar_item(player, item_id, quantidade=1):
    if item_id not in ITEMS:
        return False

    if possui_item(player, item_id):
        player.inventario[item_id] += quantidade
    else:
        player.inventario[item_id] = quantidade

    return True

def remover_item(player, item_id, quantidade=1):
    if not possui_item(player, item_id) or player.inventario[item_id] < quantidade:
        return False
    
    player.inventario[item_id] -= quantidade

    if player.inventario[item_id] <= 0 :
        del player.inventario[item_id]

    return True

def mostrar_inventario(player):
    print("\n===== INVENTÁRIO =====")

    if not player.inventario:
        print("Inventário vazio.")
        return 

    for item_id, quantidade, in player.inventario.items():
        item = ITEMS[item_id]

        print(f"{item['nome']}: x{quantidade}")
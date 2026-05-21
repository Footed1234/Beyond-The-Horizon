from data.enemies import ENEMIES

class Enemy:
    def __init__(self, enemy_id):
        enemy_data = ENEMIES[enemy_id]

        self.id = enemy_id

        self.nome = enemy_data["nome"]

        self.hp = enemy_data["hp"]
        
        self.forca = enemy_data["forca"]
        self.defesa = enemy_data["defesa"]

        self.xp = enemy_data["xp"]
        self.moedas = enemy_data["moedas"]

    def receber_dano(self, dano):
        if self.defesa >= dano:
            self.defesa -= dano
            dano_hp = 0
        else:
            dano_hp = dano - self.defesa
            self.defesa = 0
            self.hp -= dano_hp

        if self.hp < 0:
            self.hp = 0

        return dano_hp
    
    def esta_vivo(self):
        return self.hp > 0 
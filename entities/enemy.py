from data.enemies import ENEMIES

class Enemy:
    def __init__(self, enemy_id):
        enemy_data = ENEMIES[enemy_id]

        self.id = enemy_id

        self.nome = enemy_data["nome"]

        self.hp_max = enemy_data["hp"]
        self.hp = self.hp_max
        
        self.forca = enemy_data["forca"]
        self.defesa = enemy_data["defesa"]

        self.xp = enemy_data["xp"]
        self.moedas = enemy_data["moedas"]

    def receber_dano(self, dano):
        dano_final = max(0, dano - self.defesa)

        self.hp -= dano_final

        if self.hp < 0: 
            self.hp = 0

        return dano_final
    
    def esta_vivo(self):
        return self.hp > 0 
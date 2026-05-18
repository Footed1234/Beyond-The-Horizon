from data.classes import CLASSES

class Player:
    def __init__(self, nome, classe):

        classe_data = CLASSES[classe]

        self.nome = nome
        self.classe = classe

        self.hp_max = classe_data["hp"]
        self.hp = self.hp_max

        self.recurso_max = classe_data["recurso"]
        self.recurso = self.recurso_max

        self.forca = classe_data["forca"]
        self.defesa = classe_data["defesa"]

        self.nivel = 1
        self.xp = 0
        self.xp_proximo = 100

        self.moedas = 0

        self.arma = None
        self.armadura = None

        self.inventario = {}

        self.quests = {}

    def receber_dano(self, dano):
        dano_final = max(0, dano - self.defesa) # Calcula o dano final considerando a defesa do jogador

        self.hp -= dano_final

        if self.hp < 0:
            self.hp = 0

        return dano_final
    
    def curar(self, valor):

        self.hp += valor

        if self.hp > self.hp_max:
            self.hp = self.hp_max
    
    def ganhar_xp(self, valor):
        self.xp += valor

        if self.xp >= self.xp_proximo:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1

        self.xp -= self.xp_proximo

        self.xp_proximo = int(self.xp_proximo * 1.1)

        self.hp_max += 10
        self.hp += 10
        self.recurso_max += 5
        self.recurso += 5
        self.forca += 1
        self.defesa += 1
    
    def esta_vivo(self):
        return self.hp > 0
        
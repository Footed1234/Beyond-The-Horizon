from data.classes import CLASSES

class Player:
    def __init__(self, nome, classe):
        classe_data = CLASSES[classe]

        self.nome = nome
        self.classe = classe

        self.hp_max = classe_data["hp"]
        self.hp = self.hp_max

        self.recurso_nome = classe_data["recurso"]["nome"]
        self.recurso_max = classe_data["recurso"]["quantidade"]
        self.recurso = self.recurso_max
        self.recurso_gasto = 10

        self.forca = classe_data["forca"]
        self.defesa_max = classe_data["defesa"]
        self.defesa = self.defesa_max

        self.nivel = 1
        self.xp = 0
        self.xp_proximo = 100

        self.moedas = 0

        self.arma = None
        self.armadura = None

        self.inventario = {}

        self.quests = {}

        self.recuperando = False
        self.recuperacao_turnos = 0

    def receber_dano(self, dano):
        dano_defesa = 0
        dano_hp = 0
        bool_dano_hp = False
        
        if self.defesa >= dano:
            self.defesa -= dano
            dano_defesa = dano
        else:
            dano_defesa = self.defesa
            dano_hp = dano - self.defesa
            self.defesa = 0
            self.hp -= dano_hp
            bool_dano_hp = True

        if self.hp < 0:
            self.hp = 0

        return dano_defesa, dano_hp, bool_dano_hp
    
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
        self.defesa_max += 1
        self.defesa += 1
    
    def esta_vivo(self):
        return self.hp > 0
    
    def iniciar_recuperacao(self):
        self.recuperando = True
        self.recuperacao_turnos = 5

    def esta_em_recuperacao(self):
        return self.recuperando

    def processar_recuperacao(self):
        if not self.recuperando:
            return False

        self.recuperacao_turnos -= 1
        if self.recuperacao_turnos <= 0:
            self.recuperando = False
            self.recuperacao_turnos = 0
            self.recurso = self.recurso_max
            return True

        return False

    def recuperar_da_batalha(self):
        self.recurso = self.recurso_max
        self.defesa = self.defesa_max
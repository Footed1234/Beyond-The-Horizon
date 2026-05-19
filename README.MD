# Beyond The Horizon

Beyond The Horizon é um RPG ASCII desenvolvido em Python, focado em exploração, progressão de personagem, combate por turnos, quests, cidades e dungeons geradas proceduralmente.

O jogo se passa no misterioso mundo de Varyn, onde o jogador desperta sem memórias em uma floresta desconhecida após uma missão fracassada.

---

# Features

## Sistema de Classes
O jogador pode escolher entre diferentes classes:

- Guerreiro
- Mago
- Ladino

Cada classe possui:
- Atributos próprios;
- Equipamentos específicos;
- Estilo de combate único.

---

## Sistema de Combate
- Combate em turnos;
- Cálculo de dano;
- Defesa;
- Cura;
- Progressão de atributos.

---

## Sistema de Inventário
- Adicionar/remover itens;
- Equipamentos;
- Gerenciamento de armas e armaduras.

---

## Sistema de Itens
- Armas exclusivas por classe;
- Armaduras específicas;
- Progressão de raridade e poder.

---

## Sistema de Mapa
- Movimentação em mapa 10x10;
- Cidades;
- Diferentes biomas:
  - floresta
  - montanha
  - planície
  - colinas
  - pântano

---

## Sistema de Cidades
Cada cidade possui:
- Mapa próprio;
- Descrição própria;
- Lojas;
- Ferreiro;
- Estalagem.

Cidades atuais:
- Eldor
- Thalos
- Nyxar
- Draven

---

## Sistema de Quests
- Missões com objetivos;
- Recompensas;
- Track de progressão;
- Integração com combate.

---

## Sistema de Dungeons
- Geração procedural;
- Localização aleatória por save;
- Exploração;
- Chefes únicos.

---

## Sistema de Save/Load
- Salvamento em JSON;
- Persistência de:
  - Player
  - Quests
  - Equipamentos
  - Dungeons
  - Posição
  - Inventário

---

# Estrutura do Projeto

```txt
beyond_the_horizon/
│
├── main.py
│
├── core/
│   ├── game_state.py
│   ├── config.py
│   └── save_manager.py
│
├── entities/
│   ├── player.py
│   ├── enemy.py
│   ├── npc.py
│   └── item.py
│
├── systems/
│   ├── combat_system.py
│   ├── city_system.py
│   ├── inventory_system.py
│   ├── world_system.py
│   ├── item_system.py
│   ├── dungeon_system.py
│   ├── quest_system.py
│   └── dialogue_system.py
│
├── data/
│   ├── items.py
│   ├── enemies.py
│   ├── dialogues.py
│   ├── classes.py
│   ├── world_map.py
│   ├── dungeons.py
│   ├── quests.py
│   └── cities.py
│
├── ui/
│   ├── menus.py
│   ├── text.py
│   └── ascii.py
│
└── utils/
    └── helpers.py
```

---

# Requisitos

## Python

Versão recomendada:

```txt
Python 3.12+
```

Versão mínima:

```txt
Python 3.11
```

---

# Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/beyond-the-horizon.git
```

---

## 2. Entre na pasta

```bash
cd beyond-the-horizon
```

---

## 3. Crie o ambiente virtual

Windows:

```bash
python -m venv .venv
```

Linux/MacOS:

```bash
python3 -m venv .venv
```

---

## 4. Ative o ambiente virtual

Windows:

```bash
.venv\Scripts\activate
```

Linux/MacOS:

```bash
source .venv/bin/activate
```

---

## 5. Execute o jogo

```bash
python main.py
```

---

# Roadmap Futuro

## Sistemas planejados

- Múltiplas dungeons;
- Bosses especiais;
- Habilidades;
- Árvores de skill;
- Crafting;
- NPCs interativos;
- Facções;
- Clima dinâmico;
- Eventos aleatórios;
- Sistema de reputação;
- Lojas completas;
- Geração procedural avançada.

---

# Lore

O jogador desperta sozinho em uma floresta desconhecida do mundo de Varyn, sem qualquer memória de como chegou ali.

Após enfrentar criaturas estranhas e conhecer o sábio Kael, descobre lentamente que fazia parte de uma missão que terminou em desastre.

Enquanto explora cidades antigas, ruínas esquecidas e masmorras ocultas, o jogador começa a desvendar os segredos obscuros de Varyn e a verdadeira ameaça por trás do Imperador dos Demônios.

---

# Objetivo Final

Explorar Varyn, fortalecer seu personagem, desvendar a verdade sobre sua missão perdida e enfrentar o Imperador dos Demônios.

---

# Autor

Projeto desenvolvido por Henrique Ratis.

---

# Licença

Este projeto tem objetivo educacional e de aprendizado, com possível uso comercial futuro.
#forma numeros aleatorios de forma inteiro (randint)
from random import randint
#cria uma lista vazia
lista_npcs = []
player = {
    "nome": "Noah",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "dano": 25,
}
#gera um dicionario automatico com as informações que eu preciso para um npc
def criar_npc(level):
    novo_npc = {
        #o nome do npc está vinculado a variavel level para gerar automaticamente
        "nome": f"Monstro #{level}",
        #o level gerado é vinculado a variavel
        "level": level,
        #o dano do npc é de acordo com o level dele (se for level 2 ele tem 10 de dano por ser X5)
        "dano": 5 * level,
        #a vida do npc é de acordo com o level dele (se ele é level 2 ele tem 200 de vida por ser X100)
        "hp": 100 * level,
        'hp_max': 100 * level,
        #o quanto de experiencia ele vai me dar quando eu matar ele
        "exp": 7 * level,
    }
    #salva os itens criados na lista novo_npc
    return novo_npc
#gera uma lista de npcs de acordo com os atributos a cima utilizando o range(que serve para gerar uma lista com a quantidade de numeros informados)
def gerar_npcs (n_npcs):
    for x in range(n_npcs):
        npc = criar_npc(x + 1)
        lista_npcs.append(npc)
#exibe os npcs criados no gerar_npcs
def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)
#exibe as informações dos npcs
def exibir_npc(npc):
    print(
            f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']} "
        )
#exibe as informações do player    
def exibir_player():
    print(
            f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']} "
        )
#reseta a vida do player depois da luta
def reset_player():
    player['hp'] = player['hp_max']
def reset_npc(npc):
    npc['hp'] = npc['hp_max']
#esquema de level up, como funciona, exp aumentada e hp aumentado
def level_up():
    if player["exp"] >= player["exp_max"]:
        player["level"] += 1
        player["exp"] = 0
        player["exp_max"] = player["exp_max"] * 2
        player["hp_max"] += 20
        
# inicia a batalha
def iniciar_batalha(npc): 
    while player["hp"] > 0 and npc["hp"] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)
    #fala quanto de exp ganhou
    if player['hp'] > 0:
        print(f"O {player['nome']} venceu e ganhou {npc['exp']} de EXP!")
        player['exp'] += npc['exp']
        exibir_player()
    #falha que o player perdeu
    else:
        print(f"O {npc['nome']} venceu!")
        exibir_npc(npc)
    #chama a função de level up antes de resetar a vida do player e npc
    level_up()
    #chama a função que reseta a vida do player e do npc
    reset_player()
    reset_npc(npc)

# atacar_npc(npc) - npc:hp - player:dano 
def atacar_npc(npc):
    npc["hp"] -= player["dano"]
# atacar_player(npc) - player:hp - npc:dano 
def atacar_player(npc): 
    player["hp"] -= npc["dano"]
# mostra o quanto de vida que o player e o npc perderam
def exibir_info_batalha(npc):
    print(f"Player: {player['hp']}/{player['hp_max']}")
    print(f"NPC {npc['nome']}: {npc['hp']}/{npc['hp_max']}")
    print('---------------------\n')

#escolhe a quantidade de npcs que o item gerar_npcs vai criar
gerar_npcs(5)
exibir_npcs()
npc_selecionado = lista_npcs[0]
iniciar_batalha(npc_selecionado)

exibir_player()
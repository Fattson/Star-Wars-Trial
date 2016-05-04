# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 08:16:01 2016

@author: GuilhermeZaborowsky
"""

import SwTrail as sw
import random as rd

meuJogador = sw.Jogo()

# 3000 km  5 cidades 5 camps

CC = []
ci = 5 # 1
ca = 5 # 2
p = 50

for i in range(ci+ca):
    if ci>0 and ca>0:
        x = rd.randint(1,100)

        if x > p:
            CC.append(1)
            ci -= 1
            p += 15
        else:
            CC.append(2)
            ca -= 1
            p -= 15
            
    elif ci>0:
        CC.append(1)
        ci -= 1
    else:
        CC.append(2)      
        ca -= 1
        
def dist_proximaCidade(CCrestante):
    for d in range(len(CCrestante)):
        if CCrestante[d] == 1:
            break
    
    return (d+1)

def status(jogador):
    print()
    print("===== STATUS =====")
    print("Gasolina: ", jogador.gas)
    print("Pecas: ", jogador.pecas)    
    print("Durabilidade: ", jogador.durab)
    print("Comida: ", jogador.comida)
    print("Health: ", jogador.health)
    print("DinDin: ", jogador.reais)
    print("Amigos vivos: ", jogador.numero_jogadores-1)
    print("Distancia faltante: ", jogador.distancia)
    print("Tempo restante: ", jogador.temporestante)
    print("==================")


   
def mercado(jog):# criar
    print()
    print("===== MERCADO =====")
    z = -1
    while z != 0:
        print()
        print("Grana atual: ", jog.reais)
        print("Comida atual: ", jog.comida)
        print("0 - Sair \n1 - Comprar 10 comidas (10 reais) \n2 - Vender 10 comidas (10 reais) \n3 - Comprar 100 pecas (10 reais)\n4 - Comprar 100 gasosa (10 reais) \n5 - Queimar dinheiro")
        z = int(input("==>"))
        if z == 1:
            if jog.reais >= 10:
                jog.reais-=10
                jog.comida+=10
                print("Comida agora: ", jog.comida)
            else:
                print("Ta sem grana porra")
        if z == 2:
            if jog.comida >= 10:
                jog.comida-=10
                jog.reais+=10
                print("Comida agora: ", jog.comida)
            else:
                print("Ta sem comida porra, ta tentando enganar alguem?")
        if z == 3:
            if jog.reais >= 10:
                jog.reais-=10
                jog.pecas+=100
                print("Pecas agora: ", jog.pecas)
            else:
                print("Ta sem grana porra")
        if z == 4:
            if jog.reais >= 10:
                jog.reais-=10
                jog.gas+=100
                print("Gasosa agora: ", jog.gas)
            else:
                print("Ta sem grana porra")
        if z == 5:
            if jog.reais > 0:
                print("Is not about the money, is about sending the message.")
                jog.reais=0
            else:
                print("vc nem tem dinheiro p queimar")
                
    
    
def conserto(jogador):
    print()
    print("===== CONSERTO =====")
    y = -1
    while y != 0:
        print()
        print("Durabilidade atual: ", jogador.durab)
        print("qtdade atual de pecas: ", jogador.pecas)
        y = int(input("1 - Consertar 200 de durabilidade (custo depende da durabilidade: >600=200pecas >300=300pecas else 500 pecas) \n0 - Sair\n"))
        if y == 1:
            if jogador.durab == 1000:
                print("Carro ja saudavel")
            else:
                if jogador.durab > 600:
                    if jogador.pecas >= 200:
                        print("consertou 200 por 200 pecas")
                        jogador.durab += 200
                        jogador.pecas -= 200
                    else:
                        print("ta sem pecas suficientes, vai comprar")
                elif jogador.durab > 300:
                    if jogador.pecas >= 300:
                        print("consertou 200 por 300 pecas")
                        jogador.durab += 200
                        jogador.pecas -= 300
                    else:
                        print("ta sem pecas suficientes, vai comprar")
                else:
                    if jogador.pecas >= 500:
                        print("consertou 200 por 500 pecas")
                        jogador.durab += 200
                        jogador.pecas -= 500
                    else:
                        print("ta sem pecas suficientes, vai comprar")
            
            if jogador.durab > 1000: # nao deixa passar do max
                jogador.durab = 1000

def camp(jogador, prox):# criar
    print("Voce esta no acampamento.")


def cidade(jogador, prox):
    print("******CIDADE******")
    print("Vc esta numa cidade, oq deseja fazer?")
    print("Rodadas p prox cidade (ou destino final): ", prox)
    x = -1
    while x != 0:
        print()
        print("0 - continuar viagem (0 horas) \n1 - mercado (3 horas) \n2 - SUS (2 horas) \n3 - hospotal particular (0 horas/20 reais) \n4 - conserto do carro (2 horas) \n5 - Status")
        x = int(input("==>"))
        if x == 1: # mercado
            mercado(jogador)
            jogador.temporestante -= 3
        if x == 2: # sus
            print("foi ao sus, gastou 2 horas e recuperou 20 de vida")
            jogador.temporestante -= 2
            jogador.health += 20
        if x == 3: #hosp particular
            if jogador.reais >= 20:
                print("foi ao hospital, gastou 20 reais e recuperou 20 health")
            else:
                print("nao deu, vc ta sem grana")
        if x == 4: # conserto
            conserto(jogador)
            jogador.temporestante -= 2
        if x == 5: # status
            status(jogador)
        


chegou = False
game_over = False

print("vc e 3 amigos tao no piaui e blablabla roubaram um carro blablabla vai")
print("a viagem comeca na cidade que vcs estavam com a escola")
print()
proxCidade = dist_proximaCidade(CC)
cidade(meuJogador, proxCidade)

i = 0 #iterador de rodadas

while chegou == False and game_over == False:
    
    ev = rd.randint(1,100)
    
    proxCidade = dist_proximaCidade(CC[i:])
    
    if ev < 50:
        #acontece ema
        pass
    elif ev < 75:
        #acontece lobo guara
        pass
    elif ev < 85:
        #acontece buraco
        pass
    
    if meuJogador.temporestante <= 0:
        game_over = True
        break
    
    meuJogador.varia_comida()
    meuJogador.varia_gas()
    meuJogador.varia_distancia()
    meuJogador.varia_durabilidade(meuJogador.tempodeviagem)
    meuJogador.varia_health()
    meuJogador.varia_tempo()
    
    if meuJogador.distancia <= 0:
        chegou = True
        break
    elif meuJogador.temporestante <= 0:
        game_over = True
        break
    
    if CC[i] == 1:
        cidade(meuJogador, proxCidade) #continuar criando
    else:
        camp(meuJogador, proxCidade) # criar
        
    if meuJogador.distancia <= 0:
        chegou = True
    elif meuJogador.temporestante <= 0:
        game_over = True
    
    i += 1
    




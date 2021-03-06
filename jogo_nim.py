 
# n - número de peças inicial
# m - número máximo de peças que é possível retirar em uma rodada

# decide quantas peças o computador irá tirar do tabuleiro 
def computador_escolhe_jogada(n, m):

    #verifica o número de peças que seja múltiplo de (m+1)
    computremove = n % (m+1)
    
    if computremove  > 0:
        return computremove
    else: 
        return m 

# Verifica quantidade de peças que o usuário esta tirando do tabuleiro 
def usuario_escolhe_jogada (n, m):

    print(" ")
    useremove = int(input("Quantas peças você vai tirar? "))
    print(" ")

    #Verifica se os valores inseridos são correspondentes 
    while useremove > m or useremove <= 0 or useremove > n:  
        print(" ")  
        print("Oops! Jogada inválida! Tente de novo.")
        print(" ")
        useremove= int(input("Quantas peças você vai tirar? "))
        
    return useremove

def partida ():

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por rodada? "))

    # Controla a vez do computador e do usuário
    controle = True

    # decide quem iniciará o jogo
    if n % (m + 1) == 0: 
        print("")
        print("Voce começa!")
        controle = False
    else:
        print("")
        print("Computador começa!")
        print("")

    # Continua enquanto estiver peça no jogo
    while n > 0:

        # condição para chamar uma das duas funções 
        if controle:
            controle = False 
            rodada = computador_escolhe_jogada(n, m)
            print("Computador retirou {} peças.".format(rodada))
        else:
            controle = True 
            rodada = usuario_escolhe_jogada(n, m)
            print("Você retirou {} peças.".format(rodada))

        # Retira as peças do jogo:
        n = n - rodada

        # Mostra o estado atual do jogo:
        print("Restam apenas {} peças em jogo.".format(n))
        print(" ")
    print("Fim do jogo! Computador ganhou!")

def campeonato():
    jogada_campeonato = 1

    #Executa a partida três vezes
    while jogada_campeonato < 4:
        print(" ")
        print("**** Rodada {} ****".format(jogada_campeonato))
        print(" ")
        partida()
        jogada_campeonato += 1
    print("**** Final do campeonato! ****")
    print(" ")
    print("Placar: Você 0 x 3 Computador")

 
tipo_jogo = 0

# verifica a escolha do usuário
while tipo_jogo == 0:

    print("Bem-vindo ao jogo NIM! Escolha: ")
    print("1 - para jogar partida isolada ")
    print("2 - para jogar campeonato ")
    tipo_jogo = int(input())

    if tipo_jogo == 1:
        print("Voce escolheu partida isolada!")
        print("")
        partida()
        break # para sair do loop 

    if tipo_jogo == 2:
        print(" ")
        print("Voce escolheu campeonato!")
        print("")
        campeonato()
        break # para sair do loop

    else:
        print("Opção invalida")
        tipo_jogo = 0 # condição para repetir o while

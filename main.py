from jogoEstrutura import tabuleiro, movimento,  verificaInput, \
                            printTabuleiro, verificaVencedor,  fazMovimento

from minimax import movimentoIA

jogador = 0 

print("===================")
print("\nDesenvolvedor: Thiago Manoel Basilio\nRGM:20646828")
print("===================")
print("Bem vindo ao jogo da velha com IA")

op = int(input("Opções: \n1 - Jogador X IA \n2 - IA x IA\n\n Digite sua opção: "))
tab = tabuleiro()
vencedor = verificaVencedor(tab)
if(op == 1):#Jogador x IA
    while(not vencedor):
        print("===================")
        printTabuleiro(tab)
        print("===================")
        if(jogador == 0):
            i = verificaInput("Digite a linha: ")
            j = verificaInput("Digite a coluna: ")
            
        else:
            i,j = movimentoIA(tab, jogador)    
              
        if(movimento(tab, i, j)):
            fazMovimento(tab, i, j, jogador)
            jogador = (jogador + 1)%2
        else:
            print("A posicao informado ja esta ocupada")
        
        vencedor = verificaVencedor(tab)
elif(op == 2):#IAxIA
    while(not vencedor):
        printTabuleiro(tab)
        print("===================")
        if(jogador == 0):
            i,j = movimentoIA(tab, jogador)
        else:
        
            i,j = movimentoIA(tab, jogador)
        
        
        if(movimento(tab, i, j)):
            fazMovimento(tab, i, j, jogador)
            jogador = (jogador + 1)%2
        else:
            print("A posicao informado ja esta ocupada")
        
        vencedor = verificaVencedor(tab)
else:
    print("essa opção não é valida\n===================")


print("===================")
printTabuleiro(tab)
print("Resultado = ", vencedor)
print("===================")

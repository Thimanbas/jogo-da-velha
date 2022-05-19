from jogoEstrutura import branco, token, verificaVencedor

def movimentoIA(tab, jogador):
    possibilidades = getPosicoes(tab)
    melhorValor = None
    melhorMovimento = None
    for possibilidade in possibilidades:
        tab[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(tab, jogador)
        tab[possibilidade[0]][possibilidade[1]] = branco
        if(melhorValor is None):
            melhorValor = valor
            melhorMovimentomento = possibilidade
        elif(jogador == 0):
            if(valor > melhorValor):
                melhorValor = valor
                melhorMovimentomento = possibilidade
        elif(jogador == 1):
            if(valor < melhorValor):
                melhorValor = valor
                melhorMovimentomento = possibilidade

    return melhorMovimentomento[0], melhorMovimentomento[1]

def getPosicoes(tab):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(tab[i][j] == branco):
                posicoes.append([i, j])
    
    return posicoes

score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}

def minimax(tab, jogador):
    vencedor = verificaVencedor(tab)
    if(vencedor):
        return score[vencedor]
    jogador = (jogador + 1)%2
    
    possibilidades = getPosicoes(tab)
    melhorValor = None
    for possibilidade in possibilidades:
        tab[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(tab, jogador)
        tab[possibilidade[0]][possibilidade[1]] = branco

        if(melhorValor is None):
            melhorValor = valor
        elif(jogador == 0):
            if(valor > melhorValor):
                melhorValor = valor
        elif(jogador == 1):
            if(valor < melhorValor):
                melhorValor = valor

    return melhorValor
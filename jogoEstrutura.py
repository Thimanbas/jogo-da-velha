branco = " "
token = ["X", "O"]

def tabuleiro():#cria o tabuleiro vazio
    tab = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ]
    return tab


def printTabuleiro(tab):#mostra o tabuleiro atual
    for i in range(3):
        print("|".join(tab[i]))
        if(i < 2):
            print("------")


def verificaInput(mensagem):#verifica se é valido o input de linha e coluna
    try:
        n = int(input(mensagem))
        if(n >= 1 and n <= 3):
            return n - 1
        else:
            print("Numero precisa estar entra 1 e 3")
            return verificaInput(mensagem)
    except:
        print("Numero nao valido")
        return verificaInput(mensagem)


def movimento(tab, i , j):#verifica se a casa está livre
    if(tab[i][j] == branco):
        return True
    else:
        return False


def fazMovimento(tab, i, j, jogador): #coloca o token do jogador ou da IA na casa
    tab[i][j] = token[jogador]


def verificaVencedor(tab):#verifica pelas linhas e colunas e depois nas diagonais se existem 3 tokens iguais
    # linhas 
    for i in range(3):
        if(tab[i][0] == tab[i][1] and tab[i][1] == tab[i][2] and tab[i][0] != branco):
            return tab[i][0]
    
    # coluna
    for i in range(3):
        if(tab[0][i] == tab[1][i] and tab[1][i] == tab[2][i] and tab[0][i] != branco):
            return tab[0][i]

    # diagonal principal
    if(tab[0][0] != branco and tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2]):
        return tab[0][0]

    # diagonal secundaria
    if(tab[0][2] != branco and tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0]):
        return tab[0][2]

    for i in range(3):
        for j in range(3):
            if(tab[i][j] == branco):
                return False

    return "EMPATE"
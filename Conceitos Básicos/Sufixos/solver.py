# Função recursiva que devolve uma lista com todos os sufixos de uma palavra x
def sufixos(x):
    #  se x = vazio então vazio é o conjunto de todos os sufixos de x
    if len(x) == 0:
        return [""]
    else:
        # chamo recursivamente para a palavra, removendo o primeiro caractere e adicionando o primeiro caractere à lista de sufixos
        return [x] + sufixos(x[1:]) 

def main():
    x = input()
    
    print( sufixos(x) )


if __name__ == "__main__":
    main()
    
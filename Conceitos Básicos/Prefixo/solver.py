# função recursiva que decide se uma palavra x é prefixo de uma palavra y
def prefixo(x, y):
    if len(x) == 0:
        return True
    if len(y) == 0:
        return False
    # se x != de vazio e y = vazio, então x não é prefixo de y
    if len(x) != 0 and len(y) == 0: 
        return False
    # se o primeiro caractere de x for diferente do primeiro caractere de y, então x não é prefixo de y
    if x[0] != y[0]:
        return False
    else:
        return prefixo(x[1:], y[1:]) #chamo recursivamente  
     
def main():
    x = input()
    y = input()
    print( prefixo(x,y) )


if __name__ == "__main__":
    main()
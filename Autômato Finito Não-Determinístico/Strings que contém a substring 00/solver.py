# Exemplo de NFA que terminam em 00 ou 11 
edges = {
(1, '0') : [1, 2],
(1, '1') : [1, 3],
(2, '0') : [],
(2, '1') : [1, 3],
(3, '0') : [1, 2],
(3, '1') : [4],
(4, '0') : [4],
(4, '1') : [4]

}
initial   =  1 # estado inicial
accepting = [4] # estados finais

def nfa(string, current, edges, accepting): 
    if string == "":
        return  current in accepting        
    else:
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if nfa(string[1:], next, edges, accepting):
                    return True
        return False
        

string = input()
print ( nfa(string, initial, edges, accepting) )

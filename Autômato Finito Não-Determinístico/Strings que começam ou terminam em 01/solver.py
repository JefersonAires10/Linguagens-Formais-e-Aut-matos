# Faça um NFA que aceite strings que começam com 01 ou que termina em 01
edges = {
    (0, '0') : [1,3],
    (0, '1') : [5],
    (1, '0') : [3],
    (1, '1') : [2],
    (2, '0') : [2],
    (2, '1') : [2],
    (3, '0') : [3],
    (3, '1') : [4],
    (5, '1') : [5],
    (5, '0') : [3]
}
initial   =  0 # estado inicial
accepting = [2,4] # estado final

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


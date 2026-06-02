lista = [2, 4, 2, 2, 3, 3, 1]
nova_lista = [] 

def remove_repetidos(lista):
    
    for elemento in lista:
        if elemento not in nova_lista:
            nova_lista.append(elemento)
            
    return sorted(nova_lista)

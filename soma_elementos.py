lista = []

n = int(input("Digite o número de elementos: "))

for i in range(n):
    valor = int(input("Digite um número: "))
    lista.append(valor)

def soma_elementos(lista):
    return sum(lista)
   
print(soma_elementos((lista)))
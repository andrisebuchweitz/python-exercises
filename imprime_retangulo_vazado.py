largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

i = 1

print("#" * largura)

while i < (altura - 1):
    print("#", " " * (largura - 4), "#")
    i = i + 1

print("#" * largura)
        
   
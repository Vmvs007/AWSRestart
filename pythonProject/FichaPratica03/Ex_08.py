num = 0
somatorio = 0
contador = 0

while (num != -1):
    num = int(input("Insira um número: "))
    somatorio += num
    contador += 1

print("Somatorio:",somatorio)
print("Contador:",contador)
media = (somatorio+1) / (contador-1)
print("Média:", media)

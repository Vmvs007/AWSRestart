
# ler numero
num=int(input("Insira um número: "))

ant=num-5
suc=num+5

# imprimir anteriores
while(ant<num):
    print(ant)
    ant+=1

num+=1

# imprimir sucessores
while(num<=suc):
    print(num)
    num+=1
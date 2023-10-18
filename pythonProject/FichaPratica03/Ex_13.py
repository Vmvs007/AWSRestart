
crescente = bool(True)

# ler quantidade de numeros
quantidade_numeros=int(input("Quantos números deseja inserir: "))

contador=1

anterior=int(input("Insira um número: "))

while(contador<quantidade_numeros):
    num=int(input("Insira um número: "))
    contador+=1

    if(num<=anterior): # se isto for verdade, a sequencia nunca mais é crescente
        crescente=False

    anterior=num


if(crescente):
    print("Crescente")
else:
    print("Não Crescente")
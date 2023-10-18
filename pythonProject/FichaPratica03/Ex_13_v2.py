qtd_numeros = int(input("Quantos números deseja inserir: "))

i=1
n1 = int(input("introduza um numero: "))

while (i < qtd_numeros):

    n2 = int(input("introduza um numero: "))
    i = i + 1

    if (n1 >= n2):
        crescente = False

    n1=n2


if crescente == True:
    print("Sequência crescente...")
else:
    print("Sequência não crescente")
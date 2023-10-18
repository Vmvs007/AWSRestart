quant=int(input("Quantos números deseja inserir?:"))
counter=1
posicao=1

#tem de inserir mais que 1 numero para comparar
if quant>=2:
    # 1º valor para registo de comparação com o 2º input
    valor=int(input("Insira um número:"))
    while (counter<quant):
        valorNovo=int(input("Insira um número:"))
        #compara o valor inserido, com o antigo
        if (valorNovo>valor):
            #se sim, incrementa uma posicao para comparar com quantidade
            posicao=posicao+1
        counter=counter+1
        #escreve o valor novo por cima do anterior
        valor = valorNovo

#se a posicao foi igual à quantidade então é porque foi sempre crescente
    if (posicao==quant):
        print("Os números são crescentes!")
    else:
        print("Os números não são crescentes!")
else:
    print("Insira 2 valores para comparação!!!")
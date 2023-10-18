
# ler numero
num=int(input("Insira um número: "))

ant=num-5
num=num+5

while(ant<=num):
    if(ant!=num-5):
        print(ant)
    ant+=1

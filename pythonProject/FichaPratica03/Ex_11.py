num = 0

intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while (num >= 0):
    num = int(input("Insira um numero (negativo para terminar): "))

    if (num >= 0 and num <= 25):
        intervalo_0_25 += 1

    if (num >= 26 and num <= 50):
        intervalo_26_50 += 1

    if (num >= 51 and num <= 75):
        intervalo_51_75 += 1

    if (num >= 76 and num <= 100):
        intervalo_76_100 += 1


print("[0,25]:",intervalo_0_25)
print("[26,50]:", intervalo_26_50)
print("[51,75]:",intervalo_51_75)
print("[76,100]:", intervalo_76_100)
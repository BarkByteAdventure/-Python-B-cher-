def summe(*zahl):
    summe = 0
    for i in zahl:
        summe += i
    return summe

print(summe(1,2,3))
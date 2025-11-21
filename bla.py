def summera(lista):
    summan = 0
    for i in range(len(lista)):
        summan   = summan + lista[i]
    return summan

summan = summera([1,2,3,4,5,6])
print(summan)
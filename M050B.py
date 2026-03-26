def karralilar_yigindisi(n):
    yigindi = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
             yigindi += i 
    return yigindi
n = int(input())
print(karralilar_yigindisi(n))
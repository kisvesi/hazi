n = 0
i = 999
j = 999

while n == 0 and i > 99:
    j = i
    while n == 0 and j > 99:
        szorzat = str(i * j)
        if int(szorzat) > n:
            if szorzat == szorzat[::-1]:
                n = int(szorzat)
                x = i
                y = j
        j -= 1
    i -= 1

print(n, ' a legnagyobb palindromszám, amely kettő 3-jegyű szám (', x, ' x ', y, ') szorzataként felírható.')
n = 0
x = 0
y = 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        szorzat = str(i * j)
        if int(szorzat) > n:
            if szorzat == szorzat[::-1]:
                n = int(szorzat)
                x = i
                y = j

print(n, 'a legnagyobb palindromszám, amely kettő 3-jegyű szám (', x, 'x', y, ') szorzataként felírható.')

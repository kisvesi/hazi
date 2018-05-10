szamjegyek = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
szamjegyek2 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}


def tizesbevaltas(n, b1):
    tizesszam = 0
    lepes = 1
    hatvany = 1
    while lepes <= len(n):
        tizesszam += szamjegyek[str(n)[::-1][lepes-1]] * hatvany
        lepes += 1
        hatvany = hatvany * int(b1)
    return tizesszam


def atvaltas(n, b1, b2):
    if b2 == '10':
        return tizesbevaltas(n, b1)
    szamstr = ''
    szam = tizesbevaltas(n, b1)
    while szam != 0:
        szamstr += szamjegyek2[szam % int(b2)]
        szam = szam // int(b2)
    return szamstr[::-1]


print('Számrendszer átváltó ( 2 - 36 )!')
adatok = input('Adjon meg egy számot, annak számrendszerét és a cél számrendszert! (n1,n2,n3): ')
szam, szr1, szr2 = adatok.split(',')

print('A megadott szám (', szam, ') a kiválasztott cél számrendszerben (', szr2, '): ', atvaltas(szam, szr1, szr2))

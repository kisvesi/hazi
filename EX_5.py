dict = {0: '', 1: '-', 2: '+'}


def kiszamol(ls):
    for i in ls:
        ossz = 0
        aktszam = ''
        aktelojel = ''
        for j in i:
            if '1' <= j <= '9':
                aktszam += j
            else:
                if aktelojel == '':
                    ossz = int(aktszam)
                    aktszam = ''
                    aktelojel = j
                else:
                    if aktelojel == '+':
                        ossz += int(aktszam)
                        aktszam = ''
                        aktelojel = j
                    else:
                        ossz -= int(aktszam)
                        aktszam = ''
                        aktelojel = j
        if aktelojel == '+':
            ossz += int(aktszam)
        else:
            ossz -= int(aktszam)
        if ossz == 100:
            print(i,'= 100')


sorok = []

for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        for g in range(3):
                            for h in range(3):
                                sor = '1'
                                sor += dict[a] + '2' + dict[b] + '3' + dict[c] + '4' + dict[d] + '5' + dict[e] + '6' + dict[f] + '7' + dict[g] + '8' + dict[h] + '9'
                                sorok.append(sor)

kiszamol(sorok)
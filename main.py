import collections

T = int(input())

peregovorki = []

vershina = set()
for i in range(T):
    d = input()
    for j in range(len(d) - 3):
        cur = d[j] + d[j + 1] + d[j + 2]
        cur_next = d[j + 1] + d[j + 2] + d[j + 3]
        peregovorki.append([cur, cur_next])
        vershina.add(cur)
        vershina.add(cur_next)

peregovorki.sort()

c = collections.Counter()
for x, x1 in peregovorki:
    c[x, x1] += 1

print(len(vershina))

print(len(c))
for p in c:
    print(p[0], p[1], c.get(p))
    

#День стажера Яндекса - бэкенд разработки

#Задача - А. Граф подстрок

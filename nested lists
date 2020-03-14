from __future__ import print_function
import sys

nested_list = list()

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    nested_list.append([name,score])


scores = list()

for i in nested_list:
    scores.append(i[1])

min1 = min(scores)

scores = [i for i in scores if i != min1] 

min2 = min(scores)

lista_nombres = list()
for i in nested_list:
    if i[1] == min2:
        lista_nombres.append(i[0])

print(*sorted(lista_nombres), sep="\n", file=sys.stdout)

import sys
from itertools import combinations

score = []
lastchar = []

def is_valid_comb(comb):
    for comb_ix, data_ix in enumerate(comb):
        if lastchar[data_ix] == '1' and comb[comb_ix-1] != data_ix-1:
            return False
    return True

def sum_comb(comb):
    return sum(map(lambda x: score[x], comb))

n, m = map(int, input().split())
if n > 100:
    raise ValueError
    
lines = sys.stdin.readlines()
lines.sort()
for i in range(n):
    str = lines[i].split(" ")
    score.append(int(str[1]))
    lastchar.append(str[0][-1])

combs = combinations(list(range(0, n)), m)
#print(list(combs))  
valid_combs = [c for c in combs if is_valid_comb(c)]
#print(valid_combs)  
csums = map(lambda x: sum_comb(x), valid_combs)
#print(list(csums))  
answer = min(csums)
    
print(answer)

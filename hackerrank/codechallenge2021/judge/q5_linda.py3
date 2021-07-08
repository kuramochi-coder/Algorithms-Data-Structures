import sys

class Data:
    def __init__(self, isortval, iscore, iptype):
        self.sortval = isortval
        self.score = iscore
        self.ptype = iptype #0 for single, 1 or 2 for couple

def max_ptype_0_or_2(idata):
    return max(filter(lambda x: x.ptype != 1, idata), key=lambda x: x.score).score

def min_ptype_0_or_1(idata):
    return min(filter(lambda x: x.ptype != 2, idata), key=lambda x: x.score).score

n, m = map(int, input().split())
lines = sys.stdin.readlines()
lines.sort()
data = []
for i, line in enumerate(lines): #not faster
    words = line.split(" ")
    lastchar = words[0][-1]
    score = int(words[1])
    if lastchar == '1':
        partner_score = data[i-1].score
        if partner_score <= score:
            data.append(Data(score*2.0, score, 0)) #treat as single
        else:
            #if same couple score, sort higher +0 score first
            sortval = score + partner_score + (score*1e-7) + (i*1e-8)
            data[i-1].sortval = sortval #update sortval of partner
            data[i-1].ptype = 1 #update ptype of partner
            data.append(Data(sortval+2e-9, score, 2))
    else:
        data.append(Data(score*2.0, score, 0))

if m == 1:
    answer = min_ptype_0_or_1(data) #no need to sort
elif m == n:
    answer = sum(x.score for x in data) #no need to sort
else:
    data.sort(key=lambda x:x.sortval)
    answer = sum(x.score for x in data[:m])
    if data[m-1].ptype == 1:
        answer1 = answer - data[m-1].score + min_ptype_0_or_1(data[m-1:n])
        answer2 = answer + data[m].score - max_ptype_0_or_2(data[:m-1])
        answer = min(answer1, answer2)

print(answer)

def hIndex(pubs):
    n = len(pubs)
    freqs = [0] * (n + 1)

    for pub in pubs:
        if pub >= n:
            freqs[n] += 1
        else:
            freqs[pub] += 1

    total = 0
    i = n
    while i >= 0:
        total += freqs[i]
        if total >= i:
            return i
        i -= 1
    return 0

def hindex2(pubs):
    pubs = sorted(pubs, key=lambda x: -x)
    for i in range(len(pubs)):
        if pubs[i] <= i:
            return i
    return 0


print(hIndex([5, 3, 3, 1, 0]))
# 3
print(hindex2([5, 3, 3, 1, 0]))
# 3
import itertools

def valid(p):
    S, E, N, D, M, O, R, Y = p #initialising 

    send = S * 1000 + E * 100 + N * 10 + D
    more = M * 1000 + O * 100 + R * 10 + E
    money = M * 10000 + O * 1000 + N * 100 + E * 10 + Y

    return send + more == money and M != 0 and S != 0


letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')

for perm in itertools.permutations(range(10), len(letters)):
    if valid(perm):
        print(dict(zip(letters, perm)))
        break

f = open('input.txt', 'r').read().strip().split('\n\n')

origP1, origP2 = [[int(x) for x in q.split('\n')[1:]] for q in f]
p1 = origP1.copy()
p2 = origP2.copy()

def war(p1Cards, p2Cards):
    while len(p1Cards) > 0 and len(p2Cards) > 0:
        a = p1.pop(0)
        b = p2.pop(0)
        if a > b:
            p1.extend([a, b])
        else:
            p2.extend([b, a])
    return p1Cards if len(p1Cards) > 0 else p2Cards

print(sum((i + 1) * x for i, x in enumerate(war(p1, p2)[::-1])))

def recursiveWar(p1Cards, p2Cards, visited):
    while (len(p1Cards) > 0 and len(p2Cards) > 0):
        if (tuple(p1Cards), tuple(p2Cards)) in visited:
            return 1, p1Cards
        
        visited.add((tuple(p1Cards), tuple(p2Cards)))
        a, b = p1Cards.pop(0), p2Cards.pop(0)
        if len(p1Cards) >= a and len(p2Cards) >= b:
            winner, _ = recursiveWar(p1Cards[:a], p2Cards[:b], set())
        else:
            winner = 1 if a > b else 0
        
        if winner == 1:
            p1Cards.extend([a, b])
        else:
            p2Cards.extend([b, a])
        
    return (1, p1Cards) if len(p1Cards) > 0 else (0, p2Cards)

print(sum((i+1) * x for i, x in enumerate(recursiveWar(origP1, origP2, set())[1][::-1])))
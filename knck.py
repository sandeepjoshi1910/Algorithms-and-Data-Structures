

T = 50

W = [10,20,30]

V = {10:60, 20:100, 30:120}

memo = {}

def KS(sum,weight,items):
    if weight in memo.keys():
        return memo[weight]

    if weight == 0:
        return 0
    
    if weight < 0:
        return -1

    vals = []

    for w in W:
        if w not in items:
            vals.append(KS(sum+V[w],weight-w,items[:]+[w]) + KS(sum+V[w],w,items[:]+[w]))
    
    if len(vals) != 0:
        memo[weight] = max(vals) + sum
        
    return max(vals) + sum
    

KS(0,50,[])

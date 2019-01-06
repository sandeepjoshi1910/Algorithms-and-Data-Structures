numdict = {
    2: list("ABC"),
    3: list("DEF"),
    4: list("GHI"),
    5: list("JKL"),
    6: list("MNO"),
    7: list("PQRS"),
    8: list("TUV"),
    9: list("WXYZ")
}

def genMnemonics(num):
    if len(num) == 1:
        return numdict[int(num)]
    
    ans = numdict[int(num[0])]

    res = genMnemonics(num[1:])

    mn = []
    for a in ans:
        for r in res:
            mn.append(a+r)

    return mn

print(genMnemonics("223456"))

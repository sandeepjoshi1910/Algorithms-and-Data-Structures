def stringToInt(s):
    multiply = 1
    if s[0] == '-':
        multiply = -1
        s = s[1:]
    
    mul = len(s)-1

    num = 0

    for ch in s:
        num = num + (10 ** mul) * (ord(ch)-48)
        mul = mul - 1
    
    num = num * multiply

    return num

print(stringToInt("-0000045637560003330003"))

    
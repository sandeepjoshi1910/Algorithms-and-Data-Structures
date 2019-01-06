def numForCh(ch):
    ch = ch.upper()
    return ord(ch) - 65 + 1

def sheetEncoding(sheetNo):
    if len(sheetNo) == 1:
        return numForCh(sheetNo)

    nums = [numForCh(x) for x in sheetNo]

    ans = 0

    for i in range(1,len(sheetNo)):
        ans = ans + 26 ** i
    
    res = 1
    for i in nums:
        res = res * i
    
    return res + ans

print(sheetEncoding('AZ'))
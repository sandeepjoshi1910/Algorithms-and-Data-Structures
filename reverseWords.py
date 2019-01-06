# Reverse all words in a sentence. 
# Ex: "Alice likes bob" --> "bob likes Alice"

def reverseSentence(sent):
    words = sent.split(" ")

    i = 0
    j = len(words) - 1

    while i < j:
        temp = words[i]
        words[i] = words[j]
        words[j] = temp
        i = i + 1
        j = j - 1
    
    res = ""
    for w in words:
        res = res + " " + w
    return  res

print(reverseSentence('I am in coffee alley drinking coffee'))
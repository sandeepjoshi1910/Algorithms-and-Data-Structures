"""

Source: https://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/

Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. 
Determine the maximum value obtainable by cutting up the rod and selling the pieces. 
For example, if length of the rod is 8 and the values of different pieces are given as following, 
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20

"""

priceDict = {1:3, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20}
solutions = {}

def optOfN(n):
    if n in solutions.keys():
        return solutions[n]
    if n == 1:
        solutions[1] = priceDict[1]
        return solutions[1]
        
    opt = [priceDict[n]]
    for i in range(1,int(n/2)+1):
        opt.append(optOfN(i)+optOfN(n-i))

    solutions[n] = max(opt)
    return solutions[n]


optOfN(8)
print(solutions)
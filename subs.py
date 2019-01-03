def getIndices(val,arr):
            indices = []
            for it,item in enumerate(arr):
                if item == val:
                    indices.append(it)
            return indices

def sublist(sub,li):
            if sub == []:
                return False
            if len(sub) > len(li):
                return False
            
            indices = getIndices(sub[0],li)
            is_sub_list = False
            for index in indices:
                broke = False
                for i in range(1,len(sub[1:])+1):
                    try:
                        if sub[i] != li[index+i]:
                            broke = True
                            break
                    except:
                        broke = True
                        break
                if not broke:
                    is_sub_list = True
                    break
            return is_sub_list

print(sublist([-9, 3], [5, -6, 2, 5, 0, -1, -3, -1, 9, -7, 6, -9, 8, 9, -2, 5]))            
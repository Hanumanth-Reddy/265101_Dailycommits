li = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print("input list= ",li)
di = {}
for i in range(len(li)):
    di[i] = li[i]  # di.update({i:li[i]})
print("output dict= ",di)

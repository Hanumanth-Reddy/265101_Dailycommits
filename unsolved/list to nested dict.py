li = [{'name': 'a', 'grade': "I"}, {'name': 'b', 'grade': "II"}, {'name': 'c', 'grade': "III"}]
print("input list=  ", li)
di = {}
for i in range(len(li)):
    di['child' + str(i)] = li[i]
print('output nested dict=  ', di)

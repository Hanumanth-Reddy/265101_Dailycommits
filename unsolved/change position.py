position_list=[1,2,3,4,5,6,7,8,9,0,]
replcae=[]
print(position_list)
for i in range(len(position_list)-1):
    position_list[i]=position_list[i+1]
position_list.pop(len(position_list)-1)
print(position_list)
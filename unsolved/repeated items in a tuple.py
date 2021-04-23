s=(1,2,2,3,4,5,6,6,7,"h","h")
s1=set()
for i in s:
    co=s.count(i)
    if co>1:
        s1.add(i)

print(s1)
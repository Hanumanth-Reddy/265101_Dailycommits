year=int(input("enter year: "))
month=int(input("enter month: "))
day=int(input("enter day: "))
if year%4==0:
    leap=True
else:
    leap=False
if month in (1,3,5,7,8,10,12):
    len=31
elif month==2:
    if leap:
        len=29
    else:
        len=28
else:
    len=30
if day<len:
    day+=1
else:
    day=1
    if month==12:
        month=1
        year+=1
    else:
        month+=1

print("Next date dd/mm/yyyy %d/%d/%d."%(day,month,year))


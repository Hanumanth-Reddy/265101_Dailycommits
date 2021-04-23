slices=int(input("Enter no. of slices: "))
def pizza(n):
    global price
    if n%2==0:
        price = 120*n
        return price
    else:
        price=123*n
        return price


pizza(slices)
print("price of",slices,"slice =",price)
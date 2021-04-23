s = input("Enter a number to check its type like real,complex etc: ")


def fun(input):
    try:
        val = int(input)!=0
        if val:
           print("real")
        else:
            print("zero")
    except ValueError:
        try:
            val = float(input) != 0.
            if val:
              print("float")
            else:
                print("zero")
        except ValueError:
            try:
                val = complex(input)
                if val:
                 print("complex")
                else:
                    raise ValueError
            except ValueError:
                    print("str")


fun(s)

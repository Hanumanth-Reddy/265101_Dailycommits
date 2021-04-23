dic={"lol":"laughing out loud","rofl":"rolling on the floor","lmk":"let me know","smh":"shaking my hand"}
inp=input("enter key to know abbreviation: ")
if inp in dic:
    print(dic[inp])
else:
    print("abbreviation not found")
user = int(input("how many rows?"))
if user>1 and user<25:
    for i in range(9,0,-1):
        print(i*str(i), end="")
else:
    print('Out of range - must be between 1 and 25')
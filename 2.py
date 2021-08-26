h=int(input("mời nhập chiều cao h: "))
for i in range(h):
    for j in range(2*h-1):
        if j==0 or j==2*h-2 or j==h-1 or i==j or i==j-h+1 or j>=h-1 and i==0 or j<h and i==h-1:
            print("*",end="")
        else: print(" ",end="")
    print()
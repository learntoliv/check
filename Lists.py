if __name__ == '__main__':
    n= int(input())
    list =[]
    for _ in range(n):
        type, *rest = input().split()
        if type!= "print":
            type+= "(" + ",".join(rest) + ")"
            eval("list."+type)
        else: print(list)

if __name__ == '__main__':
    n=int(input())
    marksheet = []
    for _ in range (n):
        name = input()
        scores = [float(input()),float(input()),float(input())]
        marksheet.append([name,scores])
    x = input()
    average = 0.0
    for a,b in marksheet:
        if a == x:
            average = (b[0]+b[1]+b[2])/3
    print("{0:.2f}".format(average))


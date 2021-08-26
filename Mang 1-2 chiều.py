import numpy as np

def Taomang2ChieuC1(rows, cols):
    D=[]
    for i in np.arange(rows):
        row =[]
        for i in np.arange(cols):
            row.append(np.random.randint(100))
        D.append(row)
    return D
def TaoMang2chieuC2(rows, cols):
    D= np.random.randint(100,size=(rows,cols))
    return D

arr =np.array([1,2,3,4,5])
arr2= np.array([1,2,3,4,5],dtype='f',ndmin=3)

arr3 = np.array([1,2,3,4,5,6,7,8,9,10], dtype='i')

filter_arr3= arr3%2==0

print(arr3)
print(filter_arr3)
print(arr3[filter_arr3])
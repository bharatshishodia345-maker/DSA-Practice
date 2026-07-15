# time complaxitry
arr1 = [5,8,9,5,6,4]
arr2 = [6,5,4,1,2,3]

for i in arr1:
    for j in arr2:
        for k in range(1000):
            print(('{},{}').format(i,j))
#Data Structures Ch. 2.3
#Big O Notation

#Find min number of list
import time
from random import randrange


#O(n^2)
# def findMin(aList):
#     overallMin = aList[0]
#     for i in aList:
#         isSmallest = True
#         for j in aList:
#             if i > j:
#                 isSmallest = False
#         if isSmallest:
#             overallMin = i
#     return overallMin

#O(n)
def findMin(aList):
    minsofar = aList[0]
    for i in aList:
        if i < minsofar:
            minsofar = i
    return minsofar

# someList = [5,4,2,1,0]
# print(findMin(someList))

for listSize in range(1000,100001,1000):
    aList = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin(aList))
    end = time.time()
    print("size: %d time: %f" % (listSize, end-start))


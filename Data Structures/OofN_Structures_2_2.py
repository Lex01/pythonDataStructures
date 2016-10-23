import timeit
import random

#Different List Generators
# def test1():
#     l = []
#     for i in range(1000):
#         l = l + [i]
#
# def test2():
#     l = []
#     for i in range(1000):
#         l.append(i)
#
# def test3():
#     l = [i for i in range(1000)]
#
# def test4():
#     l = list(range(1000))

# t1 = timeit.Timer("test1()", "from __main__ import test1")
# print("concat ",t1.timeit(number=1000), "milliseconds") #number=1 would give microseconds
# t2 = timeit.Timer("test2()", "from __main__ import test2")#no number parameter defaults to 1000000
# print("append ",t2.timeit(number=1000), "milliseconds")
# t3 = timeit.Timer("test3()", "from __main__ import test3")
# print("comprehension ",t3.timeit(number=1000), "milliseconds")
# t4 = timeit.Timer("test4()", "from __main__ import test4")
# print("list range ",t4.timeit(number=1000), "milliseconds")

#List pop() vs pop(0) time comparison. O(n) vs O(1)
# popzero = timeit.Timer("x.pop(0)",
#                 "from __main__ import x")
# popend = timeit.Timer("x.pop()",
#                "from __main__ import x")
# print("pop(0)   pop()")
# for i in range(1000000,10000001,1000000):
#     x = list(range(i))
#     pt = popend.timeit(number=1000)
#     x = list(range(i))
#     pz = popzero.timeit(number=1000)
#     print("%15.5f, %15.5f" %(pz,pt))

#List vs Dict time comparison. O(n) vs O(1)
for i in range(10000,100001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,
                     "from __main__ import random,x")
    x = list(range(i))
    list_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    dict_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, list_time, dict_time))

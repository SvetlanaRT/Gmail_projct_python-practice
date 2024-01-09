# list = range(0,10)
#
# number = int(input("Enter the nuber: "))
#
#
# def inList (x,list):
#
#     for n in list:
#         if x==n:
#             return True
#     return False


# print(inList(number,list))

# import random
#
# list02=list(map(lambda x: random.randint(0,100),range(10)))
# print(list02)
#
# list03 =[]
#
# for i in range(10):
#
#     list03.append(random.randint(0,50))
#
# print(list03)
#
# max= list03[0]
#
# for i in range(len(list03)):
#     if list03[i] > max:
#         max=list03[i]
#
# print(max)
#
# def findMax (list):
#
#     max=list[0]
#
#     for i in range(len(list)):
#         if list[i] > max:
#             max=list[i]
#
#     print(max)
#
# findMax(list03)

# sortTup

# tupleList=[(1,2,9),(1,0),(1,8),(1,5,-1),(1,3),(1,4,-10)]

# def tupLast(tup):
#     return tup[-1]
#
# def sortedTup(list):
#     return sorted(list, key=tupLast)
#
# print(sortedTup(tupleList))

# list01=["lretl","1vdfg1","dfgf","acvcvbvba"]
#
#
# def sameC(list):
#     total=0
#     for w in list:
#         if len(w)>1 and w[0]==w[-1]:
#             total+=1
#     return total
#
# print(sameC(list01))
#
# for w in list01:
#     if w=="lretl":
#         list01.remove(w)
# print(list01)
list02= [10,20,30,40,50,60,70,80,90,100]

list03=list(filter(lambda x: (x!=100),list02))
print(list03)
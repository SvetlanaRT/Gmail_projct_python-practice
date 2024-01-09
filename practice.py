import copy
import random

# list = [x for x in range(1,11)]
# n= int(input("Please enter the number: "))
#
#
# print(list)
# def num_fun (x,lis):
#     for item in lis:
#         if x == item:
#             return True
#
#     return False
#
# print(num_fun(n,list))
#
# ----------------------------# import random
#
# list01=list(map(lambda x: random.randint(0,100),range(10)))
#
# print(list01)
#
# max= list01[0]
# for i in range(len(list01)):
#     if list01[i]>max:
#         max=list01[i]
# print(max)

# tList=[(2,5),(2,3),(4,4),(3,5),(3,3),(2,1)]
# def lastT(tup):
#     return tup[-1]
#
# def sortLastTup(tup):
#     return sorted(tup, key=lastT)
#
# tList=sortLastTup(tList)
#
# print(tList)


# list01=['adfga','adfg','1fdhgf2','1fgh1','3fgh3','tgjhj']
# list01=["lretl","1vdfg1","dfgf","acvcvbvba"]

# def sameC(list):
#     total=0
#     for w in list:
#         if len(w)>1 and w[0]==w[-1]:
#             total+=1
#     return total
#
# print(sameC(list01))
# list01=[10,20,30,50,40,50,60,70,80,90,100,111111]
#
# for n in list01:
#     max=list01[0]
#     for x in range(len(list01)):
#         if list01[x] > max:
#             max=list01[x]
#
# print(max)



# import random
#
# list02=[]
# for i in range(10):
#     list02.append(random.randint(0,100))
# print(list02)
#
# for n in list02:
#     max=list02[0]
#
#     for i in range(len(list02)):
#         if list02[i]>max:
#             max=list02[i]
#
# print(max)

#
# ind=list01.index(70)
#
# list01[ind]=700
#
# print(list01)

# list01=list(filter(lambda x: (x!=50),list01))

# list01=list(filter(lambda x: (x!=10),list01))
# print(list01)
# def remove100(list):
#     return [x for x in list if x!=100]
# print(remove100(list01))
# def firstLast(list):
#     return(list[1],list[-1])
#
# print(firstLast(list01))
# list02=list(filter(lambda x: (x!=10),list01))
#
# print(list02)

# names=["","olga","sveta"]
#
#
# names=list(filter(None,names))

# for x in names:
#     if len(x)==0:
#         names.remove(x)
# print(names)

# list04=[(1,2),(1,4),(1,3),(1,1)]
#
# def sortT (tuple):
#     return tuple[-1]
#
# def sortL(list):
#
#     return sorted(list, key=sortT)
#
# print(sortL(list04))

# list05=['adfa', 'fljkf','dfgfdg','hlklh','1df1','2df2']
# #
# for w in list05:
#     if w=="adfa":
#         list05.remove(w)
#
# list06=list(reversed(list05))
# print(list06)



# list11=copy.copy(list10)
#
#
# print(list11[0],list11[-1])
#
# print(list11)




# def countPolindrom(list):
#     count_p=0
#     for w in list:
#         if len(w) and w[0]==w[-1]:
#             count_p+=1
#
#     return count_p
# print(countPolindrom(list05))

# def min_max(my_list):
#
#     if not my_list:
#         print("list is empty")
#
#
#     max_num= my_list[0]
#     min_num=my_list[0]
#
#     for n in my_list:
#         if n>max_num:
#             max_num=n
#
#         elif n<min_num:
#             min_num=n
#
#     return min_num, max_num
#
#
# list_for_test =[-1,-10,5,10]
#
# minimum_value,maximum_value=min_max(list_for_test)
#
# if minimum_value is not None and maximum_value is not None:
#     pass
#
# print("Minimum is: {}  Maximum is: {}".format(minimum_value, maximum_value))
import random

# list1  = ['M', 'NA', 'I']
# list2 = ['Y', 'ME', 'Z']
# list3= list(zip(list1,list2))
# list4=[x+y for x,y in list3]
# print(list3)
# print(list4)

# def remove_neg(list_t):
#     return list(filter(lambda x: x>0,list_t ))
# print(remove_neg([-10,10,-20,20]))


# list1=["","q","",""]
# def remove_empty(list_t):
#     return list(filter(lambda x: len(x)>0 ,list_t))
# print(remove_empty(list1))



# list_inlist=[10,20,[300,400,[5000,6000,7000],500],30,40]
# print(list_inlist[0],list_inlist[2][3],'700={}'.format(list_inlist[2][2][2]))

# list_t=[10,20,30,20]
#
# num_index=list_t.index(20)
# list_t[num_index]=200
# print(list_t)


# list_for_test =[-1,-10,5,10,20,-10]
# list1=[x for x in list_for_test if x !=-10]
# list2=list(filter(lambda x: x !=-10, list_for_test))
# print(list1,list2)


# def last_tup(tup):
#     return tup[1]
#
# def sort_list_tup(list_t):
#     return sorted(list_t,key=last_tup)
#
# list1=[(10,10),(1,1),(20,20)]
#
# print(sort_list_tup(list1))


list1=[random.randint(0,20)for _ in range(10)]
print(list1)

def max_min(list_t):
    i=0
    maxim=list_t[0]
    minim=list_t[0]

    for n in list_t:
        i+=1
        if n>maxim:
            maxim=n
        elif n<minim:
            minim=n

    return minim, maxim

list1=[10,20,-10,-20,100]
if list is not None:
    minim,maxim= max_min(list1)
    print(minim,maxim)
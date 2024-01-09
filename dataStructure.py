# var= "James Bond"
# print(var[2::-1])
#
# l1 = [3, 6, 9, 12, 15, 18, 21,100]
# l2 = [4, 8, 12, 16, 20, 24, 28]
#
# l1=l1[1::2]
# l2=l2[0::2]
#
# l3=l1+l2
#
# print(l1)
#
# num=l1.pop(-1)
#
# l2.insert(2,num)
#
# print(l1)
# # print(l2)
#
# l1 = [3, 6, 9, 12, 15, 18, 21,100,100]
# l6 = l1[::-1]
# l4=l1[2::-1]
# print(l4)


# count_dict={}
#
# for n in l1:
#     count_dict[n]=count_dict.get(n,0)+1
#
# print(count_dict)

# l7=list(zip(l1,l6))
# print(l7)

# l7 = {30, 6, 90, 12, 150, 18, 21,100,1100}
# l8 = {3, 6, 9, 12, 15, 18, 21,100,100}
#
# intersection=l7.intersection(l8)
# print(intersection)
# for n in intersection:
#     l7.remove(n)
# print(l7)


# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# roll_number=[x for x in sample_dict.values()]
# print(roll_number)
# l9 = [30, 6, 90, 90, 12, 150, 18, 18, 21, 100, 1100]
#
# l10=tuple(set(l9))
# print(l10)
# def getMax():
#     l9 = [30, 6, 90, 90,12, 150, 18, 18,21,100,1100]
#     max=0
#     for n in l9:
#         if n>max:
#             max=n
#     return max
# print(getMax())
#
# print(max(l9))
# print(min(l9))

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# # print(l1[1::2]+l2[::2])
#
# num=l1.pop(4)
# l2.insert(2,num)
#
# print(l1)
# print(l2)
# --------------------
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# #output #{11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
#
# dict={}
# for n in sample_list:
#    dict[n]=dict.get(n,0)+1
#
# print(dict)

# ================================================
sample_set= {11, 46, 8, 10, 23, 45, 22, 45, 89}
sample_set01 = {11, 45, 8}
print(sample_set)
print(sample_set01)
#
# full_list=list(zip(sample_set01,sample_set))
# print(full_list)
#
# full_list=list(zip(sample_set01,sample_set))
# print(full_list)
#
# -------------------
# intersection=sample_set.intersection(sample_set01)
# for i in intersection:
#    sample_set.remove(i)
# print(sample_set)
# print(intersection)
# -------------------

# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
##output After removing unwanted elements from list [47, 69, 76, 97]
# roll_number[:]=[x for x in sample_dict.values()]
# print(roll_number)
# ------------------------------------------------------------
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# list=list(set([x for x in speed.values()]))
# print(list)
# ----------------------------------------------------------
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97,47, 64, 69, 37, 76, 83, 95, 97]
# roll_number01= tuple(set(roll_number))
# print(max(roll_number01))
# print(min(roll_number01))
# print(type(roll_number01))

# ---------------------------------------------------------------
for n in range (1,11):
    for j in range(1,11):
        print(n*j, end=' ')
    print("\t\t")
# class B:
#     def fruits(self):
#         fruits = ["banana", "apple", "cherry"]
#         fruits = fruits.pop(2)
#         return fruits
#
#
# instanceB = B()
# print(instanceB.fruits())

list1=['m','n','i']
list2=['y','ame','s']
list3=list(zip(list1,list2))
print(list(list3))
# list4=[ x+y for x,y in zip(list1,list2)]
list4=[ x+y for x,y in list3]
print(list4)

list6 = [('a', 1), ('c', 3), ('b', 2)]
list7 = sorted(list6,key=lambda x:x[0])

print(list7)

words1=['hello','Hi']
words2=['dear','sweaty']

words3=[x+y for x in words1 for y in words2]
print(words3)
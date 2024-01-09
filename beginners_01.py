import random


# PRINT SUM,PREVIOUS,CURENT
# def ten_sum():
#     previous=0
#     for curent in range(1,11):
#
#         sum=previous+curent
#         print(f"Previous:{previous}, Curent:{curent}, Sum:{sum}")
#         previous=curent
#
# print(ten_sum())
# ----------------------------
# RETURN PRODUCT or SUM (<1000)
# def sumOrproduct(a,b):
#     produt= a*b
#     if produt>= 1000:
#         return a+b
#     else: return produt
#
#
# print(sumOrproduct(1000,2000))
# print(sumOrproduct(10,20))

# ------------------------------
#PRINT EVEN INDEX
# def even_index(list):
#     for number,index in enumerate(list):
#         print(f"index of {number} is {index}" )
#     print(list)
#     print(list[::2])
#
#
# list10=[x for x in range(1,11)]
#
# print(even_index(list10))
#-------------------------------
# LETTERS in STRING on EVEN index
# def evenI():
#     word=str(input("Enter theword: "))
#     letters=list(word)
#     for l in letters[::2]:
#         i=letters.index(l)
#         print("index of '{}' is {}".format(l,i))
#     print(letters)
#     print(letters[::2])
#
# evenI()
# ------------------------------------------------
#remove letters from start to N  and print new word

# def remove_letters():
#     word=str(input("Enter the word: "))
#     n=int(input("Enter thenumber: "))
#     if n<len(word):
#         new_word=list(word[n:])
#         return (new_word)
#     else: print(" number is bigger than length of the word ")
# print(remove_letters())

#-----------------------------------------------
# LAST & FIRST

# def polind(number):
#     caracters=list(str(number))
#     for c in caracters:
#         if caracters[0]==caracters[-1]:
#             return True
#         else: return False
#
# print(polind(1563))

#---------------------------------------------
# Divisile

# def div5(list):
#     list5=[]
#     for n in list:
#         if n%5==0:
#             list5.append(n)
#     return list5
# print(div5([5,10,55,60,100,22,11]))
#------------------------------------------
#EMMA count
# str_x = "Emma is good developer. Emma is a writer"
# count=str_x.count("Emma")
# print(count)

#------------------------------------------
# Pattern
# for i in range(5):
#     for ii in range(i):
#       print (str(i), end="")
#     print("\n")

# --------------------------------------------------
 #Polindrom

# def polin(number):
#         number=str(number)
#         if number[::]==number[::-1]:
#             print( "This is polindrome" )
#         else: print ("This is not polindrome")
# polin(1224)
#---------------------------------------------------
# two lists even and

# def two_lists(list1,list2):
#     new_list=[]
#     for n in list1:
#         if n%2!=0:
#             new_list.append(n)
#     for n in list2:
#         if n%2==0:
#             new_list.append(n)
#     return new_list
#
# list01=[10,50,20,21,44,33,37]
# list02=[80,90,40,28,36,100,27,23]
#
# print(two_lists(list01,list02))

#----------------------------------------
# EXPONENT
# def exponent(base,exp):
#      print( "ansver:"  +str (base**exp))
# exponent(2,5)

#--------------------------------------
#half piramide downward

# def halfPiramide():
#
#     for i in range(6,1,-1):
#         for ii in range(1,i):
#             print ("*", end="")
#         print('\t')
#
# halfPiramide()

# --------------------------------------
# table multiplication 10

# for a in range(1,11):
#     for b in range(1,11):
#         print(a*b, end='\t')
#
#     print()

# ------------------------------------------
# If the given int is 7536, the output shall be “6 3 5 7"

# def revers_order():
#     number = input(str("enter the number:"))
#
#     print(number[::-1])

# revers_order()
# --------------------------------------------
# list of devided_By5
# def devided_by5(list):
#     new_list=[]
#     for n in list:
#         if n%5==0:
#             new_list.append(n)
#     return new_list
# print(devided_by5([10,11,12,60,15,20]))
#--------------------------------------------
#Last_First

# def Last_first(list):
#     for n in list:
#         if list[0]==list[-1]:
#             return True
#         else: return  False
#
# print(Last_first(list("12341")))
# ---------------------------------------
# def short_string(n,string):
#     if n <len(string):
#       new_string=string[n:]
#       return new_string
#     else:
#       print("n can't be bigger than length of word")
#
#
# print(short_string(2,"svetlana"))
#----------------------------------------------------------

#caracter on even idex

# def index_even(string):
#     list01=list(string)
#     string01= ''.join(list01[::2])
#     print(list01[::2])
#     print(string01)
#
# print(index_even("0123456789"))

# def tenNumbers():
#
#     prev_number=0
#     for n in range(1,11):
#         sum=prev_number+n
#         print("number:"+str(n),"previous number:"+str(prev_number),"sum:"+str(sum), end='\n')
#         prev_number=n
# tenNumbers()
# --------------------------------------------
# print File
# def print_file():
#     file_path="/home/svetlanakalchenko/PycharmProjects/Gmail_project/file.txt"
#     try:
#
#         with open(file_path,"r") as file:
#             content=file.read()
#             print(content)
#     except FileExistsError:
#         print(f"file not found, path:{file_path}")
#
#     except Exception as e:
#         print("Error")
# print_file()
#--------------------------------------------

# list01=[10,20,11,3,25,31]
# list02=list(map(lambda x: x  if  x%5==0 else None,list01))
# list03=[ x/4 for x in list01]
# print(list03)
# print(list02)
# list04=[x**4 for x in list01]
# print(list04)
# --------------------------------------------
# target_value=10
# if target_value in list01:
#     print(f"target value : {target_value} is in the list")

# ----------------------------------------------
#dict of caracters in the
# string_my="svetlana"
# count_list={}
#
# for l in string_my:
#     count_list[l]=count_list.get(l,0)+1
# print(count_list)


# list0 = [2,2,2,3,4,5,5,5,6,]
# list01=list(set(list0))
# print(list01)
# --------------------------------------------------------------------------
# my_dict={}
# name="svetlanaKalchenko"
# for l in name:
#     my_dict[l]=my_dict.get(l,0)+1
# print(my_dict)
#
# def key_tosort(item):
#     return item[1]
# def sortdic(dictionary):
#     sorted_dictionary=sorted(dictionary.items(),key=key_tosort,reverse=False)
#     return dict(sorted_dictionary)
#
# print(sortdic(my_dict))
# print(my_dict["s"])

# ------------------------------------------------
#
# mytuple=("apple","banana","cherry")
#
# fruit=iter(mytuple)
#
# print(next(fruit),next(fruit))
import random

#
# def sumOrMul(a,b):
#     if a >= 10 or b>=10:
#         return a+b
#     else:
#         return a*b
#
# print(sumOrMul(10,12))
# print(sumOrMul(2,3))
#
# def preductDepend(a,b):
#     product = a*b
#     if product>=1000:
#         return a+b
#     else:return product
#
#
# print(preductDepend(1000,2000))
# print(preductDepend(10,20))

# def printSum():
#     previous=0
#     for curent in range(1,11):
#         sumoftwo = previous+curent
#         print(f"Previous: {previous} , Current: {curent} , Sum: {sumoftwo}")
#         previous=curent
#
# printSum()


# list01=[random.randint(1,10) for x in range(10)]

# def calc_numbers():
#     sum=0
#     for n in range(0,11):
#         sum+=n
#     return sum
#
# print(calc_numbers())

list=[x for x in range(4,31)]
print(list[1::2])
print(list[::2])

print(max(list))


string_with_whitespace = "   Hello, World!   "
stripped_string = string_with_whitespace.strip()

print(stripped_string)

string_wsp="    string    "
print(string_wsp.strip())
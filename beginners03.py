# def prod_or_sum(a,b):
#     if a*b >= 1000:
#         return a+b
#     else: return a*b
#
# print(prod_or_sum(10,2))

# =============================================
def sum_previous():
    pr_numberr=0
    su=0
    for n in range(1,11):
        su=n+pr_numberr
        pr_numberr=n
    print(su)

sum_previous()
# --------------------------------------
list=[10, 20, 33, 46, 55]
list=[x for x in list if x%5==0  ]


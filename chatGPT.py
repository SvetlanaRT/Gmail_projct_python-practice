# def find_max(lst):
#     return max(lst)
#
# def find_min(lst):
#     return min(lst)
#
# def max_array(arr):
#     return max(arr)
#
# def find_index_of_max(lst):
#     return lst.index(max(lst))
#
# def max_dict(dic):
#     return max(dic.values())
#
# print(max_dict({"first":10,"second":20,"third":30}))

# ------------------------------------------------------
def max_product(nums):
    nums.sort()
    # return max(nums[-1] * nums[-2], nums[0] * nums[1])
    return (nums[-1] * nums[-2], nums[0] * nums[1])

# Example usage
example_nums = [-10, -3, 5, 2, 7, -8, -4]
result = max_product(example_nums)

print(f"The maximum product of two integers in the array is: {result}")

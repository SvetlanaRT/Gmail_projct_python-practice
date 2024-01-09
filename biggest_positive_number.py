def solution(A):
    # Filter out non-positive integers and duplicates
    A = set(x for x in A if x > 0)

    # If the filtered array is empty, return 1
    if not A:
        return 1

    # Find the smallest positive integer not in the filtered array
    max_value = max(A)
    for i in range(1, max_value + 2):
        if i not in A:
            return i

# Test cases
print(solution([1, 3, 6, 4, 1, 2]))  # Output: 5
print(solution([1, 2, 3]))           # Output: 4
print(solution([-1, -3]))            # Output: 1




def add_num(arr):
    arr = set(x for x in arr if x>0)
    if not arr:
        print ("error! invalid input")
    max_num= max(arr)

    for n in range(max_num+2):
        if n not in arr:

            print(arr)























































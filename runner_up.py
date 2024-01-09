# if __name__ == '__main__':
#     x, y, z, n = map(int, input().split())
#
#     # Using list comprehension to generate coordinates
#     coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
#
#     # Print the list of coordinates
#     print(coordinates)


# def max_min():
#
#     n = input("enter number of scores: ")
#     scores=list(map(int,input("enter scores: ").split()))
#     print(scores)
#
#     if n is not None and scores is not None:
#         max_score=scores[0]
#         min_score=scores[0]
#         for sc in scores:
#             if sc > max_score:
#                 max_score=sc
#             elif sc < min_score:
#                 min_score=sc
#
#         return max_score,min_score
#     else: print("Error! Invalid parameters")
#
# my_max,my_min=max_min()
#
# if my_max is not None and my_min is not None:
#     print("Maximum is: {}, Minimum is: {} ".format(my_max,my_min))




def runner_up():
    n = int(input("enter n: ").strip())
    scores=list(map(int,input("enter scores: ").split()))
    if n is not None and scores is not None:
        scores = sorted(set(scores), reverse=True)
    else:
        print("Error! Invalid input")
    print(scores)
    return scores[1]
my_runner_up=runner_up()

if my_runner_up is not None:
    print("runner_up is: {}".format(my_runner_up))


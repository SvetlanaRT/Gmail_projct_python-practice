# # Taking input for the scores
# scores_str = input("Enter the scores separated by spaces: ")
#
# # Splitting the input string into a list of strings
# scores = list(map(int, scores_str.split()))
# print(scores)
# # Finding the unique scores and sorting them in descending order
# unique_scores = sorted(set(scores), reverse=True)
#
# # The second element in the sorted list is the runner-up score
# runner_up_score = unique_scores[1]
#
# # Print the runner-up score
# print("Runner-up score:", runner_up_score)



def run_up():
    arr= list(map(int, input("enter scores: )").strip().split()))
    if arr is not None:
        arr=sorted(set(arr),reverse=True)
    else: print("Error! Invalid input")
    return arr[1]


my_runner_up=run_up()

if my_runner_up is not None:
    print("Second place has : {}".format(my_runner_up))




















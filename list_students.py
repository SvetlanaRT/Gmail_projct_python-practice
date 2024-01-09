num_students=int(input("Enter number of studenst: "))
student_list=[]

for _ in range(num_students):
    name=input("Enter name of the student: ")
    score = float(input("Enter score of the student"))
    if name is not None and score is not None:
        student_list.append([name,score])



    else: print("Error! Invalid Input ")





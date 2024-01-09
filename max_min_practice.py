def max_min(arr):

    if arr is not None:
        max_num=arr[0]
        min_num=arr[0]

        for n in arr:


            if n > max_num:
                max_num=n

            elif n < min_num:
                min_num=n
        return max_num, min_num


    else:
        print("Arr can't be empty")

my_list= [-1,-2,10,40]

my_maximum,my_minimum = max_min(my_list)

if my_maximum is not None and my_minimum is not None:
    print("Maximum is {} , Minimum is {} ".format(my_maximum,my_minimum))




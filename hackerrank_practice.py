if __name__ == '__main__':
    number = int(input().strip())

if number % 2 != 0:
    print("Wierd")
elif number % 2 == 0 and 2 <= number <= 5:
    print("Not Wierd")
elif number % 2 == 0 and 6 <= number <= 20:
    print("Wierd")
elif number % 2 == 0 and number > 20:
    print("Not Wierd")

else: print("out of scope")

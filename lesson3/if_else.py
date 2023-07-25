first_num = int(input("Enter first number"))
second_num = int(input("Enter second number"))
#       '5'     >    '10'
if first_num > second_num:
    print(True)
    print("first number more than second number")
elif first_num < second_num:
    print(False)
    print("second number more than first number")
else:
    print("Equal")

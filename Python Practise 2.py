number = int(input("Enter a number: "))
min_num = int(input("Enter the min mumber from where you will divide: "))
max_num = int(input("Enter the max mumber from which you will divide: "))

# Error handling
if min_num == max_num:
    print("Range is not valid or invalid")
    exit()
else:
    pass

for i in range(min_num,max_num+1):
    if number%i == 0:
        print(f"{i} is the diviser of {number}")
    else:
        print(f"{i} is not the diviser of {number}")
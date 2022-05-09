def find_max(num1, num2):
    max_num = -1
    # Write your logic here
    if num1 == num2:
        return -1
    for num in range(num1, num2 + 1):
        if len(str(num)) != 2 or num % 5 != 0:
            continue
        sum = num % 10 + num // 10
        if sum % 3 == 0:
            max_num = num
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)

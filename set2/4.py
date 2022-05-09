# find the sum of numbers divisible by 4


choice = "y"
sum = 0
while choice == "y":
    num = int(input("Enter a number: "))
    if num % 4 == 0:
        sum += num
    choice = input("Do you want to continue? (y/n) ")

print("The sum of numbers divisible by 4 is: ", sum)

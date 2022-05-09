def find_product(*num):
    product = 1
    # write your logic here
    # for i,num in enumerate(num):
    #     if i == 0:
    #         if num != 7:
    #             product *= num
    #     elif i == 1:
    #         if num != 7:
    #             product *= num
    #         else:
    #             product = 1
    #     elif i == 2:
    #         if num != 7:
    #             product *= num
    #         else:
    #             product = -1
    # return product
    if 7 in num:
        ind = num.index(7)
        if num[-1] == 7:
            return -1
    else:
        ind = -1

    for i in range(ind+1, len(num)):
        product *= num[i]

    return product


# Provide different values for num1, num2, num3 and test your program
product = find_product(7, 8, 2)
print(product)

# check whether a given three digit number is an Armstrong number.


def armstrong(num):
    temp = num
    sum = 0
    while num != 0:
        rem = num % 10
        sum += rem ** 3
        num = num // 10
    if temp == sum:
        return True
    else:
        return False


print(armstrong(153))

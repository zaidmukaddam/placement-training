# find if a number is palindrome or not


def palindrome(num):
    temp = num
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    if temp == rev:
        return True
    else:
        return False


print(palindrome(12321))

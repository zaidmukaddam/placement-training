# lex_auth_01269446157664256093

def check_prime(number):
    count = 0
    for i in range(2, number):
        if number % i == 0:
            count += 1
    return count == 0
 # if the number is prime return true, else return false


def rotations(num):
    if num < 10:
        return[num]
    if num < 100:
        return [num, int(str(num)[::-1])]
    if num < 1000:
        return [num, int(str(num)[1:]+str(num)[0]), int(str(num)[-1]+str(num)[:-1])]

#     It should return the list of different combinations of digits of the given number.
#     Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]


def get_circular_prime_count(limit):
    l = []
    for i in range(2, limit):
        if check_prime(i):
            x = rotations(i)
            count = 0
            for j in x:
                if check_prime(j):
                    count += 1
            if count == len(x):
                l.append(i)
    return len(l)


# Provide different values for limit and test your program
print(get_circular_prime_count(1000))

# write a program ro find smallest of three numbers


def smallest(a, b, c):
    if a < b:
        if a < c:
            return a
        else:
            return c
    elif b < c:
        return b
    else:
        return c

print(smallest(1, 2, 3))

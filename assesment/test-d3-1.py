from decimal import Decimal, ROUND_HALF_UP


def NumberSearch(strParam: str):

    digits = 0
    letters = 0

    for c in strParam:
        if c.isdigit():
            digits += int(c)
        if c.isalpha():
            letters += 1

    # code goes here
    return Decimal(digits/letters).to_integral_value(rounding=ROUND_HALF_UP)


# keep this function call here
print(NumberSearch(input()))

# https://coderbyte.com/results/userpa9tpdkc2:Number%20Search:Python3

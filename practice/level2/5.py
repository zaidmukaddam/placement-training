# lex_auth_0127136373866577921209

def integer_to_english(number):
    # start writing your code here
    single_digits = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        0: 'zero',
    }
    tens_digits = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }

    tens_multiple = {
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }

    tens_power = {
        100: 'hundred and',
        1000: 'one thousand',
    }

    if number < 0 or number > 1000:
        return -1
    elif number in single_digits:
        return single_digits[number]
    elif number in tens_digits:
        return tens_digits[number]
    elif number in tens_multiple:
        return tens_multiple[number]
    elif number in tens_power:
        return tens_power[number]
    elif number % 100 == 0:
        return single_digits[number // 100] + ' hundred'
    elif number // 100 > 0:
        return single_digits[number // 100] + ' ' + tens_power[100] + ' ' + integer_to_english(number % 100)
    elif number // 10 > 1:
        return tens_multiple[number // 10 * 10] + ' ' + integer_to_english(number % 10)
    else:
        return tens_digits[number]


number = 789
print(integer_to_english(number))

# lex_auth_0127136447430656001216

def convert_to_roman(num):
    # Start writing your code here
    m = ["", "M", "MM", "MMM", "MMMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    # Converting to roman
    thousands = m[num // 1000]  # DIVIDE to give 1000 place
    # find remainder and divide with 100 place
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]  # find remainder and divide with 10 place
    ones = i[num % 10]  # finally remainder

    ans = (thousands + hundreds +
           tens + ones)

    return ans


for num in range(1, 5000):
    print(num, " : ", convert_to_roman(num))

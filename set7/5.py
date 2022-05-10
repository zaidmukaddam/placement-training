# lex_auth_01269443664174284882
def nearest_palindrome(number):
    # start writitng your code here
    number = number+1
    s = str(number)
    while(s != s[::-1]):
        number = number+1
        s = str(number)
    return number


number = 12300
print(nearest_palindrome(number))

# lex_auth_01269438594930278448

def find_pairs_of_numbers(num_list, n):
    count = 0
    for num in num_list:
        if n - num in num_list:
            count = count + 1

    return count // 2
    # Remove pass and write your logic here


num_list = [1, 2, 4, 5, 6]
n = 6
print(find_pairs_of_numbers(num_list, n))

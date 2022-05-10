# lex_auth_01269442545042227276

def find_ten_substring(num_str):
    pairs = []
    sum = 0

    for i in range(0, len(num_str)):
        sum = 0

        for j in range(i, len(num_str)):
            sum = sum + int(num_str[j])

            if(sum == 10):
                pairs.append(num_str[i: j + 1])

            if(sum > 10):
                break

    return pairs


num_str = "2825302"
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print(result_list)

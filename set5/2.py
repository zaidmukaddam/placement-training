#lex_auth_0127382164803993601239

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func == None:
        return sum(list_of_num)

    elif filter_func == even:
        e = even(list_of_num)
        return sum(e)

    elif filter_func == odd:
        o = odd(list_of_num)
        return sum(o)

    else:
        pass #Remove pass and write the logic here

def even(data):
    even = []

    for num in data:
        if num % 2 == 0:
            even.append(num)
        else:
            continue

    return even #Remove pass and write the logic here

def odd(data):
    odd = []

    for num in data:
        if num % 2 != 0:
            odd.append(num)
        else:
            continue

    return odd #Remove pass and write the logic here

sample_data = range(1,11)

print(sum_of_numbers(sample_data,None))

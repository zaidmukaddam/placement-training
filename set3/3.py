def create_largest_number(number_list: list):
    number_list.sort(reverse=True)
    largest_number = ""
    for i in number_list:
        largest_number += str(i)
    return int(largest_number)
    # remove pass and write your logic here


number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)

# lex_auth_0127136216235950081185

def ducci_sequence(test_list, n):
    # start writing your code here
    final_list = []
    for i in range(n+1):
        temp = []
        for x in range(-1, -5, -1):  # take sub in reverse order and in negative range
            temp.insert(0, abs(test_list[x]-test_list[x+1]))
        test_list = temp
        final_list.append(temp)
    return final_list[n]


ducci_element = ducci_sequence([0, 653, 1854, 4063], 3)
print(ducci_element)

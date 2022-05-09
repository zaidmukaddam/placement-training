def find_correct(word_dict: dict):
    # start writing your code here
    output_list = [0, 0, 0]
    for correct_spelling, contestant_spelling in word_dict.items():
        count = 0
        if len(correct_spelling) != len(contestant_spelling):
            output_list[2] += 1
            continue
        for i in range(len(correct_spelling)):
            if correct_spelling[i] != contestant_spelling[i]:
                count += 1

        if count == 0:
            output_list[0] += 1
        elif count <= 2:
            output_list[1] += 1
        else:
            output_list[2] += 1

    return output_list


word_dict = {'VENDOR': 'VENDING', 'RADIO': 'RADICAL', 'MIND': 'MUND', 'CHECK': 'CHEK', 'ALWAYS': 'ALLISWELL'}
print(find_correct(word_dict))

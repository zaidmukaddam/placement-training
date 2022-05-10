def PairSearching(num):
    steps, nums, num_lists = 0, [num], [list(str(num))]
    while True:
        for digits in '0123456789':
            if any(2*digits in ''.join(num_list) for num_list in num_lists):
                return steps

        steps += 1
        new_nums, new_nums_lists = [], []

        for num, num_list in zip(nums, num_lists):
            for digit in str(num):
                new_nums.append(num*int(digit))
                new_nums_lists.append(num_list + list(str(num*int(digit))))
        nums, num_lists = new_nums, new_nums_lists


# keep this function call here
print(PairSearching(input()))

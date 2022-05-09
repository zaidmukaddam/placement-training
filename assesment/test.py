def ArrayAdditionI(arr: list):
    # code goes here
    arr.sort()

    m = dict()

    def sum_check(n, sum):
        if n == 0:
            return "false"
        if n == 1:
            return arr[0] == sum
        if (n, sum) in m.keys():
            return m[(n, sum)]
        else:
            f = sum_check(n-1, sum) or sum_check(n-1, sum - arr[n-1])
            return f
    
    return sum_check(len(arr)-1, arr[-1])


# keep this function call here
print(ArrayAdditionI([1,2,3,4,5,10]))

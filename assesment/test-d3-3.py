def StringZigzag(strArr):
    rows, word = int(strArr[1]), strArr[0]
    output = ['']*rows

    row = 0
    inc = False

    for ch in word:
        output[row] += ch

        if row == 0 or row == rows - 1:
            inc = not inc
        if rows > 1:
            row += 1 if inc else -1

    # code goes here
    return ''.join(output)


# keep this function call here
print(StringZigzag(input()))

# https://coderbyte.com/results/usercf9eei6u5:String%20Zigzag:Python3

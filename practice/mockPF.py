def list_rotate(uniquecode_list):
    rotated_list = []

    for code in uniquecode_list:
        splitCode = code.split("-")

        x = splitCode[0]
        y = splitCode[1]

        alphaCount = 0
        for ch in x:
            if ch.isalpha():
                alphaCount = alphaCount + 1
        if(alphaCount == 1):
            rotated_list.append(x[0:1] + y[1:4] + y[0:1])
        else:
            rotated_list.append(x[0:2] + y[2:4] + y[0:2])

    return rotated_list

#You may modify the below code for testing
uniquecode_list=['GT21-1011','S621-9699']
rotated_list = list_rotate(uniquecode_list)
print(rotated_list)

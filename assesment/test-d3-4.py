def EightQueens(strArr):
    x = list([[int(i) for i in p[1:-1].split(',')[0]] for p in strArr])
    y = list([[int(i) for i in p[1:-1].split(',')[1]] for p in strArr])

    ql = []

    for i in range(0, len(strArr)):
        ql.append((x[i][0], y[i][0]))

    for i in range(0, len(x)-1):
        for j in range(i-1, len(x)):
            x1, y1 = ql[i]
            x2, y2 = ql[j]
            if x1 == x2 or y1 == y2 or (x1 == y1 and x2 == y2) or x1 - y1 == x2 - y2:
                return '(' + str(x1) + ',' + str(y1) + ')'
    # code goes here
    return "true"


# keep this function call here
print(EightQueens(input()))

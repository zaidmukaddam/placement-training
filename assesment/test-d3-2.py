def BracketMatcher(strParam):

    bracs = []

    for i in strParam:
        if i == "(":
            bracs.append(i)
        if i == ")":
            if not bracs:
                return 0
            else:
                bracs.pop()

    if len(bracs) == 0:
        return 1

    # code goes here
    return 0


# keep this function call here
print(BracketMatcher(input()))

# https://coderbyte.com/results/userpa9tpdkc2:Bracket%20Matcher:Python3

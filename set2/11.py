def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = heads
    rabbit_count = 0

    # Start writing your code here
    # Populate the variables: chicken_count and rabbit_count
    while not (chicken_count * 2 + rabbit_count * 4 == legs) and chicken_count != 0:
        chicken_count -= 1
        rabbit_count += 1

    if chicken_count * 2 + rabbit_count * 4 == legs:
        print(chicken_count, rabbit_count)
    else:
        print(error_msg)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    # print(chicken_count,rabbit_count)
    # print(error_msg)


# Provide different values for heads and legs and test your program
solve(35, 94)

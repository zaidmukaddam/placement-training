def find_leap_years(given_year):

    # Write your logic here
    list_of_leap_years = []
    count = 1
    while count <= 15:
        if not given_year % 4 and given_year % 100 or not given_year % 400:
            list_of_leap_years.append(given_year)
            count += 1
        given_year += 1
    return list_of_leap_years


list_of_leap_years = find_leap_years(2000)
print(list_of_leap_years)

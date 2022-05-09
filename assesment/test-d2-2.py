def ThirdGreatest(strArr):
  # code goes here
  try:
    strArr.sort(reverse=True, key = len)
    return strArr[2]
  except(AttributeError, TypeError):
    return -1

# keep this function call here
print(ThirdGreatest(input()))

# https://coderbyte.com/results/userca5f7ue7d:Mean%20Mode:Python3
# https://coderbyte.com/results/userca5f7ue7d:Third%20Greatest:Python3

def MeanMode(arr):
  mean = sum(arr) / len(arr)

  t = {}

  for i in range(0,len(arr)):
    num = arr[i]
    if num in t:
      t[num] += 1
    else:
      t[num] = 1

  ans = {"number": '', "count": 0}

  for n in t:
    if t[n] > ans["count"]:
      ans["count"] = t[n]
      ans["number"] = n

  if ans["number"] == mean:
    return 1
  else:
    return 0

# keep this function call here
print(MeanMode(input()))

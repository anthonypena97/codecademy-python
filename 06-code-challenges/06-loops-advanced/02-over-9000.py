# MY SOLUTION
def over_nine_thousand(lst):
  sum = 0
  if len(lst) == 0:
    return 0
  else:
    for i in lst:
      sum += i
      if sum > 9000:
        return sum
    if sum < 9000:
      return sum

print(over_nine_thousand([8000, 900, 120, 5000]))

# CODECADEMY SOLUTION
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum
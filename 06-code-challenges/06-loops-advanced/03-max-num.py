def max_num(lst):
  max_value = lst[0]
  for i in lst:
    if i > max_value:
      max_value = i
  return max_value

print(max_num([50, -10, 0, 75, 20]))
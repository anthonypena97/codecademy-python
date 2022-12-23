# MY SOLUTION
def remove_middle(lst, start, end):
  x = lst[:start]
  y = lst[end+1:]
  return x + y

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# CODECADEMY'S SOLUTION
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]
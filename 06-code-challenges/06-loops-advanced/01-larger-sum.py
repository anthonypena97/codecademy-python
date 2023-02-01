#Write your function here
def larger_sum(lst1, lst2):
  x = 0
  y = 0
  for i in lst1:
    x += i
  for i in lst2:
    y =+ i
  if x >= y:
    return lst1
  else:
    return lst2


#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
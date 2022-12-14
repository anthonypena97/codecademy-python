# MY SOLUTION
def double_index(lst, index):
  new_lst = []
  i = 0
  for e in lst:
    if i == index:
      new_lst.append(e * 2)
    else:
      new_lst.append(e)
    i += 1
  return new_lst
  
print(double_index([3, 8, -10, 12], 2))

# CODECADEMY'S SOLUTION
def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list 
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst
  
# THIS SOLUTION USES SLICING
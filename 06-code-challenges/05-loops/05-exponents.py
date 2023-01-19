def exponents(bases, powers):
  new_list = []
  for i in range(len(bases)):
    for x in range(len(powers)):
      new_list.append(bases[i] ** powers[x])
  return new_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst
  
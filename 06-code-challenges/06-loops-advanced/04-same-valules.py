#Write your function here
def same_values(lst1, lst2):
  matching = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      matching.append(i)
  return matching


#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
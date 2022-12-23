# MY SOLUTION
def every_three_nums(start):
  answer = []
  index = start
  if(start > 100):
    return answer
  else:
    while(index <= 100):
      answer.append(index)
      index += 3
    return answer

print(every_three_nums(91))

# CODECADEMY'S SOLTION
def every_three_nums(start):
  return list(range(start, 101, 3))

# We can write the body of this function in one line by nesting the range() function inside of the list() function. The range function accepts the starting number, the ending number (exclusive), and the amount to increment by.

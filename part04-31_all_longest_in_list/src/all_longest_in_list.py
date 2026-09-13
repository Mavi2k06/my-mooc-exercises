def all_the_longest(my_list):
  largest = my_list[0]
  number = []

  for num in my_list:
    if len(num) > len(largest):
      largest = num
      number = [num]
    elif len(num) == len(largest):
      number.append(num)

  return number

if __name__ == "__main__":
  my_list = ["first", "second", "fourth", "eleventh"]

  result = all_the_longest(my_list)
  print(result) # ['eleventh']
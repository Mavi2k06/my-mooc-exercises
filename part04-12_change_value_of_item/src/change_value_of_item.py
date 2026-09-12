my_list = [1,2,3,4,5]
while True:
    index = int(input("Index:"))
    if index == -1:
        break
    input_value = int(input("New value:"))
    my_list[index] = input_value
    print(my_list)
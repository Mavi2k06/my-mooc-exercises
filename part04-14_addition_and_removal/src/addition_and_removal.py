list = []
num = 1

while True:
    add_list = input("a(d)d, (r)emove or e(x)it:")
    print(f"The list is now {list}")
    if add_list == "d":
        list.append(num)
        num += 1
    elif add_list == "r":
        if list:
            list.pop()
            num -= 1
    if add_list == "x":
        break
print("Bye!")
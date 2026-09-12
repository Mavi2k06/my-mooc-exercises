number = int(input("How many items:"))
items = []
num = 1
while num <= number:
    item = int(input(f"Item {num}:"))
    items.append(item)
    num += 1

print(items)
def line(times , string):
    if string == "":
        print("*" * times)
    else:
        print(string[0] * times)

def square(size, character):
    num = 1
    while num <= size:
        line(size, character)
        num += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
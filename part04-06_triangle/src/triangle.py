def line(times , string):
    if string == "":
        print("*" * times)
    else:
        print(string[0] * times)
def triangle(size):
    num = 1
    while num <= size:
        line(num, "#")
        num += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)

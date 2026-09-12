def spruce(size):
    print("a spruce!")
    stars = 1
    spaces = size - 1
    while stars <= 2 * size - 1:
        print(" " * spaces + "*" * stars)
        stars += 2
        spaces -= 1
    
    print(" " * (size - 1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
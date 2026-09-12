def same_chars(string , a, b):
    if a < len(string) and b < len(string):
        if string[a] == string[b]:
            return True
        else:
            return False
    else:
        return False
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))
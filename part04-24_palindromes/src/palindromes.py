def palindromes(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False
    return True

def main():
    while True:
        word = input("Please type in a palindrome:")

        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")

main()
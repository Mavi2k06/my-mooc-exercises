def anagrams(string1, string2):
        srt1 = sorted(string1)
        srt2 = sorted(string2)
        if srt1 == srt2:
            return True
        else:
            return False

if __name__ == "__main__":
        print(anagrams("tame", "meta")) 
        print(anagrams("tame", "mate"))
        print(anagrams("tame", "team"))
        print(anagrams("tabby", "batty"))
        print(anagrams("python", "java"))
if __name__ == '__main__':
    s = input()

    functions = [str.isalnum , str.isalpha, str.isdigit, str.islower, str.isupper]

    for f in functions:
        result = False
        for ch in s:
            if f(ch):
                result = True
                break
        print(result)

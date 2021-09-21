def isBin(string : str) -> bool:
    for s in string:
        if s not in ['1', '0', '.']:
            return False
    return True

def text2bin(string : str) -> str:
    res = ""
    for s in string:
        r = bin(ord(s))
        res += r[2:] + '.'
    res = res[:len(res)-1]
    return res

def bin2text(string : str) -> str:
    res = ""
    array = string.split('.')
    for val in array:
        r = chr(int(val, 2))
        res += r
    return res


def main():
    string = ""
    while True:
        string = input("> ")

        if string == "exit":
            break

        if isBin(string):
            print("Расшифровано: {0}\n".format(bin2text(string)))
        else:
            print("Зашифровано:\n{0}\n".format(text2bin(string)))

main()
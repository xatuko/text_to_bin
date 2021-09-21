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
        
        try:
            action, message = string.split(' ', 1)
            if action == "code":
                print(text2bin(message))
            if action == "decode":
                print(bin2text(message))
        except:
            print("Ввел хуйню")
            
main()
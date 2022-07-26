def get_number(text: str, error_text = 'Wrong input. Try again -> ', min=1, max=28) -> int:
    print(text, end='')
    while True:
        numb = input()
        if numb.isdigit():
            numb = int(numb)
            if min <= numb <= max:
                return numb
            else: print(error_text, end='')
        else: print(error_text, end='')


def read_file(filename: str) -> str:
    res = ''
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            res += line
    return res


def write_file(filename: str, text: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

from functions import read_file, write_file

def code(text: str) -> str:
    res = ''
    count = 0
    for i in range(len(text)):
        if i == len(text)-1:
            res += f'{count}x{text[i]}, '
            return res[:-2]
        if text[i] == text[i+1]:
            count += 1
        else:
            count +=1 
            res += f'{count}x{text[i]}, '
            count = 0


def decode(text: str) -> str:
    res = ''
    elements = text.split(', ')
    for elem in elements:
        count = int(elem[0])
        symbol = elem[-1]
        for i in range(count):
            res += symbol
    return res


text = read_file('file.txt')

codding = code(text)
decodding = decode(codding)

print(f'Origin text - {text}')
print(f'Codding text - {codding}')
print(f'Decodding text - {decodding}')

write_file('output.txt', codding)
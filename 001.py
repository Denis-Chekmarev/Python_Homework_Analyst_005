# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

text = 'абвгдейка - это передача'
new_text = ' '.join(filter(lambda x: 'абв' not in x, text.split()))
print(new_text)
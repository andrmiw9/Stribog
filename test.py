def text_bin(s: str) -> str:
    return ' '.join(f"{ord(i):08b}" for i in s)


def text_to_bin(text):
    return ' '.join(format(x, '08b') for x in bytearray(text, 'utf-8'))


a = 'ПИПИСКА АНТОНА'
print(text_bin(a), end='\n\n')
print(text_to_bin(a))

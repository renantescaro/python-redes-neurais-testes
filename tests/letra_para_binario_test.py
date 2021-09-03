
def binario(caracter):
    return str(format(ord(str(caracter)), '07b'))


print(binario('1'))
print(binario('a'))
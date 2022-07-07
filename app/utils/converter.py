

class Converter:

    @staticmethod
    def bits_para_caracter(bits:str) -> str:

        unicode_str = chr(int(bits, 2))

        if len(unicode_str) == 1 and unicode_str.isalpha():
            return unicode_str

        dicionario_numeros = {
            '00000000': '0',
            '00000001': '1',
            '00000010': '2',
            '00000011': '3',
            '00000100': '4',
            '00000101': '5',
            '00000110': '6',
            '00000111': '7',
            '00001000': '8',
            '00001001': '9',
        }
        return dicionario_numeros[bits]

import os


class TelaBase:
    manter_na_tela = True
    cor = ''

    def bold(self):
        self.cor += '\033[1m'
        return self

    def branco(self):
        self.cor += '\033[97m'
        return self

    def Branco(self):
        self.cor += '\033[107m'
        return self

    def preto(self):
        self.cor += '\033[30m'
        return self

    def Preto(self):
        self.cor += '\033[40m'
        return self

    def azul(self):
        self.cor += '\033[34m'
        return self

    def Azul(self):
        self.cor += '\033[44m'
        return self

    def azul_leve(self):
        self.cor += '\033[94m'
        return self

    def Azul_leve(self):
        self.cor += '\033[104m'
        return self

    def verde(self):
        self.cor += '\033[32m'
        return self

    def Verde(self):
        self.cor += '\033[42m'
        return self

    def verde_leve(self):
        self.cor += '\033[92m'
        return self

    def Verde_leve(self):
        self.cor += '\033[102m'
        return self

    def amarelo(self):
        self.cor += '\033[33m'
        return self

    def Amarelo(self):
        self.cor += '\033[43m'
        return self

    def amarelo_leve(self):
        self.cor += '\033[93m'
        return self

    def Amarelo_leve(self):
        self.cor += '\033[103m'
        return self

    def ciano(self):
        self.cor += '\033[36m'
        return self

    def Ciano(self):
        self.cor += '\033[46m'
        return self

    def print(self, texto):
        print(self.cor + '--------' + texto + '--------' + '\033[0m')

    def printar(self, texto):
        print(texto)

    @staticmethod
    def cls():
        os.system('cls')

    @staticmethod
    def janela(metodo):
        loop = True
        while loop:
            loop = metodo()

    @staticmethod
    def transitar_janela(opcoes, escolha):
        TelaBase.janela(opcoes.get(escolha))

    @staticmethod
    def confirmar(texto):
        confirmar = input(texto)
        if confirmar.lower() != 'y':
            return False
        return True

    @staticmethod
    def input(txt):
        import msvcrt
        texto = ''

        print(txt)
        while True:
            if msvcrt.kbhit():
                key_stroke = msvcrt.getche()
                if key_stroke == chr(27).encode():
                    return None
                elif key_stroke == b'\r':
                    TelaBase.cls()
                    print('saindo...')
                    return texto
                elif key_stroke == b'\x08':
                    texto = texto[:-1]
                else:
                    texto += str(key_stroke).split("'")[1]

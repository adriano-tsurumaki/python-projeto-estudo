import pandas as pd

from Telas.Listar import Listar
from Telas.Criar import Criar
from Telas.TelaBase import TelaBase
from Utils.ValidarInput import ValidarInput


class Service:
    @staticmethod
    def retornar_df(path):
        try:
            return pd.read_csv(path)
        except (ValueError, Exception):
            df = pd.DataFrame({'Nome': '', 'Assuntos': []})
            df.to_csv(path, index=False)
            return df

    @staticmethod
    def reescrever_arquivo(path, df):
        try:
            df.to_csv(path, index=False)
            print('Arquivo salvo com sucesso')
        except (ValueError, Exception):
            print('Ocorreu um erro ao salvar o arquivo')


class Principal(TelaBase):
    pathDisciplina = r'D:\Banco do Brasil\Python\Controle\Disciplinas.csv'
    manter_na_tela = True

    def mostrar_menu(self):
        self.cls()
        self.bold().print('Menu')
        print('[0] - Sair')
        print('[1] - Criar')
        print('[2] - Listar')

        escolha = input('Digite aqui: ')

        if escolha == '0':
            confirmar = input('Deseja sair? [Y/N]')

            if confirmar.lower() != 'y':
                return self.manter_na_tela
            return not self.manter_na_tela

        [mensagem, validado] = ValidarInput.validar_input_numerico(escolha, 0, 2)
        if not validado:
            input(mensagem)
            return self.manter_na_tela

        escolha = int(escolha)

        if escolha == 0:
            return not self.manter_na_tela

        opcoes = {
            1: lambda: Criar().menu(),
            2: lambda: Listar().menu()
        }
        self.transitar_janela(opcoes, escolha)
        return self.manter_na_tela


def start_program():
    principal = Principal()
    principal.janela(principal.mostrar_menu)


if __name__ == '__main__':
    start_program()

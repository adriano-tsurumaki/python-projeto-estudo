from .ListarDisciplina import ListarDisciplina
from .ListarAssunto import ListarAssunto
from ..TelaBase import TelaBase
from Utils.ValidarInput import ValidarInput


class Listar(TelaBase):
    def menu(self):
        self.cls()
        self.bold().print('Menu de listagem')
        print('[0] - Voltar')
        print('[1] - Listar disciplina')
        print('[2] - Listar assunto')

        escolha = input('Digite aqui: ')

        [mensagem, validado] = ValidarInput.validar_input_numerico(escolha, 0, 2)
        if not validado:
            input(mensagem)
            return self.manter_na_tela

        escolha = int(escolha)

        if escolha == 0:
            return not self.manter_na_tela

        opcoes = {
            1: lambda: ListarDisciplina().mostrar(),
            2: lambda: ListarAssunto().mostrar()
        }
        self.transitar_janela(opcoes, escolha)
        return self.manter_na_tela

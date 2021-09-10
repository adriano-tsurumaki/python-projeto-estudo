from ..TelaBase import TelaBase
from Utils.ValidarInput import ValidarInput


class Criar(TelaBase):
    def menu(self):
        self.cls()
        self.bold().print('Menu de criação')
        print('[0] - Voltar')
        print('[1] - Criar disciplina')
        print('[2] - Criar assunto')
        print('[3] - Criar questões')

        escolha = input('Digite aqui: ')

        [mensagem, validado] = ValidarInput.validar_input_numerico(escolha, 0, 3)
        if not validado:
            input(mensagem)
            return self.manter_na_tela

        escolha = int(escolha)

        if escolha == 0:
            return not self.manter_na_tela

        from .CriarDisciplina import CriarDisciplina
        from .CriarAssunto import CriarAssunto
        from .CriarQuestao import CriarQuestao

        criar_questao = CriarQuestao()

        opcoes = {
            1: lambda: CriarDisciplina().mostrar(),
            2: lambda: CriarAssunto().mostrar(),
            3: lambda: criar_questao.mostrar()
        }
        self.transitar_janela(opcoes, escolha)
        return self.manter_na_tela

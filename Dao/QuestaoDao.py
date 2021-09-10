class QuestaoDao:
    @staticmethod
    def inserir(quantidade, id_assunto):
        from BancoDeDados.config_database import Questao, DATABASE
        with DATABASE.atomic() as transaction:
            try:
                for i in range(quantidade):
                    Questao.create(id_assunto=id_assunto, numero_questao=i+1)

                texto = str(quantidade) + ' questões' if quantidade > 1 else str(quantidade) + ' questão'
                input(texto + ' cadastrado com sucesso')
                transaction.commit()
            except (ValueError, Exception):
                input('Ocorreu um erro ao cadastrar as questões')
                transaction.rollback()

    @staticmethod
    def retornar_quantidade(id_assunto):
        from BancoDeDados.config_database import Questao
        return len(Questao.select().where(Questao.id_assunto == id_assunto))

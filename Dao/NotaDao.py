from BancoDeDados.config_database import Nota, Questao


class NotaDao:
    @staticmethod
    def inserir_um(id_assunto, numero_questao, acerto):
        try:
            id_questao = Questao.select()\
                .where(Questao.id_assunto == id_assunto,
                       Questao.numero_questao == numero_questao)\
                .get().id
            Nota.create(id_questao=id_questao, acerto=acerto)
            input('Nota registrado com sucesso.')
            return True
        except (ValueError, Exception):
            input('Ocorreu um erro ao inserir a nota.')
            return False

    @staticmethod
    def inserir_range(id_assunto, acertou_param, acertos, inicio, fim):
        from BancoDeDados.config_database import DATABASE

        with DATABASE.atomic() as transaction:
            try:
                for i in range(inicio, fim+1):
                    acertou = acertou_param
                    id_questao = Questao.select()\
                        .where(Questao.id_assunto == id_assunto,
                               Questao.numero_questao == i)\
                        .get().id
                    if i not in acertos:
                        acertou = not acertou_param
                    Nota.create(id_questao=id_questao, acerto=acertou)
                input('Notas registrados com sucesso.')
                transaction.commit()
                return True
            except (ValueError, Exception):
                input('Ocorreu um erro ao inserir a nota.')
                transaction.rollback()
                return False

    @staticmethod
    def retornar_notas_por_questao(id_questao):
        return Nota.select().where(Nota.id_questao == id_questao)

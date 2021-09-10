class ValidarInput:
    @staticmethod
    def validar_input_numerico(escolha, numero_inicio, numero_final):
        if not escolha.isnumeric():
            return ['Deve ser um número', False]

        escolha = int(escolha)

        if escolha not in range(numero_inicio, numero_final + 1):
            return ['Opção não listada', False]

        return ['', True]

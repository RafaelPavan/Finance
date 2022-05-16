from filtra_dados.scraper import valor_dolar, valor_euro, valor_libra, valor_iene
from interfaces import interface
from querys.user_query import QueryCustomer

if __name__ == '__main__':
    # print(valor_dolar.text)
    # print(valor_euro.text)
    pass


class Cots:
    @staticmethod
    def show_quotations():
        interface.cotacoes.show()
        interface.login.close()

    @staticmethod
    def dolar_cot():
        interface.dolar.show()
        interface.cotacoes.close()
        interface.dolar.label_3.setText(f'R$ {valor_dolar.text}')

    @staticmethod
    def euro_cot():
        interface.euro.show()
        interface.cotacoes.close()
        interface.euro.label_3.setText(f'R$ {valor_euro.text}')

    @staticmethod
    def libra_cot():
        interface.libra.show()
        interface.cotacoes.close()
        interface.libra.label_3.setText(f'R$ {valor_libra.text}')

    @staticmethod
    def iene_cot():
        interface.iene.show()
        interface.cotacoes.close()
        interface.iene.label_3.setText(f'R$ {valor_iene.text}')

    @staticmethod
    def back_dolar():
        interface.dolar.close()
        interface.cotacoes.show()

    @staticmethod
    def back_euro():
        interface.euro.close()
        interface.cotacoes.show()

    @staticmethod
    def back_libra():
        interface.libra.close()
        interface.cotacoes.show()

    @staticmethod
    def back_iene():
        interface.iene.close()
        interface.cotacoes.show()


class Register(object):

    @staticmethod
    def aparece_usuario():
        interface.register.show()
        interface.login.close()

    @staticmethod
    def register_user():
        name = interface.register.lineEdit.text()
        surname = interface.register.lineEdit_2.text()
        cpf = interface.register.lineEdit_3.text()
        user_login = interface.register.lineEdit_4.text()
        password = interface.register.lineEdit_5.text()

        try:
            QueryCustomer().insert_user(name, surname, cpf, user_login, password)
            interface.register.label_2.setText("Cliente cadastrado com sucesso!")
        except Exception as erro:
            print(erro)

    @staticmethod
    def back_login():
        interface.login.show()
        interface.register.close()

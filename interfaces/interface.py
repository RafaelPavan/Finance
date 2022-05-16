from PyQt5 import uic, QtWidgets
import main


app = QtWidgets.QApplication([])
cotacoes = uic.loadUi('interfaces/cotacoes.ui')
dolar = uic.loadUi('interfaces/dolar.ui')
euro = uic.loadUi('interfaces/euro.ui')
libra = uic.loadUi('interfaces/libra.ui')
iene = uic.loadUi('interfaces/iene.ui')

cotacoes.pushButton.clicked.connect(main.Cots.dolar_cot)
cotacoes.pushButton_2.clicked.connect(main.Cots.euro_cot)
cotacoes.pushButton_3.clicked.connect(main.Cots.libra_cot)
cotacoes.pushButton_4.clicked.connect(main.Cots.iene_cot)

dolar.pushButton.clicked.connect(main.Cots.back_dolar)
euro.pushButton.clicked.connect(main.Cots.back_euro)
libra.pushButton.clicked.connect(main.Cots.back_libra)
iene.pushButton.clicked.connect(main.Cots.back_iene)

cotacoes.show()
app.exec()

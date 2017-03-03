import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QAction,QFileDialog
from PyQt5.QtWidgets import QLabel, QCheckBox, QPushButton, QGridLayout, qApp

class MyWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		
		exitAction = QAction("&Выход", self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip("Выход")
		exitAction.triggered.connect(qApp.quit)

		openAction = QAction("&Открыть тест", self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip("Открытие теста")
		openAction.triggered.connect(qApp.quit)
		self.statusBar()

		menu = self.menuBar()
		fileMenu = menu.addMenu("&Файл")
		fileMenu.addAction(exitAction)
		fileMenu.addAction(openAction)

		grid = QGridLayout()
		grid.setSpacing(10)




		self.setGeometry(150,150,450,250)
		self.setWindowTitle("Тест ыыыы")
		self.show()




if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyWindow()
	sys.exit(app.exec_())




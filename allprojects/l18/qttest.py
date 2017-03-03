import sys
from PyQt5.QtWidgets import QApplication, QWidget

class FirstWindow(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		self.setGeometry(300,300, 200, 300)
		self.show()

if __name__ == "__main__":

	app = QApplication(sys.argv)
	window = FirstWindow()
	sys.exit(app.exec_())




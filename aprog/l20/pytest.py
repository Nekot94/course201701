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
		openAction.triggered.connect(self.openTest)
		self.statusBar()

		menu = self.menuBar()
		fileMenu = menu.addMenu("&Файл")
		fileMenu.addAction(exitAction)
		fileMenu.addAction(openAction)

		grid = QGridLayout()
		grid.setSpacing(10)

		self.question = QLabel()
		grid.addWidget(self.question,0,0)

		self.answers = []
		n, k = 1, 0
		for i in range(4):
			self.answers.append(QCheckBox()) 
			grid.addWidget(self.answers[i],n,k)
			if k < 1:
				k += 1
			else:
				k = 0
				n += 1

		self.nextButton = QPushButton()
		self.nextButton.clicked.connect(self.goNext)
		grid.addWidget(self.nextButton,n,1)

		self.myWidg = QWidget()
		self.myWidg.setLayout(grid)
		self.myWidg.hide()
		self.setCentralWidget(self.myWidg)

		self.endWidg = QLabel()



		self.setGeometry(150,150,450,250)
		self.setWindowTitle("Тест ыыыы")
		self.show()

	def openTest(self):
		fName = QFileDialog.getOpenFileName(self,'Открыть файл', '.')
		self.test = []
		with open(fName[0],'r',encoding='utf-8') as f:
			for line in f:
				self.test.append(line)

		print(self.test)

		self.counts = len(self.test) // 3
		self.currentQuestion = 1
		self.line = 0
		self.rightCounts = 0

		self.goNext()
		self.myWidg.show()

	def goNext(self):
		if self.currentQuestion > 1:
			right = 0
			for cAnswer in self.answers:
				if cAnswer.isChecked():
					if cAnswer.text() in self.rightAnswers:
						right += 1
					else:
						right = 0
						break
			if right == len(self.rightAnswers):
				self.rightCounts += 1

		if self.currentQuestion > self.counts:
			self.endWidg.setText('Твой результат: {0.rightCounts}/{0.counts}'.format(self))
			self.setCentralWidget(self.endWidg)
			return


		l = self.line
		self.question.setText(self.test[l])
		answers = self.test[l+1][:-1].split(', ')
		for cAnswer, answer in zip(self.answers,answers):
			cAnswer.setText(answer)
		self.rightAnswers = self.test[l+2][:-1].split(', ')

		self.line += 3
		self.currentQuestion += 1













if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyWindow()
	sys.exit(app.exec_())




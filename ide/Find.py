from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QCheckBox, QDialogButtonBox, QPushButton, QRadioButton, QGroupBox
class findDialog(QDialog):
	def __init__(self,mainWindow,editor):
		super().__init__(mainWindow)
		self.setWindowTitle("Find")
		self.resize(402,300)
		self.editor=editor
		self.RE=None
		self.CS=None
		self.Word=None
		self.Wrap=None
		self.Forward=None
		self.queryWord=None
		self.initUI()
		self.show()
	def initUI(self):
		lblFind=QLabel(self)
		lblFind.setGeometry(QRect(10, 20, 51, 21))
		defaultFont=QFont()
		defaultFont.setPointSize(10)
		lblFind.setFont(defaultFont)
		lblFind.setText("Find:")
		
		self.txtFind=QLineEdit(self)
		self.txtFind.setGeometry(QRect(70, 20, 321, 20))
		self.txtFind.setFont(defaultFont)
		
		self.chkRE=QCheckBox(self)
		self.chkRE.setGeometry(QRect(10, 60, 281, 17))
		self.chkRE.setFont(defaultFont)
		self.chkRE.setText("Regular Expression")
		
		self.chkCS=QCheckBox(self)
		self.chkCS.setGeometry(QRect(10, 90, 281, 17))
		self.chkCS.setFont(defaultFont)
		self.chkCS.setText("Case sensitive")
		
		self.chkWord=QCheckBox(self)
		self.chkWord.setGeometry(QRect(10, 120, 281, 17))
		self.chkWord.setFont(defaultFont)
		self.chkWord.setText("Whole word")
		
		self.chkWrap=QCheckBox(self)
		self.chkWrap.setGeometry(QRect(10, 150, 281, 17))
		self.chkWrap.setFont(defaultFont)
		self.chkWrap.setText("Wrap around")
		
		defaultDialogButtons=QDialogButtonBox(self)
		defaultDialogButtons.setGeometry(QRect(240, 270, 156, 23))
		defaultDialogButtons.setFont(defaultFont)
		defaultDialogButtons.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
		
		btnFind=QPushButton(self)
		btnFind.setGeometry(QRect(160, 270, 75, 23))
		btnFind.setFont(defaultFont)
		btnFind.setText("Find...")

		
		
		directionBox=QGroupBox(self)
		directionBox.setGeometry(QRect(10, 180, 341, 51))
		directionBox.setFont(defaultFont)
		directionBox.setTitle("Direction")
		
		self.rbFwd=QRadioButton(directionBox)
		self.rbFwd.setGeometry(QRect(0, 20, 82, 17))
		self.rbFwd.setFont(defaultFont)
		self.rbFwd.setText("Forward")
		self.rbFwd.setChecked(True)
		
		self.rbBwd=QRadioButton(directionBox)
		self.rbBwd.setGeometry(QRect(260, 20, 82, 17))
		self.rbBwd.setFont(defaultFont)
		self.rbBwd.setText("Backward")
		
		btnFind.clicked.connect(self.FindText)
	def FindText(self):
		RE=self.chkRE.isChecked()
		CS=self.chkCS.isChecked()
		Word=self.chkWord.isChecked()
		Wrap=self.chkWrap.isChecked()
		Forward=True
		if self.rbBwd.isChecked():
			Forward=False
		queryWord=self.txtFind.text()
		if ((self.RE==RE) and (self.CS==CS) and (self.Word==Word) and (self.Wrap==Wrap) and (self.Forward==Forward) and (self.queryWord==queryWord)):
			output=self.editor.findNext()
		else:
			output=self.editor.findFirst(queryWord,RE,CS,Word,Wrap,Forward,0,0)
			self.RE=RE
			self.CS=CS
			self.Word=Word
			self.Wrap=Wrap
			self.Forward=Forward
			self.queryWord=queryWord
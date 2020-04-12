from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QCheckBox, QDialogButtonBox, QPushButton, QRadioButton, QGroupBox
class replaceDialog(QDialog):
	def __init__(self,mainWindow,editor):
		super().__init__(mainWindow)
		self.resize(409, 367)
		self.editor=editor
		self.initUI()
		self.show()
	def initUI(self):
		lblFind=QLabel(self)
		lblFind.setGeometry(QRect(10, 10, 47, 21))
		defaultFont=QFont()
		defaultFont.setPointSize(10)
		lblFind.setFont(defaultFont)
		lblFind.setText("Find")
		
		lblReplace=QLabel(self)
		lblReplace.setGeometry(QRect(10, 53, 61, 20))
		lblReplace.setFont(defaultFont)
		lblReplace.setText("Replace")
		
		self.txtFind=QLineEdit(self)
		self.txtFind.setGeometry(QRect(80, 10, 261, 20))
		self.txtFind.setFont(defaultFont)
		
		self.txtReplace=QLineEdit(self)
		self.txtReplace.setGeometry(QRect(80, 50, 261, 21))
		self.txtReplace.setFont(defaultFont)
		
		self.chkRE=QCheckBox(self)
		self.chkRE.setGeometry(QRect(10, 110, 261, 17))
		self.chkRE.setFont(defaultFont)
		self.chkRE.setText("Regular Expression")
		
		self.chkCS=QCheckBox(self)
		self.chkCS.setGeometry(QRect(10, 140, 261, 17))
		self.chkCS.setFont(defaultFont)
		self.chkCS.setText("Case sensitive")
		
		self.chkWord=QCheckBox(self)
		self.chkWord.setGeometry(QRect(10, 170, 261, 17))
		self.chkWord.setFont(defaultFont)
		self.chkWord.setText("Whole word")
		
		self.chkWrap=QCheckBox(self)
		self.chkWrap.setGeometry(QRect(10, 200, 261, 17))
		self.chkWrap.setFont(defaultFont)
		self.chkWrap.setText("Wrap around")
		
		defaultDialogButtons=QDialogButtonBox(self)
		defaultDialogButtons.setGeometry(QRect(250, 340, 156, 23))
		defaultDialogButtons.setFont(defaultFont)
		defaultDialogButtons.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
		
		btnReplace=QPushButton(self)
		btnReplace.setGeometry(QRect(150, 340, 91, 23))
		btnReplace.setFont(defaultFont)
		btnReplace.setText("Replace...")
		
		directionBox=QGroupBox(self)
		directionBox.setGeometry(QRect(20, 240, 120, 80))
		directionBox.setFont(defaultFont)
		directionBox.setTitle("Direction")
		
		self.rbFwd=QRadioButton(directionBox)
		self.rbFwd.setGeometry(QRect(10, 20, 82, 17))
		self.rbFwd.setFont(defaultFont)
		self.rbFwd.setText("Forward")
		self.rbFwd.setChecked(True)
		
		self.rbBwd=QRadioButton(directionBox)
		self.rbBwd.setGeometry(QRect(10, 50, 82, 17))
		self.rbBwd.setFont(defaultFont)
		self.rbBwd.setText("Backward")
		
		btnReplace.clicked.connect(self.ReplaceText)
	def ReplaceText(self):
		if self.rbFwd.isChecked():
			forward=True
		if self.rbBwd.isChecked():
			forward=False
		if self.txtFind.text()=="":
			self.txtFind.setFocus()
		elif self.txtReplace.text()=="":
			self.txtFind.setFocus()
		else:
			returnVal=self.editor.findFirst(self.txtFind.text(),self.chkRE.isChecked(),self.chkCS.isChecked(),self.chkWord.isChecked(),self.chkWrap.isChecked(),0,0)
			self.editor.replace(self.txtReplace.text())
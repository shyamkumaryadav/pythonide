from PyQt5.QtWidgets import QMessageBox,QApplication,QStyleFactory
class Dialogs(QMessageBox):
    def __init__(self,mainwindow):
        super().__init__(mainwindow)
        self.button_status=None
    def Error(self,message,title="Alert"):
        self.setIcon(QMessageBox.Critical)
        self.setText(message)
        self.setWindowTitle(title)
        self.setStandardButtons(QMessageBox.Ok)
        self.buttonClicked.connect(self.msgreturn)
        self.exec_()
    def Message(self,message,title="Message"):
        self.setIcon(QMessageBox.Information)
        self.setText(message)
        self.setWindowTitle(title)
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.buttonClicked.connect(self.msgreturn)
        self.exec_()
    def MsgQuestion(self,message,title="Question"):
        self.setIcon(QMessageBox.Information)
        self.setText(message)
        self.setWindowTitle(title)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        self.buttonClicked.connect(self.msgreturn)
        self.exec_()
    def msgreturn(self,i):
        if(i.text()=="Ok"):
            self.button_status="Ok"
        elif(i.text()=="Yes"):
            self.button_status="accept"
        elif(i.text()=="No"):
            self.butoon_status="reject"
        else:
            self.button_status="Cancel"
    def getclickstatus(self):
        return self.button_status 
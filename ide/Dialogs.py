from PyQt5.QtWidgets import QMessageBox
class Dialogs():
	def Message(self,parent,message,title="Python IDE"):
		retval=QMessageBox.information(parent,title,message)
		if retval==QMessageBox.Ok:
			pass
	def Question(self,parent,message,title="Python IDE"):
		retval=QMessageBox.question(parent,title,message,defaultButton=QMessageBox.Yes)
		if retval==QMessageBox.Yes:
			return "accept"
		else:
			return "reject"
	def Error(self,parent,message,title="Python IDE"):
		retval=QMessagebox.critical(parent,title,message)
		if retval==QMessageBox.Ok:
			pass

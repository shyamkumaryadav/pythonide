from PyQt5.QtWidgets import QFileDialog
class SaveLoad():
    def SaveDialog(self):
        return QFileDialog().getSaveFileName()[0]
    def OpenDialog(self):
        return QFileDialog().getOpenFileName()[0]

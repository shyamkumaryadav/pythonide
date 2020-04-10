from PyQt5.QtWidgets import QSizePolicy, QWidget, QMenuBar, QMenu, QAction, QApplication, QMainWindow, QMessageBox, QStyleFactory, QDesktopWidget,QInputDialog,QLineEdit,QFontDialog
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QColor,QFont
from PyQt5.Qsci import *
import platform
import sys
from Settings import style_settings
from Dialogs import Dialogs
from SaveLoad import SaveLoad
from Operations import Save,Open
from Runfile import Runfile, Shell
s=SaveLoad()
class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.filename=None
        self.setFixedSize(900,QDesktopWidget().screenGeometry(-1).height())
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.initUI()
        self.d=Dialogs(self)
    def initUI(self):
        self.centralWidget=QWidget(self)
        sizePolicy=QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalPolicy(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralwidget")
        self.editor=QsciScintilla(self.centralWidget)
        try:
            file_handle=open("config.txt","r")
            font_name,size,bold,italic=file_handle.read().split("/")
            if bold and italic:
                font=QFont(font_name,float(size),QFont.Bold,True)
            elif bold:
                font=QFont(font_name,float(size),QFont.Bold)
            else:
                font=QFont(font_name,float(size))
                if italic:
                    font.setItalic(True)
        except:
            font=QFont("Times New Roman",12)
        self.editor.setFont(font)
        self.editor.setMargins(2)
        self.editor.setMarginType(0,QsciScintilla.NumberMargin)
        self.editor.setMarginType(1,QsciScintilla.SymbolMargin)
        self.editor.setMarginWidth(0,"00")
        self.editor.setMarginWidth(1,"00")
        self.editor.markerDefine(QsciScintilla.RightTriangle,1)
        if(platform.system()=="Windows"):
            self.editor.setEolMode(QsciScintilla.EolWindows)
        elif(platform.system()=="Linux"):
            self.editor.setEolMode(QsciScintilla.EolUnix)
        elif(platform.system()=="Mac"):
            self.editor.setEolMode(QsciScintilla.EolMac)
        else:
            print("Using default(i.e. Windows bindings)")
            self.editor.setEolMode(QsciScintilla.EolWindows)
        self.editor.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.editor.setIndentationsUseTabs(True)
        self.editor.setTabWidth(4)
        self.editor.setIndentationGuides(True)
        self.editor.setTabIndents(True)
        self.editor.setAutoIndent(True)
        self.editor.setCaretForegroundColor(QColor("#ff11214b"))
        self.editor.setCaretLineVisible(True)
        self.editor.setCaretLineBackgroundColor(QColor("#1f0000ff"))
        self.editor.setUtf8(True)
        self.editor.setMarginSensitivity(1,True)
        self.editor.marginClicked.connect(self.margin_clicked)
        self.editor.marginRightClicked.connect(self.margin_right_clicked)
        self.lexer=QsciLexerPython()
        self.lexer.setFont(font)
        self.editor.setLexer(self.lexer)
        self.editor.setGeometry(QRect(0, 0, 900,680))
        self.setCentralWidget(self.centralWidget)
        self.menubar=QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 833, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.setMenuBar(self.menubar)
        self.actionFont = QAction(self)
        self.actionFont.setObjectName("actionFont")
        self.actionEncoding = QAction(self)
        self.actionEncoding.setObjectName("actionEncoding")
        self.actionNew = QAction(self)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QAction(self)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QAction(self)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QAction(self)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QAction(self)
        self.actionRedo.setObjectName("actionRedo")
        self.actionSelect_All = QAction(self)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionCut = QAction(self)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QAction(self)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QAction(self)
        self.actionPaste.setObjectName("actionPaste")
        self.actionFind = QAction(self)
        self.actionFind.setObjectName("actionFind")
        self.actionReplace = QAction(self)
        self.actionReplace.setObjectName("actionReplace")
        self.actionRun = QAction(self)
        self.actionRun.setObjectName("actionRun")
        self.actionRunCustomized = QAction(self)
        self.actionRunCustomized.setObjectName("actionRunCustomized")
        self.actionShell = QAction(self)
        self.actionShell.setObjectName("actionShell")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuView.addAction(self.actionFind)
        self.menuView.addAction(self.actionReplace)
        self.menuRun.addAction(self.actionRun)
        self.menuRun.addAction(self.actionRunCustomized)
        self.menuRun.addAction(self.actionShell)
        self.menuSettings.addAction(self.actionFont)
        self.menuSettings.addAction(self.actionEncoding)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.retranslateUI()
        self.actionNew.triggered.connect(self.new)
        self.actionOpen.triggered.connect(self.open)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_As.triggered.connect(self.saveAs)
        self.actionExit.triggered.connect(self.close)
        self.actionUndo.triggered.connect(self.editor.undo)
        self.actionRedo.triggered.connect(self.editor.redo)
        self.actionSelect_All.triggered.connect(lambda:self.editor.selectAll(True))
        self.actionCut.triggered.connect(self.editor.cut)
        self.actionCopy.triggered.connect(self.editor.copy)
        self.actionPaste.triggered.connect(self.editor.paste)
        self.actionRun.triggered.connect(self.run)
        self.actionRunCustomized.triggered.connect(self.runCustom)
        self.actionShell.triggered.connect(self.shell)
        self.actionFont.triggered.connect(self.Font)
        QMetaObject.connectSlotsByName(self)
    def retranslateUI(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Untitled"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuRun.setTitle(_translate("MainWindow","Run"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionFont.setText(_translate("MainWindow", "Font..."))
        self.actionEncoding.setText(_translate("MainWindow", "Encoding..."))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Alt+X"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionSelect_All.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionFind.setText(_translate("MainWindow", "Find..."))
        self.actionReplace.setText(_translate("MainWindow", "Replace..."))
        self.actionRun.setText(_translate("MainWindow","Run..."))
        self.actionRunCustomized.setText(_translate("MainWindow","Run customized"))
        self.actionShell.setText(_translate("MainWindow","Shell"))
    def margin_clicked(self,margin_nr,line_nr,state):
        self.editor.markerAdd(line_nr,margin_nr)
    def margin_right_clicked(self,margin_nr,line_nr,state):
        self.editor.markerDelete(line_nr,margin_nr)
    def new(self):
        if self.editor.text()!= None:
            self.d.MsgQuestion("Do you want to save your file?")
            if(self.d.getclickstatus()=="accept"):
                filepath=s.SaveDialog()
                returnval=Save(self.editor.text(),filepath)
                if(returnval):
                    self.d.Message("File Saved successfully")
                else:
                    self.d.Error("File could not be saved")
        self.editor.setText("")
    def open(self):
        if self.editor.text()!= None:
            self.d.MsgQuestion("Do you want to save your file?")
            if(self.d.getclickstatus()=="accept"):
                filepath=s.SaveDialog()
                returnval=Save(filepath)
                if(returnval):
                    d.Message("File Saved successfully")
                else:
                    d.Error("File could not be saved")
        filename=s.OpenDialog()
        data=Open(filename)
        if data is not None:
            self.editor.setText(data)
            self.setWindowTitle(filename)
            self.filename=filename
    def save(self):
        if self.filename is None:
            self.saveAs()
        else:
            returnval=Save(self.editor.text(),self.filename)
            if(returnval):
                self.d.Message("File Saved successfully")
                self.setWindowTitle(self.filename)
            else:
                self.d.Error("File could not be saved")
    def saveAs(self):
        self.filename=s.SaveDialog()
        returnval=Save(self.editor.text(),self.filename)
        if(returnval):
            self.d.Message("File Saved successfully")
            self.setWindowTitle(self.filename)
        else:
            self.d.Error("File could not be saved")
    def run(self):
        if self.filename is None:
            self.saveAs()
        Runfile(self.filename)
    def runCustom(self):
        if self.filename is None:
            self.saveAs()
        if self.filename != "":
            print(len(self.filename))
            option,ok=QInputDialog().getText(self,"Customized run","Enter parameters for sys.argv",QLineEdit.Normal," ")
            if ok:
                Runfile(self.filename,option)
            else:
                Runfile(self.filename)
    def shell(self):
        Shell()
    def Font(self):
        font, ok=QFontDialog.getFont()
        if ok:
            self.editor.setFont(font)
            self.lexer.setFont(font)
            self.editor.setLexer(self.lexer)
if __name__=="__main__":
    style=style_settings(QStyleFactory.keys())
    app=QApplication([])
    app.setStyle(QStyleFactory.create(style))
    g=TextEditor()
    g.show()
    sys.exit(app.exec_())
    

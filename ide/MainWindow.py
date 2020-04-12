from PyQt5.QtWidgets import QAction, QApplication, QFileSystemModel, QFontDialog, QHBoxLayout, QInputDialog, QLineEdit, QMainWindow, QMenu, QMenuBar, QMessageBox, QStyleFactory, QTreeView, QWidget
from PyQt5.QtGui import QColor, QFont
from PyQt5.Qsci import QsciLexerPython, QsciScintilla
from platform import system
from sys import exit
from Settings import style_settings
from Dialogs import Dialogs
from SaveLoad import SaveLoad
from Operations import Save,Open
from Runfile import Runfile, Shell
from Replace import replaceDialog
from Find import findDialog
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Untitled")
		self.saveLoad=SaveLoad()
		self.fileName=None
		self.dialogs=Dialogs(self)
		self.setupUI()
	def setupUI(self):
		centralWidget=QWidget(self)
		layout=QHBoxLayout(centralWidget)
		self.fileSysView=QTreeView(centralWidget)
		self.setupFileSystemViewer()
		self.editor=QsciScintilla(centralWidget)
		self.setupEditor()
		layout.addWidget(self.fileSysView,1)
		layout.addWidget(self.editor,3)
		self.setCentralWidget(centralWidget)
		self.setMinimumSize(700,500)
		self.defaultMenuBar=QMenuBar(self)
		self.setupMenus()
		self.setMenuBar(self.defaultMenuBar)
		self.show()
	def setupEditor(self):
		self.editor.setFont(QFont("Times New Roman",12))
		self.editor.setMargins(2)
		self.editor.setMarginType(0,QsciScintilla.NumberMargin)
		self.editor.setMarginType(1,QsciScintilla.SymbolMargin)
		self.editor.setMarginWidth(0,"000")
		self.editor.setMarginWidth(1,"00")
		self.editor.markerDefine(QsciScintilla.RightTriangle,1)
		if system()=="Windows":
			self.editor.setEolMode(QsciScintilla.EolWindows)
		elif system()=="Linux":
			self.editor.setEolMode(QsciScintilla.EolUnix)
		elif system()=="Mac":
			self.editor.setEolMode(QsciScintilla.EolMac)
		else:
			print("Using Windows EOL")
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
		self.lexer.setFont(QFont("Times New Roman",12))
		self.editor.setLexer(self.lexer)
		self.editor.textChanged.connect(self.fileChanged)
	def setupFileSystemViewer(self):
		model=QFileSystemModel()
		model.setRootPath("/")
		self.fileSysView.setModel(model)
		self.fileSysView.hideColumn(1)
		self.fileSysView.hideColumn(2)
		self.fileSysView.hideColumn(3)
		self.fileSysView.doubleClicked.connect(self.openFile)
	def setupMenus(self):
		fileMenu=QMenu(self.defaultMenuBar)
		fileMenu.setTitle("File")
		editMenu=QMenu(self.defaultMenuBar)
		editMenu.setTitle("Edit")
		viewMenu=QMenu(self.defaultMenuBar)
		viewMenu.setTitle("View")
		runMenu=QMenu(self.defaultMenuBar)
		runMenu.setTitle("Run")
		settingsMenu=QMenu(self.defaultMenuBar)
		settingsMenu.setTitle("Settings")
		self.actionNew=QAction(self)
		self.actionNew.setText("New")
		self.actionNew.setShortcut("Ctrl+N")
		self.actionOpen=QAction(self)
		self.actionOpen.setText("Open")
		self.actionOpen.setShortcut("Ctrl+O")
		self.actionSave=QAction(self)
		self.actionSave.setText("Save")
		self.actionSave.setShortcut("Ctrl+S")
		self.actionSaveAs=QAction(self)
		self.actionSaveAs.setText("Save As")
		self.actionSaveAs.setShortcut("Ctrl+Shift+S")
		self.actionExit=QAction(self)
		self.actionExit.setText("Exit")
		self.actionExit.setShortcut("Alt+X")
		self.actionUndo=QAction(self)
		self.actionUndo.setText("Undo")
		self.actionUndo.setShortcut("Ctrl+Z")
		self.actionRedo=QAction(self)
		self.actionRedo.setText("Redo")
		self.actionRedo.setShortcut("Ctrl+Shift+Z")
		self.actionSelectAll=QAction(self)
		self.actionSelectAll.setText("Select all")
		self.actionSelectAll.setShortcut("Ctrl+A")
		self.actionCut=QAction(self)
		self.actionCut.setText("Cut")
		self.actionCut.setShortcut("Ctrl+X")
		self.actionCopy=QAction(self)
		self.actionCopy.setText("Copy")
		self.actionCopy.setShortcut("Ctrl+C")
		self.actionPaste=QAction(self)
		self.actionPaste.setText("Paste")
		self.actionPaste.setShortcut("Ctrl+V")
		self.actionFind=QAction(self)
		self.actionFind.setText("Find")
		self.actionFind.setShortcut("Ctrl+F")
		self.actionReplace=QAction(self)
		self.actionReplace.setText("Replace")
		self.actionReplace.setShortcut("Ctrl+H")
		self.actionRun=QAction(self)
		self.actionRun.setText("Run")
		self.actionRun.setShortcut("F5")
		self.actionRunCustom=QAction(self)
		self.actionRunCustom.setText("Run Customized")
		self.actionRunCustom.setShortcut("Shift+F5")
		self.actionShell=QAction(self)
		self.actionShell.setText("Python shell")
		self.actionShell.setShortcut("Alt+S")
		self.actionFont=QAction(self)
		self.actionFont.setText("Font")
		self.actionEncoding=QAction(self)
		self.actionEncoding.setText("Encoding")
		fileMenu.addAction(self.actionNew)
		fileMenu.addAction(self.actionOpen)
		fileMenu.addAction(self.actionSave)
		fileMenu.addAction(self.actionSaveAs)
		fileMenu.addSeparator()
		fileMenu.addAction(self.actionExit)
		editMenu.addAction(self.actionUndo)
		editMenu.addAction(self.actionRedo)
		editMenu.addSeparator()
		editMenu.addAction(self.actionSelectAll)
		editMenu.addSeparator()
		editMenu.addAction(self.actionCut)
		editMenu.addAction(self.actionCopy)
		editMenu.addAction(self.actionPaste)
		viewMenu.addAction(self.actionFind)
		viewMenu.addAction(self.actionReplace)
		runMenu.addAction(self.actionRun)
		runMenu.addAction(self.actionRunCustom)
		runMenu.addAction(self.actionShell)
		settingsMenu.addAction(self.actionFont)
		settingsMenu.addAction(self.actionEncoding)
		self.defaultMenuBar.addAction(fileMenu.menuAction())
		self.defaultMenuBar.addAction(editMenu.menuAction())
		self.defaultMenuBar.addAction(viewMenu.menuAction())
		self.defaultMenuBar.addAction(runMenu.menuAction())
		self.defaultMenuBar.addAction(settingsMenu.menuAction())
		self.actionNew.triggered.connect(self.new)
		self.actionOpen.triggered.connect(self.open)
		self.actionSave.triggered.connect(self.save)
		self.actionSaveAs.triggered.connect(self.saveAs)
		self.actionExit.triggered.connect(self.close)
		self.actionUndo.triggered.connect(self.editor.undo)
		self.actionRedo.triggered.connect(self.editor.redo)
		self.actionSelectAll.triggered.connect(lambda:self.editor.selectAll(True))
		self.actionCut.triggered.connect(self.editor.cut)
		self.actionCopy.triggered.connect(self.editor.copy)
		self.actionPaste.triggered.connect(self.editor.paste)
		self.actionFind.triggered.connect(self.find)
		self.actionReplace.triggered.connect(self.replace)
		self.actionRun.triggered.connect(self.run)
		self.actionRunCustom.triggered.connect(self.runCustom)
		self.actionShell.triggered.connect(self.shell)
		self.actionFont.triggered.connect(self.Font)
	def margin_clicked(self,margin_nr,line_nr,state):
		self.editor.markerAdd(line_nr,margin_nr)
	def margin_right_clicked(self,margin_nr,line_nr,state):
		self.editor.markerDelete(line_nr,margin_nr)
	def new(self):
		if self.windowTitle().endswith("*"):
			self.dialogs.MsgQuestion("Do you want to save your file?")
			if(self.dialogs.getclickstatus()=="accept"):
				if self.filename is None:
					self.saveAs()
				else:
					self.save()
		self.editor.setText("")
		self.setWindowTitle("Untitled")
	def open(self):
		if self.windowTitle().endswith("*"):
			self.dialogs.MsgQuestion("Do you want to save your file?")
			if(self.dialogs.getclickstatus()=="accept"):
				if self.filename is None:
					self.saveAs()
				else:
					self.save()
		filename=self.saveLoad.OpenDialog()
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
				self.dialogs.Message("File Saved successfully")
				self.setWindowTitle(self.filename)
			else:
				self.dialogs.Error("File could not be saved")
	def saveAs(self):
		self.filename=self.saveLoad.SaveDialog()
		returnval=Save(self.editor.text(),self.filename)
		if(returnval):
			self.dialogs.Message("File Saved successfully")
			self.setWindowTitle(self.filename)
		else:
			self.dialogs.Error("File could not be saved")
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
	def shell(self):
		Shell()
	def Font(self):
		font, ok=QFontDialog.getFont()
		if ok:
			self.editor.setFont(font)
			self.lexer.setFont(font)
			self.editor.setLexer(self.lexer)
	def openFile(self,signal):
		fileName=self.fileSysView.model().filePath(signal)
		if fileName.endswith("py") or fileName.endswith("pyw"):
			if self.windowTitle().endswith("*"):
				self.dialogs.MsgQuestion("Do you want to save your file?")
				if self.dialogs.getclickstatus()=="accept":
					if self.filename is None:
						self.saveAs()
					else:
						self.save()
			data=Open(fileName)
			if data is not None:
				self.editor.setText(data)
				self.setWindowTitle(fileName)
				self.filename=fileName
	def fileChanged(self):
		title=self.windowTitle()
		if not(title.endswith("*")):
			self.setWindowTitle(title+" *")
	def replace(self):
		replaceObj=replaceDialog(self,self.editor)
	def find(self):
		findObj=findDialog(self,self.editor)
if __name__=="__main__":
	app=QApplication([])
	app.setStyle(QStyleFactory.create("Fusion"))
	textEdit=MainWindow()
	exit(app.exec_())

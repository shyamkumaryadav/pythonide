# Python IDE

---

# Steps To Setup you System

---
  * [Download Git and Install](https://git-scm.com/downloads 'download & install')
  * Make a [GitHub Account](https://github.com/join)
  * Go And [Fork this repository](https://github.com/shyamkumaryadav/pythonide/fork "Python IDE")
  * set value on git
  `git config --global user.email "you@example.com"`
	`git config --global user.name "Your Name"`
  * Check out the source code with:
  `git clone https://github.com/YOUR_GITHUB_USERNAME/pythonide.git`
  * Start a new git branch with
	`cd pythonide`
	* install all Required pip by
	`python -m pip install -r requirements.txt`
	* after adding some changes and features
	`git add -A`
	`git commit -m 'your message'`
	`git push origin master`
	---


> This file will run you through the work I have done( the work is neither optimized nor is it complete(Find and replace is missing and many more))

| File&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Description |
| ----------------------- | ------------------ |
| [MainWindow.py](https://github.com/shyamkumaryadav/pythonide/find/master)| Main Entry Point of the IDE |
| [Dialogs.py](https://github.com/shyamkumaryadav/pythonide/find/master)| Base Dialogs( Message, Warning and Question) |
| [SaveLoad.py](https://github.com/shyamkumaryadav/pythonide/find/master)| Save and Open Dialogs |
| [Operations.py](https://github.com/shyamkumaryadav/pythonide/find/master)| Backend for the save/load (open) operations |
| [Find.py](https://github.com/shyamkumaryadav/pythonide/find/master)| File for implementing Find functionality |
| [Replace.py](https://github.com/shyamkumaryadav/pythonide/find/master)| File for implementing Replace functionality |


## Pending
> 1. Improvement for Find/Replace functionality
> 2. file for changing encoding/ EOL and to save such files
> 3. Improving the shell like interface
> 4. Debugging
> 5. Improvement in the interface of running the file within the application (as well as showing the output in a new window)

## Features:
1. Syntax Highlighting
2. Bracket Matching

## screenshot
![Python IDE Logo](/screenshot/pythonide.png)


Built using:
Python 3.7.4:
[Official site](https://www.python.org/)
PyQt5 5.14.2:
[Download from PyPI](https://pypi.org/project/PyQt5/) or [Official site](https://www.riverbankcomputing.com/software/pyqt/download5)
QScintilla 2.11.4:
[Download from PyPI](https://pypi.org/project/QScintilla/) or [Official Site](https://www.riverbankcomputing.com/software/qscintilla/intro)

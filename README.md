# Python IDE

---

# Steps To Setup you System

---  
  * [Downlado Git and Install](https://git-scm.com/downloads 'download & install')  
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


This file will run you through the work I have done( the work is neither optimized nor is it complete(Find and replace is missing and many more))
MainWindow.py -----> Main Entry Point of the IDE
Dialogs.py -----> Base Dialogs( Message, Warning and Question)
SaveLoad.py -----> Save and Open Dialogs
Operations.py -----> Backend for the save/load (open) operations

Untested and redundant files:
SaveOperation.py ------> An earlier version of Operations.py
FindModified.py -----> An untested version for the find dialog

Pending:
file for Replace functionality
file for changing encoding/ EOL and to save such files
Shell like interface
Debugging
Running the file within the application (as well as showing the output in a new window)

Built using:
Python 3.7.4 shell
PyQt5 5.14.2
QScintilla 2.11.4
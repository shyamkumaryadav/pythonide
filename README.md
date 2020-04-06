# Python IDE

---

# Steps To Contribute

### S 1

<p>
	1. [Fork this repository](https://github.com/shyamkumaryadav/pythonide/fork)

	2. Check out the source code with:
		git clone git@github.com:YOUR_GITHUB_USERNAME/pythonide.git

	3. Start a new git branch with
		cd youtube-dl
		git checkout -b yourextractor


Start a new git branch with
</p>
---
<p>
	1. yes python
	2. Run the requirements.txt (C:> <u>python -m pip install -r requirements.txt<\u>)
	3. 
<p>

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
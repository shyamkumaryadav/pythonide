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
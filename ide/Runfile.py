from subprocess import Popen
from platform import system
def Runfile(filename,options=None):
    if system()=="Windows":
        file_handle=open("out.bat","w")
        file_handle.write("python "+filename)
        if options is not None:
            file_handle.write(" ",options)
        file_handle.write("\npause")
        file_handle.close()
        process=Popen(["out.bat"])
        exit_code=process.wait()
    elif system()=="Linux":
        file_handle=open("out.sh","w")
        file_handle.write("python3 "+filename)
        if options is not None:
            file_handle.write(" ",options)
        file_handle.close()
        process=Popen(["out.sh"])
        exit_code=process.wait()
def Shell():
    if system()=="Windows":
        process=Popen(["shell.bat"])
        exit_code=process.wait()
    elif system()=="Linux":
        process=Popen(["shell.sh"])
        exit_code=process.wait()
        

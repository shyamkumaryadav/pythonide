def Save(data,filename):
    try:
        file_handle=open(filename,"w")
        file_handle.write(data)
        file_handle.close()
        return True
    except:
        return False
def Open(filename):
    try:
        file_handle=open(filename,"r")
        data=file_handle.read()
        file_handle.close()
        return data
    except:
        return None

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
        print("File Handle",file_handle)
        data=file_handle.read()
        file_handle.close()
        print("Data")
        return data
    except:
        return None

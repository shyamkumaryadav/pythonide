from time import ctime
def style_settings(avail_styles):
    try:
        file_handle=open("style.file","r")
        style=file_handle.read()
        file_handle.close()
        return style
    except:
        print("Style settings not found. Guessing this is the first time of execution")
        print("\nSelect a style")
        j=1
        for i in avail_styles:
            print(f"{j}) {i}\n")
            j+=1
        style=input("Enter a style(Enter the name in the way it is displayed on the screen):\t")
        while style not in avail_styles:
            print("Please enter the name as shown above")
            style=input("Enter a style(Enter the name in the way it is displayed on the screen):\t")
        file_handle=open("style.file","w")
        file_handle.write(style)
        file_handle.close()
        print("Settings saved successfully")
        file_handle=open("availstyles.txt","w")
        for i in avail_styles:
            file_handle.write(f"{i}\n")
        print(f"Available styles as of {ctime()} is stored in file availstyles.txt")
        file_handle.close()
        return style
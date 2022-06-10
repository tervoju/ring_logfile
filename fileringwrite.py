from datetime import datetime

# Getting the current date and time
dt = datetime.now()

cnt = 0
idx = 0

#does not work 

def writeringfile(csv_str):
    global cnt, idx
    # Open the file in append & read mode ('a+')
    if cnt < 9:
        with open("sample0.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
        
            # Append text at the end of file
            str_str = str(cnt) + " " + str(dt)  + csv_str 
            file_object.write(str_str)
            cnt = cnt + 1
    else:
        idx = 

if __name__  == "__main__":
    x = range(20)
    for n in x:
        writeringfile("asd, adsa,adsa,")
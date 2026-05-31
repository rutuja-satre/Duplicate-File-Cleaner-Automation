# Import required modules
import time
import sys
import os
import hashlib   #to check checksum

# Calculate MD5 checksum of a file
def CalculateChecksum(path, BlockSize = 1024):
    fobj = open(path ,'rb')  

    hobj = hashlib.md5()       
    buffer = fobj.read(BlockSize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

# Create log file and write header information
def DirectoryWatcher(DirectoryName = "Logger"):

    flag = os.path.isabs(DirectoryName)

    if(flag==False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if(flag==False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag==False):
        print("Path is valid but the target is not a directory")
        exit()

    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        for fname in FileNames:
           fname = os.path.join(FolderName,fname)
           checksum = CalculateChecksum(fname)
       

    timestamp = time.ctime()

    filename = "Logger%s.log" %(timestamp)   #show timestamp in filename
    filename = filename.replace(" ","_")   #replace space by underscore
    filename = filename.replace(":","_") 

    fobj = open(filename,"w")

    Border = "-"*54

    fobj.write(Border+"\n")
    fobj.write("This is a log file of Automation Script\n")
    fobj.write("This is a directory cleaner Script\n")

    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("This is created at \n"+timestamp+"\n")
    fobj.write(Border+"\n") 

    return fobj
# Find duplicate files using checksum comparison
def FindDuplicate(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag==False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag==False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag==False):
        print("Path is valid but the target is not a directory")
        exit()

    Duplicate = {}

    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
               Duplicate[checksum].append(fname)        
            else:
               Duplicate[checksum] = [fname]
    return Duplicate

# Display duplicate files 
def DisplayResult(MyDict):
    Result = list(filter(lambda x: len(x)>1, MyDict.values()))

    Count = 0
    for value in Result:
        for subvalue in value:
            Count = Count+1
            print(subvalue)

        print("---------------------------")
        print("Value of count is : ",Count)
        print("---------------------------")

        Count = 0

# Delete duplicate files and store deleted file names in log file
def DeleteDuplicate(MyDict,fobj):
    Result = list(filter(lambda x: len(x)>1, MyDict.values()))

    Count = 0
    cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count+1
            if (Count > 1):
                filename = os.path.basename(subvalue)
                fobj.write("Deleted file : " + filename + "\n")
                os.remove(subvalue)
                cnt = cnt+1
        Count = 0

    fobj.write("\n")
    fobj.write("Total deleted file : " + str(cnt) + "\n")

# Main function
def main():
    #header
    Border = "-"*54
    print(Border)
    print("---------------Automation--------------------")
    print(Border)

    if(len(sys.argv)==2):
        if((sys.argv[1] == "--h") or (sys.argv[1]=="--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1]=="--U")):
            print("Use the given script as ")
            print("ScriptName.py NameOfDirectory")
            print("Please provide valid absolute path")

        else:
            fobj = DirectoryWatcher(sys.argv[1])
            Result = FindDuplicate(sys.argv[1])
            DeleteDuplicate(Result,fobj)
            fobj.close()

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : used to display the usage")

#footer
    print(Border)
    print("--------------Thank you for using script--------------")
    print(Border)


if __name__=="__main__":
    main()

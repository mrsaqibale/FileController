import linecache
import os.path
import os
import time
from colorama import Fore
global xyzCounter
xyzCounter = 0
def MyTool():
    i = """
    \t ____             __                           
    \t|  _ \ _ __ ___  / _| ___  ___ ___  ___  _ __ 
    \t| |_) | '__/ _ \| |_ / _ \/ __/ __|/ _ \| '__/ """
    p="""
    \t|  __/| | | (_) |  _|  __/\__ \__ \ (_) | |   """
    s ="""
    \t| |   |_|  \___/| |  \___||___/___/\___/|_|
    \t|_|             |_|                                     
    """
    time.sleep(0.4)
    print(Fore.LIGHTGREEN_EX,"\tTool By" ,end='')
    time.sleep(0.1)
    print(Fore.LIGHTGREEN_EX,i,end='')
    time.sleep(0.2)
    print(Fore.LIGHTMAGENTA_EX,p,end='')
    time.sleep(0.3)
    print(Fore.LIGHTYELLOW_EX,s,end='')
    print(Fore.LIGHTYELLOW_EX,"\t\t\t\t\t   Professor")
def NewFileCopy(count,Line):
    count -=1
    x =0 
    NewFileObject = open(NewFileName,'a')
    NewFileObject.write('\n\n\nNew Result\n\n')
    while x < Line:
        FinalString = linecache.getline(CheckFile,count)
        count -=1
        NewFileObject.write(str(FinalString))
        x +=1
        
    NewFileObject.close() 
def ReadFileMe(PrintLine,FindMe):
    obj = open(CheckFile, "r")
    count = 0
    for x in obj.readlines():
        count+=1
        list =[x]
        for y in list:
            if FindMe in y:
                NewFileCopy(count,PrintLine)
    obj.close()
    # ###########################################
def NewFileNames():
    flag = True
    while flag:
        print(Fore.BLUE+"Enter name of new file also you can set path :",Fore.LIGHTRED_EX,"/home/Professor/file.txt  ")
        fname = input()
        PathExsist = os.path.exists(fname)
        if PathExsist:
            print(Fore.LIGHTRED_EX+"This name Already Exsist: ")
            flag = True
        else:
            return fname
            flag = False
            
def CheckStatus():
    obj = open(CheckFile,"r")
    if FindMe in obj.read():
        obj.close()
        return True
    else: 
        obj.close()
        return False
flag = True
while(flag==True):  
    os.system('clear')
    MyTool()        
    print(Fore.BLUE,'\n\nEnter the path of the file "Example',Fore.LIGHTRED_EX,' home/professor/Desktop/file.txt" ')        
    CheckFile = input()
    pathExsist = os.path.exists(CheckFile)
    if pathExsist:
        if(CheckFile[-4:] == '.txt'):
            print(Fore.BLUE,"Enter string Which you want to Find:",Fore.LIGHTRED_EX,"__  ")
            FindMe = input()
            if(len(FindMe)):
                if CheckStatus():
                    NewFileName = NewFileNames()
                    print(Fore.BLUE,"How much lines Print:  ")
                    PrintLines = input()

                    if(len(PrintLines) ):
                        try:
                            PrintLine = int(PrintLines)
                        except ValueError as verr:
                            print(Fore.LIGHTRED_EX,"Please enter some Number:  ")
                        if(isinstance(PrintLine,int)):
                            ReadFileMe(PrintLine,FindMe)
                    else:
                        print(Fore.LIGHTRED_EX,"Please enter some Number:  ")
                else:
                    print(Fore.LIGHTRED_EX,"String can't match:  ")
            else :
                print(Fore.LIGHTRED_EX,"The String is Empty, so please enter some string:  ")
        else:
            print(Fore.LIGHTRED_EX,'Please Enter your File in the Text Format: "file.txt"')
    
    else :
        print(Fore.LIGHTRED_EX,"File is not Exist ")
    print(Fore.LIGHTYELLOW_EX,"PRESS [Y] TO CONTINUE: _\b",end='')
    choice = input()
    if( choice == 'y'):
        flag = True
    else:
        flag = False



    


import os
import os.path


dir='./'


def listUiFile():
    list = []
    files=os.listdir(dir)
    for filename in files:
        if os.path.splitext(filename)[1] == '.qrc':
            list.append(filename)
    return list


def transPyFile(filename):
    return os.path.splitext(filename)[0]+'.py'


def runMain():
    list=listUiFile()
    for uifile in list:
        pyfile=transPyFile(uifile)
        cmd='pyrcc5 -o {pyfile} {uifile}_rc'.format(pyfile=pyfile,uifile=uifile) #注意{pyfile} {uifile}之间有空格
        os.system(cmd) 

if __name__ == "__main__" :
    runMain()
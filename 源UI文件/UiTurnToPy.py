import os
import os.path

#ui文件所在路径
dir='./'

#列出目录下所有的ui文件
def listUiFile():
    list = []
    files=os.listdir(dir)
    for filename in files:
        if os.path.splitext(filename)[1] == '.ui':
            list.append(filename)
    return list

#把扩展名为.ui的文件改成扩展名为.py的文件
def transPyFile(filename):
    return os.path.splitext(filename)[0]+'.py'

#调用系统命令把ui文件转换成python文件
def runMain():
    list=listUiFile()
    for uifile in list:
        pyfile=transPyFile(uifile)
        cmd='pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile,uifile=uifile) #注意{pyfile} {uifile}之间有空格
        os.system(cmd) 

if __name__ == "__main__" :
    runMain()
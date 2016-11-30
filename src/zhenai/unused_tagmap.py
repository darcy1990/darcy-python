# Filename: set.py
# python 3.x

import os
import shutil 
import time

basedir = "C:\\Users\\Administrator\\Desktop\\删除无流量链接\\tagmap\\" #目录

# 输入
website = basedir + "tagmap_website_key.txt" # 用户日志
database = basedir + "allkeys.txt" # 服务器上所有文件的key
datadir = basedir + "data"

# 输出
deletekeys = basedir + "\\data\\deletekeys" + time.strftime("%Y%m%d") + ".txt" # 服务器上所有文件的key
set_log = set()
set_database = set()
size = 20000

def readlog():
    print("reading log ...")
    fp = open(website, 'rb')
    while True:
        fdata = fp.readline()
        if not fdata:
            break
        data = str(fdata, encoding = "gbk")
        set_log.add(data.strip())
    fp.close()

def readdatabase():
    print("reading database ...")
    fp = open(database, 'rb')
    while True:
        fdata = fp.readline()
        if not fdata:
            break
        data = str(fdata, encoding = "gbk")
        set_database.add(data.strip())
    fp.close()

def write(result, fname):
    f = open(fname,'a')
    f.write(result)
    f.close
        
def writedecode(s, fname):
    print("writing decoded ...")
    l = list(s)
    l.sort()
    s = len(l) // size
    for i in range(0, s + 1):
        start = i * size
        end = (i + 1) * size if ((i + 1) * size < len(l)) else len(l)
        dice = l[start:end]
        content = ""
        for j in range(0, len(dice)):
            content += "http:/www.zhenai.com/tagmap/" + dice[j] + "\n"
        write(content, fname)
        

if __name__=='__main__':
    if os.path.exists(datadir):
        shutil.rmtree(datadir,True)
    os.makedirs(datadir)
        
    readlog()
    print(len(set_log))
    readdatabase()
    print(len(set_database))
    
    print("do minus operation ...")
    result = set_database - set_log
    print(len(result))
    
    writedecode(result, deletekeys)
    
    
    


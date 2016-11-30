"""Handling unused link
given all links and used links, output unused links
python 3.x
"""

import urllib.parse
import os
import shutil
import time

basedir = "C:\\Users\\Administrator\\Desktop\\删除无流量链接\\kwsearch\\" #目录

# 输入
website = basedir + "kwsearch_website.txt" # 用户日志
database = basedir + "seoKeysort.txt" # 数据库关键词
datadir = basedir + "data"

# 输出
website_decode = basedir + "data\\seoKey.tmp" # 临时文件，从用户日志里获取的关键词
output = basedir + "data\\keys.txt" # 需要从数据库删除的关键词
url_prefix = basedir + "data\\unusedUrl" + time.strftime("%Y%m%d") # 需要提交删除的url
age_prefix = basedir + "data\\ageUrl" + time.strftime("%Y%m%d") # 需要提交删除的url

set_log = set()
set_database = set()
set_age = set()
size = 20000

def read_log():
    print("reading log ...")
    fp = open(website, 'rb')
    while True:
        fdata = fp.readline()
        if not fdata:
            break
        data = str(fdata, encoding = "utf-8")
        arr = data.split()
        if "age" in arr[0]:
            set_age.add(arr[0])
            continue
        
        decode_url = urllib.parse.unquote(urllib.parse.unquote(arr[0]))
        if (decode_url.endswith("/m") or decode_url.endswith("/w")):
            decode_url = decode_url[0:len(decode_url) - 2]
        key = decode_url[30:]
        set_log.add(key)
    fp.close()

def read_database():
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
    
def do_slice(s):
    print("doing slicing ...")
    l = list(s) # better not define variable like l, o
    l.sort()
    s = len(l) // size
    for i in range(0, s + 1):
        start = i * size
        end = (i + 1) * size if ((i + 1) * size < len(l)) else len(l)
        dice = l[start:end]
        content = ""
        for j in range(0, len(dice)):
            content += dice[j] + "\n"
        write(content, output)
        content = ""
        for k in range(0, len(dice)):
            encoded_url = urllib.parse.quote(dice[k])
            content += "http://www.zhenai.com/kwsearch/" + encoded_url + "\n"
        write(content, url_prefix + str(i) + ".txt")

def do_slice2(s):
    print("doing slicing2 ...")
    l = list(s)
    l.sort()
    s = len(l) // size
    for i in range(0, s + 1):
        start = i * size
        end = (i + 1) * size if ((i + 1) * size < len(l)) else len(l)
        dice = l[start:end]
        content = ""
        for j in range(0, len(dice)):
            content += dice[j] + "\n"
        write(content, age_prefix + str(i) + ".txt")
        
def write_decode(s, fname):
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
            content += l[j] + "\n"
        write(content, fname)
        

if __name__=='__main__':
    if os.path.exists(datadir):
        shutil.rmtree(datadir,True)
    os.makedirs(datadir)   
        
    read_log()
    print(len(set_log))
    write_decode(set_log, website_decode)
    read_database()
    print(len(set_database))
    
    print("do minus operation ...")
    result = set_database - set_log
    print(len(result))
    
    do_slice(result)
    
    do_slice2(set_age)
    


#!/usr/bin/pythonw
# Filename: dataprocess.py
# python 3.x

import os
import re
import urllib.parse

pattern = re.compile(r'bot|spider|Spider')

p = r'/(.*).zhenai.com/'

s = os.sep #根据unix或win，s为\或/

basedir = "C:\\Users\\Administrator\\Desktop\\删除无流量链接"

root = basedir + "\\data" #要遍历的目录

search = root + "\\search.txt"

website = root + "\\website.txt"

if __name__=='__main__':
    if os.path.exists(search):
        os.remove(search)
    if os.path.exists(website):
        os.remove(website)
    fsearch = open(search,'w', encoding='gbk')
    fwebsite = open(website,'w', encoding='gbk')
    
    for rt, dirs, files in os.walk(root):
        for f in files:
            fp = open(root + "/" + f, 'rb')
            while True:
                fdata = fp.readline()
                if not fdata:
                    break
                data = str(fdata, encoding = "utf-8")
                arr = data.split("\t")
                source = arr[2]
                urls = arr[3].split()
                url = re.sub(p, '/www.zhenai.com/', urls[0])
                decode_url = urllib.parse.unquote(url)
                print(decode_url)
                match = pattern.search(source);
                if match:
                    fsearch.write(decode_url + "\n")
                else:
                    fwebsite.write(decode_url + "\n")
        fsearch.close()
        fwebsite.close()
            

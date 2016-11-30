'''
Created on 2015年12月15日

@author: Administrator
'''

import urllib.parse

url = "http:/www.zhenai.com/kwsearch/%25E4%25B8%2587%25E5%25AE%2581%25E5%25A5%25B3%25E6%2580%25A7%25E5%25BE%2581%25E5%25A9%259A%25E7%25BD%2591"
decode_url = urllib.parse.unquote_plus(url)
print(url)
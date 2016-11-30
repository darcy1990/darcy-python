# rundata for seo
# ∂‡œﬂ≥Ã≤‚ ‘£¨ ß∞‹

from multiprocessing import pool
import re
import random
import urllib.request

reg_str = r'.*(taiwan|xianggang|aomen|zhejiang|yunnan|xinjiang|xizang|sichuan|shanxi1|shanxi|shandong|qinghai|ningxia|neimenggu|liaoning|jiangxi|jiangsu|jilin|hunan|hubei|heilongjiang|henan|hebei|hainan|guizhou|guangxi|gansu|fujian|anhui|chongqing|tianjin|shanghai|beijing|guangdong|xinjie|jiulong1|zhoushan|taizhou1|quzhou1|lishui1|jinhua|jiaxing|huzhou|shaoxing|ningbo|wenzhou|hangzhou|diqing|nujiang|dehong|xishuangbanna|honghe1|puer|lijiang|yuxi|baoshan1|lincang|chuxiong|dali1|wenshan|zhaotong|qujing|kunming|yili|boertala|kezilesukeerkezi|tacheng|changji|hetian|kashen|akesu|tulufan|hami|bayinguoleng|aletai|kelamayi|wulumuqi|linzhi|ali|rikaze|shannan|changdu|naqu|lasa|dazhou|bazhong|suining2|guangan|meishan|ziyang1|deyang|panzhihua|luzhou|yibin|zigong|neijiang|nanchong|guangyuan|ganzi|yaan|aba|mianyang|liangshan1|leshan|chengdu|shangluo|xianyang|tongchuan|hanzhong|ankang|baoji|yulin|yanan|weinan|xian|lvliang|jinzhong|shuozhou|jincheng|changzhi|yangquan|yuncheng1|linfen|datong1|xinzhou1|taiyuan|laiwu|binzhou|rizhao|jining|zaozhuang|linyi2|heze|taian1|yantai|weifang|dongying|dezhou|liaocheng|zibo|jinan|weihai|qingdao|hainanzangzuzizhizhou|huangnan|haibei|haidongdi|haixi|yushu1|guoluo|xining|zhongwei|wuzhong|guyuan1|shizuishan|yinchuan|wulanchabu|bayannaoer|hulunbeier|eerduosi|xingan2|alashanmeng|xilinguolemeng|tongliao|chifeng|wuhai|baotou|huhehaote|huludao|liaoyang|panjin|fuxin|jinzhou2|dandong|benxi|dalian|yingkou|anshan|fushun1|tieling|shenyang|xinyu|fuzhou1|jian1|ganzhou|pingxiang2|yichun|yingtan|shangrao|jingdezhen|jiujiang|nanchang|suqian|taizhou|huaian|nantong|yangzhou|yancheng|lianyungang|zhenjiang|changzhou|xuzhou|wuxi|suzhou|nanjing|yanbian1|baishan|liaoyuan|songyuan|baicheng1|siping|tonghua|changchun|xiangxi|yongzhou|xiangtan|zhangjiajie|chenzhou|shaoyang|hengyang|huaihua|loudi|changde|yueyang|yiyang2|zhuzhou|changsha|suizhou|xiangyang|xiaogan|jingmen|huanggang|jingzhou1|enshi|yichang|shiyan|xianning|ezhou|huangshi|wuhan|qitaihe|heihe|yichun1|shuangyashan|hegang|jixi1|daxinganling|daqing|qiqihaer|mudanjiang|jiamusi|suihua|haerbin|jiaozuo|puyang1|hebi|shangqiu|kaifeng1|nanyang|sanmenxia|pingdingshan|luoyang|zhoukou|xinyang|luohe|zhumadian|xuchang|anyang|xinxiang|zhengzhou|zhangjiakou|baoding|chengde|qinhuangdao|langfang|tangshan|cangzhou|handan|xingtai|hengshui|shijiazhuang|sanya|haikou|qiannan|qiandong|qianxi2|tongren1|bijie|zunyi|anshun|liupanshui|guiyang|hezhou|chongzuo|laibin|guigang|beihai|hechi|wuzhou|guilin|fangchenggang|yulin1|baise|qinzhou|liuzhou|nanning|linxia|longnan1|baiyin|qingyang2|jiayuguan|gannan1|pingliang|dingxi|tianshui|jinchang|jiuquan|wuwei1|zhangye|lanzhou|ningde|putian|sanming|longyan|zhangzhou|nanping|quanzhou1|xiamen|fuzhou|xuancheng|chizhou|maanshan|bozhou|huaibei|tongling|huangshan|anqing|wuhu|chuzhou|liuan|fuyang1|suzhou1|bangbu|huainan|hefei|shenzhen|yunfu|shanwei|jieyang|heyuan|yangjiang|chaozhou|qingyuan3|jiangmen|shaoguan|meizhou|shantou|maoming|zhongshan3|huizhou|dongguan|zhaoqing|zhuhai|zhanjiang|foshan|guangzhou).*'

reg_keyword_str = r"<th><a href=\"http://album.zhenai.com/u/\d+\" target=\"_blank\">"

reg_keyword_jiaoyou_str = r'<a class=\"name\" href=\"http://album.zhenai.com/u/\d+\" target=\"_blank\">'

reg_keyword_city_str = r'<td><a href=\"http://album.zhenai.com/u/\d+\" target=\"_blank\">'

keyword = "<th><a href=\"http://album.zhenai.com/u"

keyword_jiaoyou = "<a class=\"name\" href=\"http://album.zhenai.com/u"

keyword_city = "<td><a href=\"http://album.zhenai.com/u"
 
def go(s):
    print('go...')
    
    if len(s) == 0:
        print('set is empty..')
        return
    
    urls = set([])
    
    for url in s:
        i = random.randint(0,2)
        if i > 0:
            if is_first_or_seconde_level_city(url):
                p.apply_async(count, args=(url,))
            else:
                urls.add(url)
        else:
            if is_first_or_seconde_level_city(url):
                urls.add(url)
            else:
                p.apply_async(count, args=(url,))
    go(urls)
    
def is_first_or_seconde_level_city(url):
    keys = url.split('//')
    u = keys[1]
    k = u.split('/')
    
    match = reg.match(k[2])
    if match:
        return True
    else:
        return False

def count(url):
    reg_keyword = re.compile(reg_keyword_str) # how to share variables between processes
    reg_keyword_jiaoyou = re.compile(reg_keyword_jiaoyou_str)
    reg_keyword_city = re.compile(reg_keyword_city_str)
    
    if len(url) == 0:
        write('Blank Line ' + url)
        
    response = urllib.request.urlopen(url)
    html = response.read().decode('gbk','ignore')
    if len(html) == 0 or '404 Error page' in html:
        write('Error ' + url)
    if 'zhenghun' in url:
        if keyword not in html:
            write('0 ' + url)
        result = reg_keyword.findall(html)
        write(str(len(result)) + ' ' + url)
    elif 'jiaoyou' in url or 'list' in url:
        if keyword_jiaoyou not in html:
            write('0 ' + url)
        result = reg_keyword_jiaoyou.findall(html)
        write(str(len(result)) + ' ' + url)
    elif 'xiangqin' in url:
        if keyword_city not in html:
            write('0 ' + url)
        result = reg_keyword_city.findall(html)
        write(str(len(result)) + ' ' + url)


def write(result):
    f = open('C:\\Users\\Administrator\\Desktop\\rundata\\pythonCount.txt','a')
    f.write(result)
    f.close
    
if __name__=='__main__':
    p = pool.Pool(10)
    
    reg = re.compile(reg_str)
     
    fo = open("C:\\Users\\Administrator\\Desktop\\rundata\\allUrls.txt");
    
    urls = set([])

    while True:
        line = fo.readline();
        if len(line) == 0:
            break
        urls.add(line)

    fo.close()
    
    go(urls)
    
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')



    
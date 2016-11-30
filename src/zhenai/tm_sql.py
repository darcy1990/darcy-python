# Filename: sqlgenerator.py
# python 3.x

basedir = "C:\\Users\\Administrator\\Desktop\\seoDelKeys\\" #目录
keys = basedir + "tmKeys.txt" # 需要从数据库删除的关键词
output = basedir + "tmSql.txt" # 需要从数据库删除的关键词

def write(result, fname):
    f = open(fname,'a')
    f.write(result)
    f.close

if __name__=='__main__':
    print("reading keys ...")
    fp = open(keys, 'rb')
    sql = ""
    i = 0
    while True:
        fdata = fp.readline()
        if not fdata:
            break
        data = str(fdata, encoding = "gbk")
        i = i + 1
        sql += "update zhenai_biz.SeoTagMap set status = 0 where url = \"" + data.strip()[29:] + "\"\n"
    write(sql, output)
    fp.close()
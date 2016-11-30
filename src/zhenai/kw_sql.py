# Filename: sqlgenerator.py
# python 3.x

basedir = "C:\\Users\\Administrator\\Desktop\\seoDelKeys\\" #目录
keys = basedir + "kwKeys.txt" # 需要从数据库删除的关键词
output = basedir + "kwSql.txt" # 需要从数据库删除的关键词

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
        sql += "update zhenai_biz.SeoKeyWord set urlStatus = 0 where seokey = '" + data.strip() + "'\n"
        if i // 5000 == 0:
            write(sql, output)
            i = 0
            sql = ""
    write(sql, output)
    fp.close()
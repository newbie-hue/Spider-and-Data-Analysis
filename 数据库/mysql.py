import pymysql



'''
1、数据库的链接和创建视图
'''
# db=pymysql.connect(host='localhost',user='root',password='caomengqi1234',port=3306)
# cursor=db.cursor()
# cursor.execute("SELECT VERSION()")
# data=cursor.fetchone()
# print('Database version:',data)
# # cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

'''
2、数据库的链接和创建表格
'''
# db=pymysql.connect(host='localhost',user='root',password='caomengqi1234',port=3306,db='spiders')
# cursor=db.cursor()
# sql="CREATE TABLE IF NOT EXISTS students " \
#     "(id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL, PRIMARY KEY (id))"
# cursor.execute(sql)
# db.close()


'''
3、数据库的链接和插入数据
'''
# id='20210001'
# user='Bob'
# age=20
#
#
# db=pymysql.connect(host='localhost',user='root',password='caomengqi1234',port=3306,db='spiders')
# cursor=db.cursor()
# sql="INSERT INTO students(id,name,age) values(%s,%s,%S)"
# try:
#     cursor.execute(sql,(id,user,age))
#     db.commit()
# except:
#     db.rollback()
# db.close()



'''
4、#数据库的更新
'''
#
# db=pymysql.connect(host='localhost',user='root',password='caomengqi1234',port=3306,db='spiders')
# cursor=db.cursor()
#
# sql="UPDATA students SET age=%s name=%s"
#
# try:
#     cursor.excute(sql,(25,"Bob"))
#     db.commit()
#     print("更新成功")
# except:
#     db.rollback()
# db.close()



# 构造字典进行读写
# 链接数据库表
db=pymysql.connect(host="localhost",user="root",password="caomengqi1234",port=3306,db="spiders")
cursor=db.cursor()
#构造通用的储存格式
table="students"
data={
    "id":"20210006",
    "name":"Bojm",
    "age":24
}
keys=",".join(i for i in data)
value=",".join(["%s"]*len(data))
update=",".join(["{key}=%s".format(key=key) for key in data])
#书写SQL语句  on条件为假执行左边的语句，条件为真执行右边的语句
sql='INSERT INTO {table}({keys}) VALUES ({value}) ON DUPLICATE KEY UPDATE  '.format(table=table,keys=keys,value=value)
sql+=update
print(sql)
#执行SQL语句
try:
    cursor.execute(sql,tuple(data.values())*2)
    db.commit()
    print(data,"已录入数据库")
except:
    print("Faild")
    db.rollback()
db.close()




'''
5、数据库的删除
'''
db=pymysql.connect(host='localhost',user='root',password='caomengqi1234',port=3306,db='spiders')
cursor=db.cursor()

table="students"
condtion="age<23"
sql='DELETE FROM {table} WHERE {condtion}'.format(table=table,condtion=condtion)
print(sql)
try:
    cursor.execute(sql)
    print("成功删除满足",condtion,"的信息")
    db.commit()
except:
    db.rollback()
    print("删除失败")


'''
6、查询数据库
'''
sql="SELECT * FROM {table}".format(table=table)
# try:
cursor.execute(sql)
print("cursor:",cursor.rowcount)
one=cursor.fetchone()
print("cursor One:",one)
all=cursor.fetchall()
print("cursor all：",all)
# except:
#     print("Error")
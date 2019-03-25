# -*- coding: utf-8 -*-
import pymysql
import time
import re
import passwd

theId='1'
user=passwd()
way='/sys/bus/w1/devices/28-011432931aaf/w1_slave'
print('系统启动，开始连接数据库')
conn = pymysql.connect(host=user.getHost(), user=user.getUser(), passwd=user.getpasswd(), db="other")
cursor = conn.cursor()
print("成功连接数据库,状态正常")

def order(iid,values):
    global cursor,conn
    iid=str(iid)
    values=str(values)
    itime=str(time.strftime('%Y-%m-%d %H:%M:%S'))
    iorder='insert into pi (id,itime,val) values ('+iid+',"'+itime+'",'+values+');'
    cursor.execute(iorder)
    conn.commit()
try:
    file=open(way,'r')
except Exception as err:
    print(err)
    order(theId,'-404')
    conn.close()
    try:
        file.close()
    except Exception:
        pass
    exit()

try:
    val=file.read()
    crc=re.compile('crc=.*? (.*?)\n').findall(val)[0]
    if crc!='YES':
        order(theId,'-410')
    else:
        t=re.compile('t=(.*?)\n').findall(val)[0]
        t=str(float(t)/1000.0)
        order(theId,t)
except Exception as err:
    print(err)
    order(theId,'-510')
finally:
    file.close()
    conn.close()
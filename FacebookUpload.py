
# coding: utf-8

# In[1]:



#facepy 설치되어있어야 합니다<pip install>
from facepy import GraphAPI
import MySQLdb
import datetime
import time


# In[2]:

# This key is expired every 2 months.
# Need to be Refresh the key in FaceBook Developer
# https://developers.facebook.com/tools/explorer
# Due Date = 2016/10/16
facebook_key='EAABb67MbMAIBABKdPNQZBiJbtCI35JxtQH8aRFSuJEYTbojix03lYHFdgDtOGHYnfce6ALppFKmsemyKWHarpNYYCTLmT5zPKHSUHHaKCObJsMnb4X8WIey54BH6EO9XRsAPdVrUQa5aJxMBS76LmlOZBZB6UEZD'


# In[3]:

graph=GraphAPI(facebook_key)


# In[4]:

today=datetime.date.today()
yesterday=today - datetime.timedelta(1)


# In[5]:

# ***** DO NOT upload more than 5days article at ONCE *****


# In[6]:

year = str.format('%04d'%(yesterday.year))
month=str.format('%02d'%(yesterday.month))
day=str.format('%02d'%(yesterday.day))


# In[9]:

# year='YYYY'
# month='MM'
# day='DD'


# In[10]:

con=MySQLdb.connect(host='218.150.181.131',user='root',passwd='1234',db='link10th',charset='utf8', use_unicode=True)
print u'>>> MySQL(for Facebook) Connected...'
cursor=con.cursor()
sql=str.format('SELECT * FROM link10th.Article WHERE Article.date like \'%s%s%s%%\''%(year,month,day))
# print sql
cursor.execute(sql)
print u'>>> select data from DB done'
sqlResult=cursor.fetchall()
print u'>>> fetch data from DB done'

index=0
for event in sqlResult:
    index+=1
    HEAD=event[2]
    MAIN='\n'.join(event[3:7])
    
    # POST on the MrWriter
    graph.post(path='/feed',message=HEAD+'\n'+MAIN,retry=10)
    print u'>>> MrWriter_LinkLab(BOT) posted article[%d/%d]'%(index,len(sqlResult))

con.commit()
print u'>>>  all transaction(for Facebook) commit  done'
cursor.close()
print u'>>>  cursor(for Facebook) close  done'
con.close()
print u'>>> MySQL(for Facebook) Disonnected...'
print


# In[ ]:




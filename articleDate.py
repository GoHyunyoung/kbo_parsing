
# coding: utf-8

# In[3]:


from BoxScoreParser import BoxScoreParser
from UrlParser import UrlParser


# In[6]:

date=20160517
urlParser = UrlParser(date)
bxsParser=BoxScoreParser(urlParser.urlList[0])
print bxsParser.date


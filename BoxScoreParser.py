
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import urllib2
import re


# In[1]:

#URL넣어주면 해당 박스스코어 파싱
class BoxScoreParser:
    def __init__(self,url):
        self.data = urllib2.urlopen(url)
        self.html = BeautifulSoup(self.data)
        
        #DATE
        self.date = self.html.select('div.yearDate span')[0].text
        
        #AWAY팀명
        self.a_Team=self.html.select('table.socreBoard tr:nth-of-type(2) th')[0].text
        
        #HOME팀명
        self.h_Team=self.html.select('table.socreBoard tr:nth-of-type(3) th')[0].text
        
        #AWAY_SCORE
        tmp=self.html.select('table.socreBoard tr:nth-of-type(2) td')
        self.a_Score=list()
        for score in tmp:
            self.a_Score.append(score.text)
        
        #HOME_SCORE
        tmp=self.html.select('table.socreBoard tr:nth-of-type(3) td')
        self.h_Score=list()
        for score in tmp:
            self.h_Score.append(score.text)
        
        #AWAY_STATUS
        self.a_status=self.html.select('p.results')[0].text
        
        #HOME_STATUS
        self.h_status=self.html.select('p.results')[1].text
        
        #STADIUM
        tmp=self.html.select('p.ballpark')[0]
        #.text 메서드는 unicode형태로 반환
        tmp=tmp.text
        self.stadium=tmp[tmp.find(u'구장')+4:tmp.find(u'관중')].strip()
        
        #HEAD
        headRowNum = len(self.html.select('table.tEx tbody tr'))
        head=dict()
        for i in range(headRowNum):
            key = self.html.select('table.tEx tr:nth-of-type(%d) th'%(i+1))[0].text
            dat = self.html.select('table.tEx tr:nth-of-type(%d) td'%(i+1))[0].text
            dat = dat.strip()
            
            if key==u'심판':
                dat = dat.split()
            else:
                dat = dat.replace(') ',')) ').split(') ')
            head[key]=dat
        
        #AWAY 투수기록
        columns=[u'선수명',u'등판',u'결과',u'승',u'패',u'세',u'이닝',u'타자',u'투구수',u'타수',u'피안타',u'홈런',u'4사구',u'삼진',u'실점',u'자책',u'평균자책점']
        frame=self.html.select('table#xtable3 tbody:nth-of-type(1) tr')
        data=list()    #frame으로부터 데이터를 담을 리스트
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n'):    #한 행(한 투수의 데이터)마다 split한뒤 list로 정리
                tmp.append(dat)
            data.append(tmp)   #정리된 list를 data에 추가
        self.a_pitRecord = pd.DataFrame(data=data,columns=columns)

        #HOME 투수기록
        #col=[u'선수명',u'등판',u'결과',u'승',u'패',u'세',u'이닝',u'타자',u'투구수',u'타수',u'피안타',u'홈런',u'4사구',u'삼진',u'실점',u'자책',u'평균자책점']
        frame=self.html.select('table#xtable3 tbody:nth-of-type(2) tr')
        data=list()    #frame으로부터 데이터를 담을 리스트
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n'):    #한 행(한 투수의 데이터)마다 split한뒤 list로 정리
                tmp.append(dat)
            data.append(tmp)   #정리된 list를 data에 추가
        self.h_pitRecord = pd.DataFrame(data=data,columns=columns)
        #등판:선발의 선수명과 이닝,타자를 get
        # -> h_pitRecord[h_pitRecord[u'등판']==u'선발'].reindex(columns=[u'선수명',u'이닝',u'타자'])
        
        #AWAY_타자기록
        columns=[u'선수명',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10',u'11',u'12',u'타수',u'안타',u'타점',u'득점',u'타율']
        frame=self.html.select('table#xtable1 tbody:nth-of-type(1) tr')
        data=list()
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n')[2:]:
                tmp.append(dat)
            data.append(tmp)
        self.a_batRecord = pd.DataFrame(data=data,columns=columns)
        
        #HOME_타자기록
        columns=[u'선수명',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10',u'11',u'12',u'타수',u'안타',u'타점',u'득점',u'타율']
        frame=self.html.select('table#xtable1 tbody:nth-of-type(2) tr')
        data=list()
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n')[2:]:
                tmp.append(dat)
            data.append(tmp)
        self.h_batRecord = pd.DataFrame(data=data,columns=columns)


# In[ ]:





# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import urllib2
import re


# In[1]:

#URL넣어주면 해당 박스스코어 파싱
class BoxScoreParser:
    def __init__(self,url):
        data = urllib2.urlopen(url)
        html = BeautifulSoup(data)
        
        #DATE
        self.date = html.select('div.yearDate span')[0].text
        
        #AWAY팀명
        self.a_team=html.select('table.socreBoard tr:nth-of-type(2) th')[0].text
        
        #HOME팀명
        self.h_team=html.select('table.socreBoard tr:nth-of-type(3) th')[0].text
        
        #AWAY_SCORE
        tmp=html.select('table.socreBoard tr:nth-of-type(2) td')
        self.a_score=list()
        for score in tmp:
            if score.text==u'-':
                self.a_score.append(0)
            else:
                self.a_score.append(int(score.text))
        
        #HOME_SCORE
        tmp=html.select('table.socreBoard tr:nth-of-type(3) td')
        self.h_score=list()
        for score in tmp:
            if score.text==u'-':
                self.h_score.append(0)
            else:
                self.h_score.append(int(score.text))
        
        #AWAY_STATUS
        self.a_status=html.select('p.results')[0].text
        
        #HOME_STATUS
        self.h_status=html.select('p.results')[1].text
        
        #STADIUM
        tmp=html.select('p.ballpark')[0]
        #.text 메서드는 unicode형태로 반환
        tmp=tmp.text
        self.stadium=tmp[tmp.find(u'구장')+4:tmp.find(u'관중')].strip()
        
        #HEAD
        headRowNum = len(html.select('table.tEx tbody tr'))
        head=dict()
        for i in range(headRowNum):
            key = html.select('table.tEx tr:nth-of-type(%d) th'%(i+1))[0].text
            dat = html.select('table.tEx tr:nth-of-type(%d) td'%(i+1))[0].text
            dat = dat.strip()
            
            if key==u'심판':
                dat = dat.split()
            else:
                dat = dat.replace(') ',')) ').split(') ')
            head[key]=dat
        
        #AWAY 투수기록
        columns=[u'선수명',u'등판',u'결과',u'승',u'패',u'세',u'이닝',u'타자',u'투구수',u'타수',u'피안타',u'홈런',u'4사구',u'삼진',u'실점',u'자책',u'평균자책점']
        frame=html.select('table#xtable3 tbody:nth-of-type(1) tr')
        data=list()    #frame으로부터 데이터를 담을 리스트
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n'):    #한 행(한 투수의 데이터)마다 split한뒤 list로 정리
                tmp.append(dat)
            data.append(tmp)   #정리된 list를 data에 추가
        self.a_pitRecord = pd.DataFrame(data=data,columns=columns)

        #HOME 투수기록
        #col=[u'선수명',u'등판',u'결과',u'승',u'패',u'세',u'이닝',u'타자',u'투구수',u'타수',u'피안타',u'홈런',u'4사구',u'삼진',u'실점',u'자책',u'평균자책점']
        frame=html.select('table#xtable3 tbody:nth-of-type(2) tr')
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
        frame=html.select('table#xtable1 tbody:nth-of-type(1) tr')
        data=list()
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n')[2:]:
                tmp.append(dat)
            data.append(tmp)
        self.a_batRecord = pd.DataFrame(data=data,columns=columns)
        
        #HOME_타자기록
        columns=[u'선수명',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10',u'11',u'12',u'타수',u'안타',u'타점',u'득점',u'타율']
        frame=html.select('table#xtable1 tbody:nth-of-type(2) tr')
        data=list()
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n')[2:]:
                tmp.append(dat)
            data.append(tmp)
        self.h_batRecord = pd.DataFrame(data=data,columns=columns)
        
        
        #WinTeam
        if self.a_score[12] > self.h_score[12]:
            self.winTeam = bxsParser.a_team
            self.winScore = bxsParser.a_score[12]
            self.winTeam_pitRecord = bxsParser.a_pitRecord
            self.winTeam_batRecord = bxsParser.a_batRecord        
            self.loseTeam = bxsParser.h_team        
            self.loseScore = bxsParser.h_score[12]
            self.loseTeam_pitRecord = bxsParser.h_pitRecord
            self.loseTeam_batRecord = bxsParser.h_batRecord
        else:
            self.loseTeam= bxsParser.a_team
            self.loseScore= bxsParser.a_score[12]
            self.loseTeam_pitRecord = bxsParser.a_pitRecord
            self.loseTeam_batRecord= bxsParser.a_batRecord        
            self.winTeam = bxsParser.h_team        
            self.winScore = bxsParser.h_score[12]
            self.winTeam_pitRecord= bxsParser.h_pitRecord
            self.winTeam_batRecord = bxsParser.h_batRecord



# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
from UrlParserForKBO import UrlParserForKBO

import numpy as np
import pandas as pd
import urllib2


# In[144]:

#URL넣어주면 해당 박스스코어 파싱
class Parser_KBO:
    def __init__(self,url):
        data = urllib2.urlopen(url)
        html = BeautifulSoup(data)
        self.boxScore={}
        self.situation={}
        
        
        #-------BEGIN self.boxScore-------#
        self.boxScore['url']=url
        #DATE
        self.boxScore['date'] = html.select_one('div.yearDate span').text.replace('.','')
        
        #AWAY팀명
        self.boxScore['awayTeam']=html.select_one('table.socreBoard tr:nth-of-type(2) th').text
        
        #HOME팀명
        self.boxScore['homeTeam']=html.select_one('table.socreBoard tr:nth-of-type(3) th').text
        
        #AWAY_SCORE
        tmp=html.select('table.socreBoard tr:nth-of-type(2) td')
        self.boxScore['awayScore']=list()
        for score in tmp:
            if score.text==u'-':
                self.boxScore['awayScore'].append(0)
            else:
                self.boxScore['awayScore'].append(int(score.text))
        
        #HOME_SCORE
        tmp=html.select('table.socreBoard tr:nth-of-type(3) td')
        self.boxScore['homeScore']=list()
        for score in tmp:
            if score.text==u'-':
                self.boxScore['homeScore'].append(0)
            else:
                self.boxScore['homeScore'].append(int(score.text))
        
        #AWAY_SUM_OF_SCORE
        self.boxScore['awayScoreSum'] = self.boxScore['awayScore'][12]
        #HOME_SUM_OF_SCORE
        self.boxScore['homeScoreSum'] = self.boxScore['homeScore'][12]
        
        #AWAY_STATUS
        self.boxScore['awayStatus']=html.select_one('div.left p.results').text
        status=html.select_one('div.left p.results').text
        self.boxScore['awayWinCount']=status[:status.find(u'승')]
        self.boxScore['awayLoseCount']=status[status.find(u'승'):status.find(u'패')]
        self.boxScore['awayDrawCount']=status[status.find(u'패'):status.find(u'무')]
        
        #HOME_STATUS
        self.boxScore['homeStatus']=html.select_one('div.left p.results').text
        status=html.select_one('div.left p.results').text
        self.boxScore['homeWinCount']=status[:status.find(u'승')]
        self.boxScore['homeLoseCount']=status[status.find(u'승'):status.find(u'패')]
        self.boxScore['homeDrawCount']=status[status.find(u'패'):status.find(u'무')]
               
        #STADIUM
        tmp=html.select_one('p.ballpark')
        #.text 메서드는 unicode형태로 반환
        tmp=tmp.text
        self.boxScore['stadium']=tmp[tmp.find(u'구장')+4:tmp.find(u'관중')].strip()
        
        #HEAD
        headRowNum = len(html.select('table.tEx tbody tr'))
        head=dict()
        for i in range(headRowNum):
            key = html.select_one('table.tEx tr:nth-of-type(%d) th'%(i+1)).text
            dat = html.select_one('table.tEx tr:nth-of-type(%d) td'%(i+1)).text
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
        self.boxScore['awayPitRecord'] = pd.DataFrame(data=data,columns=columns)

        #HOME 투수기록
        #col=[u'선수명',u'등판',u'결과',u'승',u'패',u'세',u'이닝',u'타자',u'투구수',u'타수',u'피안타',u'홈런',u'4사구',u'삼진',u'실점',u'자책',u'평균자책점']
        frame=html.select('table#xtable3 tbody:nth-of-type(2) tr')
        data=list()    #frame으로부터 데이터를 담을 리스트
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n'):    #한 행(한 투수의 데이터)마다 split한뒤 list로 정리
                tmp.append(dat)
            data.append(tmp)   #정리된 list를 data에 추가
        self.boxScore['homePitRecord'] = pd.DataFrame(data=data,columns=columns)
        #등판:선발의 선수명과 이닝,타자를 get
        # -> homepitRecord[homepitRecord[u'등판']==u'선발'].reindex(columns=[u'선수명',u'이닝',u'타자'])
        
        #AWAY_타자기록
        columns=[u'선수명',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10',u'11',u'12',u'타수',u'안타',u'타점',u'득점',u'타율']
        frame=html.select('table#xtable1 tbody:nth-of-type(1) tr')
        data=list()
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n')[2:]:
                tmp.append(dat)
            data.append(tmp)
        self.boxScore['awayBatRecord'] = pd.DataFrame(data=data,columns=columns)
        
        #HOME_타자기록
        columns=[u'선수명',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10',u'11',u'12',u'타수',u'안타',u'타점',u'득점',u'타율']
        frame=html.select('table#xtable1 tbody:nth-of-type(2) tr')
        data=list()
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n')[2:]:
                tmp.append(dat)
            data.append(tmp)
        self.boxScore['homeBatRecord'] = pd.DataFrame(data=data,columns=columns)
        
        
        #승리팀,패배팀에 대한 멤버변수 설정
        if self.boxScore['awayScore'][12] > self.boxScore['homeScore'][12]:
            self.boxScore['winTeam'] = self.boxScore['awayTeam']
            self.boxScore['winScore'] = self.boxScore['awayScore'][12]
            self.boxScore['winTeamPitRecord'] = self.boxScore['awayPitRecord']
            self.boxScore['winTeamBatRecord'] = self.boxScore['awayBatRecord']    
            self.boxScore['winTeamStatus']=self.boxScore['awayStatus']
            self.boxScore['winTeamWinCount']=self.boxScore['awayWinCount']
            self.boxScore['winTeamLoseCount']=self.boxScore['awayLoseCount']
            self.boxScore['winTeamDrawCount']=self.boxScore['awayDrawCount']
            
            self.boxScore['loseTeam'] = self.boxScore['homeTeam'] 
            self.boxScore['loseScore'] = self.boxScore['homeScore'][12]
            self.boxScore['loseTeamPitRecord'] = self.boxScore['homePitRecord']
            self.boxScore['loseTeamBatRecord'] = self.boxScore['homeBatRecord']
            self.boxScore['loseTeamStatus']=self.boxScore['homeStatus']
            self.boxScore['loseTeamWinCount']=self.boxScore['homeWinCount']
            self.boxScore['loseTeamLoseCount']=self.boxScore['homeLoseCount']
            self.boxScore['loseTeamDrawCount']=self.boxScore['homeDrawCount']
            
        else:
            self.boxScore['loseTeam']= self.boxScore['awayTeam']
            self.boxScore['loseScore']= self.boxScore['awayScore'][12]
            self.boxScore['loseTeamPitRecord'] = self.boxScore['awayPitRecord']
            self.boxScore['loseTeamBatRecord'] = self.boxScore['awayBatRecord']     
            self.boxScore['loseTeamStatus']=self.boxScore['awayStatus']
            self.boxScore['loseTeamWinCount']=self.boxScore['awayWinCount']
            self.boxScore['loseTeamLoseCount']=self.boxScore['awayLoseCount']
            self.boxScore['loseTeamDrawCount']=self.boxScore['awayDrawCount']
                                                     
            self.boxScore['winTeam'] = self.boxScore['homeTeam']        
            self.boxScore['winScore'] = self.boxScore['homeScore'][12]
            self.boxScore['winTeamPitRecord'] = self.boxScore['homePitRecord']
            self.boxScore['winTeamBatRecord'] = self.boxScore['homeBatRecord']
            self.boxScore['winTeamStatus']=self.boxScore['homeStatus']
            self.boxScore['winTeamWinCount']=self.boxScore['homeWinCount']
            self.boxScore['winTeamLoseCount']=self.boxScore['homeLoseCount']
            self.boxScore['winTeamDrawCount']=self.boxScore['homeDrawCount']
        #-------END self.boxScore-------#
            
        #-------BEGIN self.situation-------#
        url=url.replace('BoxScore','Situation')
        data=urllib2.urlopen(url)
        html=BeautifulSoup(data)
        aKeys=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10']
        bKeys=['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10']
        for aKey,bKey in zip(aKeys,bKeys):
            self.situation[aKey]=[(element.text.split()[2],' '.join(element.text.split()[3:])) for element in html.select('table.tEx.Ex2 tbody:nth-of-type(1) td')]
            self.situation[bKey]=[(element.text.split()[2],' '.join(element.text.split()[3:])) for element in html.select('table.tEx.Ex2 tbody:nth-of-type(2) td')]
        #-------END self.boxScore-------#


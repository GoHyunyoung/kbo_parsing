# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from UrlParserForKBO import UrlParserForKBO

import re
import numpy as np
import pandas as pd
import urllib2


# In[2]:

#URL넣어주면 해당 박스스코어 파싱
class Parser_KBO:
    '''
    boxScore : 박스스코어
    ------- key list -------
    [date] : 경기일
    [stadium] : 경기장
    [away/home/winTeam/loseTeam][name] : 팀명
    [away/home/winTeam/loseTeam][score] : 팀별점수(1,2,3,4...12이닝,총점)
    [away/home/winTeam/loseTeam][sum] : 팀별총점
    [away/home/winTeam/loseTeam][status]: 팀전적[승,무,패]
    [away/home/winTeam/loseTeam][pitRecord] : 투수기록(Dataframe형태)
    [away/home/winTeam/loseTeam][batRecord] : 타자기록(Dataframe형태)
    situation : 경기상황
    ------- key list -------
    [away/home/winTeam/loseTeam][이닝][몇번째][player/act]
    
    rank : 팀순위
    ------- key list -------
    0순위 1팀명 2승 3패 4무 5승률 6게임차 7최근10경기 8연속 9홈 10방문
    '''
    def __init__(self,url):
        data = urllib2.urlopen(url)
        html = BeautifulSoup(data)
        self.boxScore={'away':{},'home':{}}
        self.situation={'away':{},'home':{}}
        
        
        #-------BEGIN self.boxScore-------#
        self.boxScore['url']=url
        #DATE
        self.boxScore['date'] = html.select_one('div.yearDate span').text.replace('.','')
        
        #AWAY팀명
        self.boxScore['away']['name']=html.select_one('table.socreBoard tr:nth-of-type(2) th').text
        
        #HOME팀명
        self.boxScore['home']['name']=html.select_one('table.socreBoard tr:nth-of-type(3) th').text
        
        self.boxScore['away']['score']=[]
        self.boxScore['home']['score']=[]
        
        #AWAY_SCORE
        tmp=html.select('table.socreBoard tr:nth-of-type(2) td')
        for score in tmp:
            if score.text==u'-':
                self.boxScore['away']['score'].append(0)
            else:
                self.boxScore['away']['score'].append(int(score.text))
        
        #HOME_SCORE
        tmp=html.select('table.socreBoard tr:nth-of-type(3) td')
        self.boxScore['home']['score']=[]
        for score in tmp:
            if score.text==u'-':
                self.boxScore['home']['score'].append(0)
            else:
                self.boxScore['home']['score'].append(int(score.text))
        
        #AWAY_SUM_OF_SCORE
        self.boxScore['away']['sum'] = self.boxScore['away']['score'][12]
        #HOME_SUM_OF_SCORE
        self.boxScore['home']['sum'] = self.boxScore['home']['score'][12]
        
        #AWAY_STATUS
        status=map(int,re.findall('[\d]+',html.select_one('div.left p.results').text))
        self.boxScore['away']['status']=(status[0],status[2],status[1])
        
        #HOME_STATUS
        status=map(int,re.findall('[\d]+',html.select_one('div.right p.results').text))
        self.boxScore['home']['status']=(status[0],status[2],status[1])
               
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
        self.boxScore['away']['pitRecord'] = pd.DataFrame(data=data,columns=columns)
        self.boxScore['away']['pitRecord'].index=self.boxScore['away']['pitRecord'].pop(u'선수명')

        #HOME 투수기록
        #col=[u'선수명',u'등판',u'결과',u'승',u'패',u'세',u'이닝',u'타자',u'투구수',u'타수',u'피안타',u'홈런',u'4사구',u'삼진',u'실점',u'자책',u'평균자책점']
        frame=html.select('table#xtable3 tbody:nth-of-type(2) tr')
        data=list()    #frame으로부터 데이터를 담을 리스트
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n'):    #한 행(한 투수의 데이터)마다 split한뒤 list로 정리
                tmp.append(dat)
            data.append(tmp)   #정리된 list를 data에 추가
        self.boxScore['home']['pitRecord'] = pd.DataFrame(data=data,columns=columns)
        self.boxScore['home']['pitRecord'].index=self.boxScore['home']['pitRecord'].pop(u'선수명')
        
        #AWAY_타자기록
        columns=[u'선수명',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10',u'11',u'12',u'타수',u'안타',u'타점',u'득점',u'타율']
        frame=html.select('table#xtable1 tbody:nth-of-type(1) tr')
        data=list()
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n')[2:]:
                tmp.append(dat)
            data.append(tmp)
        self.boxScore['away']['batRecord'] = pd.DataFrame(data=data,columns=columns)
        self.boxScore['away']['batRecord'].index=self.boxScore['away']['batRecord'].pop(u'선수명')

        
        #HOME_타자기록
        columns=[u'선수명',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10',u'11',u'12',u'타수',u'안타',u'타점',u'득점',u'타율']
        frame=html.select('table#xtable1 tbody:nth-of-type(2) tr')
        data=list()
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n')[2:]:
                tmp.append(dat)
            data.append(tmp)
        self.boxScore['home']['batRecord'] = pd.DataFrame(data=data,columns=columns)
        self.boxScore['home']['batRecord'].index=self.boxScore['home']['batRecord'].pop(u'선수명')

        #-------BEGIN self.situation-------#
        self.situation={'away':[],'home':[]}
        url=url.replace('BoxScore','Situation')
        data=urllib2.urlopen(url)
        html=BeautifulSoup(data)        
        
        for number in range(1,11):    
            self.situation['away'].append([{'player':element.text.split()[2],'act':' '.join(element.text.split()[3:])} for element in html.select(str.format('div#sms%02d table.tEx.Ex2 tbody:nth-of-type(1) td'%(number)))]) 
            self.situation['home'].append([{'player':element.text.split()[2],'act':' '.join(element.text.split()[3:])} for element in html.select(str.format('div#sms%02d table.tEx.Ex2 tbody:nth-of-type(2) td'%(number)))]) 

        #-------END self.situation-------#
        
        #-------BEGIN winTeam,loseTeam -------#
        if self.boxScore['away']['sum'] > self.boxScore['home']['sum']:
            self.boxScore['winTeam'] = self.boxScore['away']            
            self.situation['winTeam']=self.situation['away']
            self.boxScore['loseTeam'] = self.boxScore['home']
            self.situation['loseTeam'] = self.situation['home']
        else:
            self.boxScore['loseTeam']= self.boxScore['away']
            self.situation['loseTeam']= self.situation['away']                                                     
            self.boxScore['winTeam'] = self.boxScore['home']
            self.situation['winTeam'] = self.situation['home']
        #-------END winTeam,loseTeam-------#
        
        data = urllib2.urlopen('http://www.koreabaseball.com/TeamRank/TeamRank.aspx')
        html = BeautifulSoup(data)
        self.rank={}
        
        columns=[u'순위',u'팀명',u'승',u'패',u'무',u'승률',u'게임차',u'최근10경기',u'연속',u'홈',u'방문']
        frame=html.select('table:nth-of-type(1) tbody tr')
        
        data=list()
        for row in frame:
            tmp=list()
            for dat in row.text.strip().split('\n'):
                tmp.append(dat)
            data.append(tmp)
        self.rank = pd.DataFrame(data=data,columns=columns)
        self.rank.index=self.rank.pop(u'순위')

# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from selenium import webdriver
from SerialParserForDaumKBO import SerialParserForDaumKBO

import sys
import re
import urllib2
import os


# In[2]:

class Parser_DaumKBO:
    '''
    stadium : 경기장

    seasonStat : 선발투수 시즌성적
    ------- key list -------
    [away/home/winTeam/loseTeam][StarterPitcher] : 선발투수 이름
    [away/home/winTeam/loseTeam][StarterPitcherWinCount] : 선발투수 승수
    [away/home/winTeam/loseTeam][StarterPitcherLoseCount] : 선발투수 패수
    [away/home/winTeam/loseTeam][StarterPitcherERA] : 선발투수 평균자책
    [away/home/winTeam/loseTeam][StarterPitcherWHIP] : 이닝당 안타 볼넷 허용률

    vsStat : 선발투수 상대전적
    ------- key list -------
    [away/home/winTeam/loseTeam][StarterPitcher] : 선발투수 이름
    [away/home/winTeam/loseTeam][StarterPitcherWinCount] : 선발투수 승수
    [away/home/winTeam/loseTeam][StarterPitcherLoseCount] : 선발투수 패수
    [away/home/winTeam/loseTeam][StarterPitcherERA] : 선발투수 평균자책
    [away/home/winTeam/loseTeam][StarterPitcherWHIP] : 이닝당 안타 볼넷 허용률
    
    startingLineUp : 선발타자
    ------- key list -------
    [away/home/winTeam/loseTeam] : (포지션,이름,평균타율)

    keyPlayer : 키플레이어(타자)
    ------- key list -------
    [away/home/winTeam/loseTeam] : (포지션,이름,평균타율)
    
    criticalInning : 승부처 이닝
    ------- key list -------
    [away/home/winTeam/loseTeam] : [승부처 이닝]

    rank : 팀의 순위(변동)
    ------- key list -------
    [away/home/winTeam/loseTeam] : (순위,(1:상승/-1:하강/0:유지))

    win_lose : 팀의 전적
    ------- key list -------
    [away/home/winTeam/loseTeam] : (승,무,패)

    accumulation : 팀의 연승(패)
    ------- key list -------
    [away/home/winTeam/loseTeam] : (1:승/-1:패)

    batRecord : 타석기록
    ------- key list -------
    [away/home/winTeam/loseTeam][H] : 안타
    [away/home/winTeam/loseTeam][HR]: 홈런
    [away/home/winTeam/loseTeam][SB]: 도루
    [away/home/winTeam/loseTeam][BB]: 사사구
    [away/home/winTeam/loseTeam][SO]: 탈삼진
    [away/home/winTeam/loseTeam][E] :실책
    [away/home/winTeam/loseTeam][GDP] : 병살
    [away/home/winTeam/loseTeam][LOB] : 잔루

    '''
    def __init__(self,date,awayTeam):
        s=SerialParserForDaumKBO(date,awayTeam)
        serial=s.getSerial()
        url='http://m.sports.media.daum.net/m/sports/pack/3min/%s'%(serial)
        
#         window=nt
        if os.name=='nt':
            driver=webdriver.PhantomJS(executable_path='./phantomjs.exe')
#       ubuntu=posix
        else:
            driver=webdriver.PhantomJS(executable_path='./phantomjs')
        driver.get(url)
        
        data=driver.page_source
        html=BeautifulSoup(data)
        
#         if os.name=='nt':
#             os.system('taskkill /f /im phantomjs.exe')
#         driver.quit()
        
        self.stadium=html.select_one('span.location').text
        
        self.seasonStat={'away':{},'home':{}}
        self.seasonStat['away']['StarterPitcher']=html.select_one('div.pitcher_comm.pitcher_away strong.name').text
        self.seasonStat['away']['StarterPitcherWinCount']=int(html.select_one('div#season_stat ul.list_record li:nth-of-type(1) span.bg_graph.graph_away span').text)
        self.seasonStat['away']['StarterPitcherLoseCount']=int(html.select_one('div#season_stat ul.list_record li:nth-of-type(2) span.bg_graph.graph_away span').text)
        self.seasonStat['away']['StarterPitcherERA']=float(html.select_one('div#season_stat ul.list_record li:nth-of-type(3) span.bg_graph.graph_away span').text)
        self.seasonStat['away']['StarterPitcherWHIP']=float(html.select_one('div#season_stat ul.list_record li:nth-of-type(4) span.bg_graph.graph_away span').text)
        self.seasonStat['home']['StarterPitcher']=html.select_one('div.pitcher_comm.pitcher_home strong.name').text
        self.seasonStat['home']['StarterPitcherWinCount']=int(html.select_one('div#season_stat ul.list_record li:nth-of-type(1) span.bg_graph.graph_home span').text)
        self.seasonStat['home']['StarterPitcherLoseCount']=int(html.select_one('div#season_stat ul.list_record li:nth-of-type(2) span.bg_graph.graph_home span').text)
        self.seasonStat['home']['StarterPitcherERA']=float(html.select_one('div#season_stat ul.list_record li:nth-of-type(3) span.bg_graph.graph_home span').text)
        self.seasonStat['home']['StarterPitcherWHIP']=float(html.select_one('div#season_stat ul.list_record li:nth-of-type(4) span.bg_graph.graph_home span').text)
        
        self.vsStat={'away':{},'home':{}}
        self.vsStat['away']['StarterPitcher']=html.select_one('div.pitcher_comm.pitcher_away strong.name').text
        self.vsStat['away']['StarterPitcherWinCount']=int(html.select_one('div#season_stat ul.list_record li:nth-of-type(1) span.bg_graph.graph_away span').text)
        self.vsStat['away']['StarterPitcherLoseCount']=int(html.select_one('div#season_stat ul.list_record li:nth-of-type(2) span.bg_graph.graph_away span').text)
        self.vsStat['away']['StarterPitcherERA']=float(html.select_one('div#season_stat ul.list_record li:nth-of-type(3) span.bg_graph.graph_away span').text)
        self.vsStat['away']['StarterPitcherWHIP']=float(html.select_one('div#season_stat ul.list_record li:nth-of-type(4) span.bg_graph.graph_away span').text)
        self.vsStat['home']['StarterPitcher']=html.select_one('div.pitcher_comm.pitcher_home strong.name').text
        self.vsStat['home']['StarterPitcherWinCount']=int(html.select_one('div#season_stat ul.list_record li:nth-of-type(1) span.bg_graph.graph_home span').text)        
        self.vsStat['home']['StarterPitcherLoseCount']=int(html.select_one('div#season_stat ul.list_record li:nth-of-type(2) span.bg_graph.graph_home span').text)
        self.vsStat['home']['StarterPitcherERA']=float(html.select_one('div#season_stat ul.list_record li:nth-of-type(3) span.bg_graph.graph_home span').text)
        self.vsStat['home']['StarterPitcherWHIP']=float(html.select_one('div#season_stat ul.list_record li:nth-of-type(4) span.bg_graph.graph_home span').text)
        
#         ---------------------------------------------------------------------------------------------------------------------------------------------------------------
#         lineup부분을 새로 가져와야함
        url='http://m.sports.media.daum.net/m/sports/pack/3min/%s?lineup'%(serial)
#         window=nt
#         if os.name=='nt':
#             driver=webdriver.PhantomJS(executable_path='./phantomjs.exe')
# #       ubuntu=posix
#         else:
#             driver=webdriver.PhantomJS(executable_path='./phantomjs')
        driver.get(url)
        data=driver.page_source
        html=BeautifulSoup(data)
        # Window에서는 PhantomJS프로세스가 남아있으므로 강제종료\n",
#         if os.name=='nt':
#             os.system('taskkill /f /im phantomjs.exe')
#         driver.quit()
#         ---------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.startingLineUp={}
        for line in html.select('div.wrap tbody tr'):
            self.startingLineUp['away']=(line.select_one('td:nth-of-type(1)').text,line.select_one('td:nth-of-type(2)').text,float(re.findall('[\.\d]+',line.select_one('td:nth-of-type(3)').text)[0]))
            self.startingLineUp['home']=(line.select_one('td:nth-of-type(4)').text,line.select_one('td:nth-of-type(5)').text,float(re.findall('[\.\d]+',line.select_one('td:nth-of-type(6)').text)[0]))
                     
        self.keyPlayer={'away':(),'home':()}
        try:
            keyPlayerParentNode=html.select_one('td.position.away.key-player').parent
            self.keyPlayer['away']=(keyPlayerParentNode.select_one('td:nth-of-type(1)').text,keyPlayerParentNode.select_one('td:nth-of-type(2)').text,float(re.findall('[\.\d]+',keyPlayerParentNode.select_one('td:nth-of-type(3)').text)[0]))
        except AttributeError:
            self.keyPlayer['away']=()
            sys.stderr.write('td.position.away.key-player == None\n')
        try:
            keyPlayerParentNode=html.select_one('td.position.home.key-player').parent
            self.keyPlayer['home']=(keyPlayerParentNode.select_one('td:nth-of-type(4)').text,keyPlayerParentNode.select_one('td:nth-of-type(5)').text,float(re.findall('[\.\d]+',keyPlayerParentNode.select_one('td:nth-of-type(6)').text)[0]))
        except AttributeError:
            self.keyPlayer['home']=()
            sys.stderr.write('td.position.home.key-player == None\n')
        
        self.criticalInning={'away':[],'home':[]}
        self.criticalInningVOD_Url=[]
        try:
            for x in html.select('table.tbl_score strong.img_highlight.ico_decisive'):
                node=x.parent.parent.parent
                if node.attrs['data-half']=='first':
                    self.criticalInning['away'].append(int(node.attrs['data-inning']))
                else:
                    self.criticalInning['home'].append(int(node.attrs['data-inning']))
                    
            for x in html.select('table.tbl_score strong.img_highlight.ico_decisive'):        
                node=x.parent.parent.parent
                vod_id=node.select_one('a.link_vod').attrs['data-id']
                url='http://m.sports.media.daum.net/m/sports/pack/3min/%s?%s'%(serial,vod_id)
                driver.get(url)
                data=driver.page_source
                html=BeautifulSoup(data)
                url=html.select_one('div.highlight_video iframe').attrs['src']
                self.criticalInningVOD_Url.append(url)
            
        except TypeError:
            sys.stderr.write('html.select(\'table.tbl_score strong.img_highlight.ico_decisive\') == None\n')
        
               
#         ---------------------------------------------------------------------------------------------------------------------------------------------------------------
#         result부분을 새로 가져와야함
        url='http://m.sports.media.daum.net/m/sports/pack/3min/%s?result'%(serial)
#         window=nt
#         if os.name=='nt':
#             driver=webdriver.PhantomJS(executable_path='./phantomjs.exe')
# #       ubuntu=posix
#         else:
#             driver=webdriver.PhantomJS(executable_path='./phantomjs')
        driver.get(url)
        data=driver.page_source
        html=BeautifulSoup(data)
        # Window에서는 PhantomJS프로세스가 남아있으므로 강제종료\n",
#         if os.name=='nt':
#             os.system('taskkill /f /im phantomjs.exe')
#         driver.quit()
#         ---------------------------------------------------------------------------------------------------------------------------------------------------------------
                
        self.rank={}
        sen=html.select_one('div.recent_stats div.away p.change').text
#      ex)   순위 9위 (-)
        rankNumber=int(sen.split()[1][:-1])
#      순위상승
        if u'▲' in sen:
            self.rank['away']=(rankNumber,int(sen[sen.find(u'▲')+1:sen.find(')')]))
#      순위하강
        elif u'▽' in sen:
            self.rank['away']=(rankNumber,-1*int(sen[sen.find(u'▽')+1:sen.find(')')]))
#      순위유지
        else:
            self.rank['away']=(rankNumber,0)
        sen=html.select_one('div.recent_stats div.home p.change').text
#      ex)   순위 9위 (-)
        rankNumber=int(sen.split()[1][:-1])
#      순위상승(u'▲'==u'\u25b2')
        if u'▲' in sen:
            self.rank['home']=(rankNumber,int(sen[sen.find(u'▲')+1:sen.find(')')]))
#      순위하강(u'▽'==u'\u25bd')
        elif u'▽' in sen:
            self.rank['home']=(rankNumber,-1*int(sen[sen.find(u'▽')+1:sen.find(')')]))
#      순위유지
        else:
            self.rank['home']=(rankNumber,0)
        
        self.win_lose={}
        sen=html.select_one('div.recent_stats div.away p.win-lose').text
        self.win_lose['away']=tuple(map(int,re.findall('[\d]+',sen)))
        sen=html.select_one('div.recent_stats div.home p.win-lose').text
        self.win_lose['home']=tuple(map(int,re.findall('[\d]+',sen)))
        
        self.accumulation={}
        sen=html.select_one('div.recent_stats div.away p.accumulation').text
        self.accumulation['away']= int(re.findall('[\d]+',sen)[0]) if sen[-1]==u'승' else (-1)*int(re.findall('[\d]+',sen)[0])
        sen=html.select_one('div.recent_stats div.home p.accumulation').text
        self.accumulation['home']=int(re.findall('[\d]+',sen)[0]) if sen[-1]==u'승' else (-1)*int(re.findall('[\d]+',sen)[0])
        
        if int(html.select('td.run')[0].text) >= int(html.select('td.run')[1].text):
            winTeam='away'
            loseTeam='home'
        else:
            winTeam='home'
            loseTeam='away'
#         ---------------------------------------------------------------------------------------------------------------------------------------------------------------
#         stats부분을 새로 가져와야함
        url='http://m.sports.media.daum.net/m/sports/pack/3min/%s?stats'%(serial)
#         window=nt
#         if os.name=='nt':
#             driver=webdriver.PhantomJS(executable_path='./phantomjs.exe')
# #       ubuntu=posix
#         else:
#             driver=webdriver.PhantomJS(executable_path='./phantomjs')
        driver.get(url)
        data=driver.page_source
        html=BeautifulSoup(data)
        # Window에서는 PhantomJS프로세스가 남아있으므로 강제종료\n",
        if os.name=='nt':
            os.system('taskkill /f /im phantomjs.exe')
        driver.quit()
#         ---------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.batRecord={'away':{},'home':{}}
        tmpList=[]
    #     안타,홈런,도루,사사구,탈삼진,실책,병살,잔루
        keyList=['H','HR','SB','BB','SO','E','GDP','LOB']
        for element in html.select('li#page-stats div.vs_graph ul.list_record'):
            tmpList.extend(tuple(map(int,re.findall('[\d]+',element.text))))
        for k in enumerate(keyList):
    #     짝수 인덱스
            if k[0]%2==0 :
                self.batRecord['home'][k[1]]= tmpList[k[0]]
            else:
                self.batRecord['away'][k[1]]=tmpList[k[0]]

        if winTeam=='away':
            self.seasonStat['winTeam']=self.seasonStat['away']
            self.vsStat['winTeam']=self.vsStat['away']
            self.startingLineUp['winTeam']=self.startingLineUp['away']
            self.keyPlayer['winTeam']=self.keyPlayer['away']
            self.rank['winTeam']=self.rank['away']
            self.criticalInning['winTeam']=self.criticalInning['away']
            self.rank['winTeam']=self.rank['away']
            self.accumulation['winTeam']=self.accumulation['away']
            self.batRecord['winTeam']=self.batRecord['away']
            self.win_lose['winTeam']=self.win_lose['away']
            
            self.seasonStat['loseTeam']=self.seasonStat['home']
            self.vsStat['loseTeam']=self.vsStat['home']
            self.startingLineUp['loseTeam']=self.startingLineUp['home']
            self.keyPlayer['loseTeam']=self.keyPlayer['home']
            self.rank['loseTeam']=self.rank['home']
            self.criticalInning['loseTeam']=self.criticalInning['home']
            self.rank['loseTeam']=self.rank['home']
            self.accumulation['loseTeam']=self.accumulation['home']
            self.batRecord['loseTeam']=self.batRecord['home']
            self.win_lose['loseTeam']=self.win_lose['home']
            
        else :
            self.seasonStat['winTeam']=self.seasonStat['home']
            self.vsStat['winTeam']=self.vsStat['home']
            self.startingLineUp['winTeam']=self.startingLineUp['home']
            self.keyPlayer['winTeam']=self.keyPlayer['home']
            self.rank['winTeam']=self.rank['home']
            self.criticalInning['winTeam']=self.criticalInning['home']
            self.rank['winTeam']=self.rank['home']
            self.accumulation['winTeam']=self.accumulation['home']
            self.batRecord['winTeam']=self.batRecord['home']
            self.win_lose['winTeam']=self.win_lose['home']
            
            self.seasonStat['loseTeam']=self.seasonStat['away']
            self.vsStat['loseTeam']=self.vsStat['away']
            self.startingLineUp['loseTeam']=self.startingLineUp['away']
            self.keyPlayer['loseTeam']=self.keyPlayer['away']
            self.rank['loseTeam']=self.rank['away']
            self.criticalInning['loseTeam']=self.criticalInning['away']
            self.rank['loseTeam']=self.rank['away']
            self.accumulation['loseTeam']=self.accumulation['away']
            self.batRecord['loseTeam']=self.batRecord['away']
            self.win_lose['loseTeam']=self.win_lose['away']


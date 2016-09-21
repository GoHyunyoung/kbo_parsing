
# coding: utf-8

# In[61]:


# pip install selenium
# pip install bs4
from UrlParserForKBO import UrlParserForKBO
from Parser_DaumKBO import Parser_DaumKBO
from Parser_KBO import Parser_KBO
from sklearn import tree
from sklearn.externals.six import StringIO

from String_checker import String_checker
from TransformeTeamName import TransformeTeamName

import pandas as pd
import numpy as np
# pip install MySQL-Python
import MySQLdb
import random
import datetime
import os
import sys
import copy


# In[62]:

contextSentence = [' ','승리하였다. ','접전끝에 승리를 하였다. ','역전에 성공했다. ','완승을 하였다. ','무승부로 끝이났다. ','영봉승을 하였다. ']


# In[63]:

def getPositionName(position):
    if position==u'P':
        return u'투수'
    elif position==u'C':
        return u'포수'
    elif position==u'1B':
        return u'1루수'
    elif position==u'2B':
        return u'2루수'
    elif position==u'3B':
        return u'3루수'
    elif position==u'1B':
        return u'1루수'
    elif position==u'SS':
        return u'유격수'
    elif position==u'LF':
        return u'좌익수'
    elif position==u'CF':
        return u'중견수'
    elif position==u'RF':
        return u'우익수'
    elif position==u'DH':
        return u'지명타자'
    elif position==u'H':
        return u'대타'
    else:
        return u'대주자'


# In[64]:

def changeWithParam(sentence, *wordBox):
    '''
    Change '()'(bracket) to element of wordBox(List) in Random.
    return type : String
    '''
    for element in wordBox:
#         print element
        word=element[random.randint(0,len(element)-1)]
        sentence=sentence.replace(u'()',word,1)
    return sentence


# In[65]:

def getClassifier(Parser_KBO,Parser_DaumKBO):
    # DecisionTree - 서두
    path_Intro = './DecisionLearning//DecisionTree_sample.csv'
    df_Intro = pd.read_csv(path_Intro,index_col=None,header=None,names=['1H','2H','3H','4H','5H','6H','7H','8H','9H','10H','11H','12H','sum','context'])
    score_Intro = np.array(df_Intro.reindex(columns=['1H','2H','3H','4H','5H','6H','7H','8H','9H','10H','11H','12H','sum']))
    context_Intro = np.array(df_Intro.get('context'))
    clf_Intro = tree.DecisionTreeClassifier(criterion='entropy')
    clf_Intro = clf_Intro.fit(score_Intro,context_Intro)
    return clf_Intro.predict([x-y for x,y in zip(Parser_KBO.boxScore['home']['score'][:13],Parser_KBO.boxScore['away']['score'][:13])])[0]


# In[66]:

def writeDate(Parser_KBO):    
    return Parser_KBO.boxScore['date']


# In[67]:

def writeHead(Parser_KBO,Parser_DaumKBO,contextClassifier):
#     문장뭉치
    sentenceGroup=[
        'at ascore vs ht hscore'
    ]
    
#     문장뽑기
    sentence=sentenceGroup[random.randint(0,len(sentenceGroup)-1)]
    
#     문장만들기
    sentence=sentence.replace('at',Parser_KBO.boxScore['away']['name'])
    sentence=sentence.replace('ht',Parser_KBO.boxScore['home']['name'])
    sentence=sentence.replace('hscore',str(Parser_KBO.boxScore['home']['sum']))
    sentence=sentence.replace('ascore',str(Parser_KBO.boxScore['away']['sum']))
    
    return sentence


# In[98]:

def writeIntro(Parser_KBO,Parser_DaumKBO,contextClassifier):
#     문장뭉치
    sentence1Group=[
        changeWithParam(u'winTeam_name는 date stadium에서 () loseTeam_name와의 ()에서 winTeam_sum-loseTeam_sum 으로 context',
                        [u'열린',u'열렸던',u'치뤄진'],
                        [u'승부',u'경기',u'대결']
                       ),
        changeWithParam(u'date stadium에서 () away_name와 home_name와의 ()에서 away_sum-home_sum으로 winTeam_name이 context',
                        [u'열린',u'열렸던',u'치뤄진'],
                        [u'승부',u'경기',u'대결']
                       ),
        changeWithParam(u'away_name와 home_name의 () date stadium에서 있었던 오늘 away_name는 away_sum, home_name는 home_sum로 winTeam_name가 경기에서 context',
                        [u'승부가',u'경기가',u'대결이']
                       ),
        changeWithParam(u'date stadium에서 있었던 away_name와 home_name과의 (), winTeam_name이 winTeam_sum loseTeam_name이 loseTeam_sum로 winTeam_name이 context',
                        [u'승부',u'경기',u'대결']
                       ),
        changeWithParam(u'홈팀 home_name과 어웨이팀 away_name () 오늘 date 펼쳐졌다. stadium경기장에서 () 이 경기에서 winTeam_name이 winTeam_sum : loseTeam_sum으로 loseTeam_name을 context',
                        [u'승부가',u'경기가',u'대결이'],
                        [u'열린',u'열렸던',u'치뤄진']
                       )
        ]
    
    #     선발투수 == 승리투수인 경우
    if Parser_DaumKBO.winlosePitcher['winTeam']['name']==Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']:
        #     6이닝 이상 && 3실점이하 -> 퀄리티 스타트
        if int(Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'이닝'].split()[0]) >= 6 and int(Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'실점']) <=3:
            sentence2Group=[
                changeWithParam(u' winTeam_name 선발투수로 나온 winTeam_StarterPitcher선수가 INN이닝동안 NP개를 던지고 H피안타 BB볼넷 SO탈삼진 R실점의 ()를 () () () winlosePitcher_winTeam_winCount번째 승리(winlosePitcher_winTeam_loseCount패)를 ()',
                                [u'역투',u'호투',u'투구'] if Parser_DaumKBO.seasonStat['winTeam']['StarterPitcherWinCount']>5 else [u'완벽투구'], 
                                [u'펼치며',u'던지며'],
                                [u'퀄리티 스타트(QS)를 하였다.',u'퀄리티 스타트를 했다.',u'퀄리티 스타트를 기록하였다.',u'Quality Start를 기록했다.'],
                                [u'이로써',u'그 결과, ',u'이로인해'],
                                [u'챙겼다.',u'거두었다.',u'가져갔다.']
                ) 
            ]
        elif int(Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'이닝'].split()[0]) >= 4:
            sentence2Group=[
                changeWithParam(u' winTeam_name 선발투수로 나온 winTeam_StarterPitcher선수가 INN이닝동안 NP개를 던지고 H피안타 BB볼넷 SO탈삼진 R실점의 ()를 () () () winlosePitcher_winTeam_winCount번째 승리(winlosePitcher_winTeam_loseCount패)를 ()',
                                [u'역투',u'호투',u'투구'] if Parser_DaumKBO.seasonStat['winTeam']['StarterPitcherWinCount']>5 else [u'완벽투구'], 
                                [u'펼치며',u'던지며'],
                                [u'승리를 리드하며 승리투수의 자리에 앉았다.',u'승리를 이끌었다.',u'승리투수로써 팀의 승리를 주도했다.'] if Parser_DaumKBO.seasonStat['winTeam']['StarterPitcherWinCount']>5 else [u'승리에 기여했다.',u'경기를 해나갔다.'],
                                [u'이로써',u'그 결과, ',u'이로인해'],
                                [u'챙겼다. ',u'거두었다. ',u'가져갔다. ']
                ) 
            ]
        else:
            sentence2Group=[
                changeWithParam(u' winTeam_name 선발투수로 나온 winTeam_StarterPitcher선수가 INN이닝동안 NP개를 던지고 H피안타 BB볼넷 SO탈삼진 R실점()',
                                [u'을 기록하고 마운드를 내려올수 밖에 없었다. ',u'을 끝으로 마운드를 물러났다. ',u'로 선발투수의 역할을 제대로 하지 못하였다. ',u'하며 팀의 불펜투수들에게 부담을 주었다. 'u'기록하며 팀의 불펜진에 火을 질렀다. ']
               )
            ]
            
    else:
        #         퀄리티 스타트의 경우
        if int(Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'이닝'].split()[0]) >= 6 and int(Parser_KBO.boxScore['winTeam']['pitRecord'].ix[parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'실점']) <=3:
            sentence2Group=[
                changeWithParam(u' winTeam_name의 winTeam_StarterPitcher선수가 INN이닝동안 NP개를 던지고 H피안타 BB볼넷 SO탈삼진 R실점의 ()를 () () () winlosePitcher_winTeam_winCount번째 승리(winlosePitcher_winTeam_loseCount패)를 ()',
                                [u'역투',u'호투',u'투구'] if Parser_DaumKBO.seasonStat['winTeam']['StarterPitcherWinCount']>5 else [u'완벽투구'], 
                                [u'펼치며',u'던지며'],
                                [u'퀄리티 스타트(QS)를 하였다.'],
                                [u'이로써',u'그 결과, ',u'이로인해'],
                                [u'챙겼다. ',u'거두었다. ',u'가져갔다. ']
                ) 
            ]
        else :
            sentence2Group=[
                changeWithParam(u' winTeam_name에서 승리투수로 활약한 winlosePitcher_winTeam_name선수가 INN이닝동안 NP개를 던지고 H피안타 BB볼넷 SO탈삼진 R실점의 ()를 () () () winlosePitcher_winTeam_winCount번째 승리(winlosePitcher_winTeam_loseCount패)를 ()',
                            [u'역투',u'호투',u'투구'],
                            [u'펼치며',u'던지며'],
                            [u'승리를 리드했다.',u'승리를 이끌었다.',u'팀의 승리를 주도했다.'],
                            [u'이로써',u'그 결과,',u'이로인해'],
                            [u'챙겼다. ',u'거두었다. ',u'가져갔다. ']
                           )
            ]    
    
    essentialSentence=u''
    #   선발투수 != 승리투수인 경우
    
    #     세이브투수가 있는경우
    if u'세' in Parser_KBO.boxScore['winTeam']['pitRecord'][u'결과'].values:
        if int(Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_KBO.boxScore['winTeam']['pitRecord'][u'결과']==u'세'][u'삼진'])>0:
            essentialSentence+=u'세이브 투수 winTeam_pitRecord_savePitcher_name선수가 winTeam_pitRecord_savePitcher_INN이닝에 등판해, winTeam_pitRecord_savePitcher_K탈삼진, winTeam_pitRecord_savePitcher_R실점으로 시즌 winTeam_pitRecord_savePitcher_saveCount번째 세이브를 챙겼다.' if int(Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_KBO.boxScore['winTeam']['pitRecord'][u'결과']==u'세'][u'자책'])!=0 else u'세이브 투수 winTeam_pitRecord_savePitcher_name가 winTeam_pitRecord_savePitcher_INN이닝, winTeam_pitRecord_savePitcher_R실점으로 시즌 winTeam_pitRecord_savePitcher_saveCount번째 세이브를 챙기며, 평균자책점을 winTeam_pitRecord_savePitcher_avgERA으로 낮췄다.'
        
    #          패배투수에 관한 기사
    #     패배팀의 선발투수 == 패배투수
    losePitcherName=Parser_DaumKBO.winlosePitcher['loseTeam']['name']
    if Parser_DaumKBO.winlosePitcher['loseTeam']['name']==Parser_DaumKBO.seasonStat['loseTeam']['StarterPitcher']:    
        essentialSentence+=changeWithParam(u'loseTeam_name의 선발 winlosePitcher_loseTeam_name선수는 INN이닝 H피안타 BB볼넷 SO탈삼진 R실점(E자책) ()',
                                          [u'을 하며 1패를 추가했다.',u'을 기록하며 무너졌다.',u'으로 패배를 기록하며 winTeam_name 승리의 재물이 되었다.'])
    
    
#     문장뽑기
    sentence1=sentence1Group[random.randint(0,len(sentence1Group)-1)]
    sentence2=sentence2Group[random.randint(0,len(sentence2Group)-1)]

#     문장만들기

    #------- BEGIN Intro1-------#
    sentence1=sentence1.replace('winTeam_name',Parser_KBO.boxScore['winTeam']['name'])
    sentence1=sentence1.replace('loseTeam_name',Parser_KBO.boxScore['loseTeam']['name'])
    sentence1=sentence1.replace('winTeam_sum',str(Parser_KBO.boxScore['winTeam']['sum']))
    sentence1=sentence1.replace('loseTeam_sum',str(Parser_KBO.boxScore['loseTeam']['sum']))
    sentence1=sentence1.replace('home_sum',str(Parser_KBO.boxScore['home']['sum']))
    sentence1=sentence1.replace('away_sum',str(Parser_KBO.boxScore['away']['sum']))
    sentence1=sentence1.replace('stadium',Parser_DaumKBO.stadium)
    sentence1=sentence1.replace('date',str(int(Parser_KBO.boxScore['date'][4:6]))+u'월'+str(int(Parser_KBO.boxScore['date'][6:8]))+u'일'+Parser_KBO.boxScore['date'][8:])
    sentence1=sentence1.replace('home_name',Parser_KBO.boxScore['home']['name'])
    sentence1=sentence1.replace('away_name',Parser_KBO.boxScore['away']['name'])    
    
    # Intro1 예외처리
    #'context' -> 무승부
    if Parser_KBO.boxScore['home']['sum']==Parser_KBO.boxScore['away']['sum']:
        sentence1=sentence1.replace('context',contextSentence[5].decode('utf-8'))    
    #'context' -> 영봉승
    elif Parser_KBO.boxScore['home']['sum']==0 or Parser_KBO.boxScore['away']['sum']==0:
        sentence1=sentence1.replace('context',contextSentence[6].decode('utf-8'))    
    #'context'-> 나머지의 경우
    else:
        sentence1=sentence1.replace('context',contextSentence[contextClassifier].decode('utf-8'))
    #------- END Intro1-------#

    #------- BEGIN Intro2-------#
    sentence2=sentence2.replace('winlosePitcher_winTeam_name',Parser_DaumKBO.winlosePitcher['winTeam']['name'])
    sentence2=sentence2.replace('winlosePitcher_winTeam_winCount',str(Parser_DaumKBO.winlosePitcher['winTeam']['winCount']))
    sentence2=sentence2.replace('winlosePitcher_winTeam_loseCount',str(Parser_DaumKBO.winlosePitcher['winTeam']['loseCount']))
    sentence2=sentence2.replace('winTeam_name',Parser_KBO.boxScore['winTeam']['name'])
    sentence2=sentence2.replace('winTeam_StarterPitcher',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']].name)
    sentence2=sentence2.replace('ERA',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'평균자책점'])
    sentence2=sentence2.replace('INN',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'이닝'])
    sentence2=sentence2.replace('BB',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'4사구'])
    sentence2=sentence2.replace('BN',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'타자'])
    sentence2=sentence2.replace('NP',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'투구수'])
    sentence2=sentence2.replace('SO',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'삼진'])            
    sentence2=sentence2.replace('ER',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'자책'])
    sentence2=sentence2.replace('R',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'실점'])
    sentence2=sentence2.replace('H',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_DaumKBO.seasonStat['winTeam']['StarterPitcher']][u'피안타'])
    #------- END Intro2-------#
    
    #------- BEGIN ESSESNTIAL-------#
    if u'세' in Parser_KBO.boxScore['winTeam']['pitRecord'][u'결과'].values:
        essentialSentence=essentialSentence.replace('winTeam_pitRecord_savePitcher_name',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_KBO.boxScore['winTeam']['pitRecord'][u'결과']==u'세'].index[0])
        essentialSentence=essentialSentence.replace('winTeam_pitRecord_savePitcher_INN',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_KBO.boxScore['winTeam']['pitRecord'][u'결과']==u'세'][u'이닝'][0])
        essentialSentence=essentialSentence.replace('winTeam_pitRecord_savePitcher_K',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_KBO.boxScore['winTeam']['pitRecord'][u'결과']==u'세'][u'삼진'][0])
        essentialSentence=essentialSentence.replace('winTeam_pitRecord_savePitcher_R',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_KBO.boxScore['winTeam']['pitRecord'][u'결과']==u'세'][u'실점'][0])
        essentialSentence=essentialSentence.replace('winTeam_pitRecord_savePitcher_saveCount',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_KBO.boxScore['winTeam']['pitRecord'][u'결과']==u'세'][u'세'][0])
        essentialSentence=essentialSentence.replace('winTeam_pitRecord_savePitcher_avgERA',Parser_KBO.boxScore['winTeam']['pitRecord'].ix[Parser_KBO.boxScore['winTeam']['pitRecord'][u'결과']==u'세'][u'평균자책점'][0])
    essentialSentence=essentialSentence.replace('winlosePitcher_loseTeam_name',Parser_DaumKBO.winlosePitcher['loseTeam']['name'])
    essentialSentence=essentialSentence.replace('winTeam_name',Parser_KBO.boxScore['winTeam']['name'])
    essentialSentence=essentialSentence.replace('loseTeam_name',Parser_KBO.boxScore['loseTeam']['name'])
    essentialSentence=essentialSentence.replace('ERA',Parser_KBO.boxScore['loseTeam']['pitRecord'].ix[Parser_DaumKBO.winlosePitcher['loseTeam']['name']][u'평균자책점'])
    essentialSentence=essentialSentence.replace('INN',Parser_KBO.boxScore['loseTeam']['pitRecord'].ix[Parser_DaumKBO.winlosePitcher['loseTeam']['name']][u'이닝'])
    essentialSentence=essentialSentence.replace('BB',Parser_KBO.boxScore['loseTeam']['pitRecord'].ix[Parser_DaumKBO.winlosePitcher['loseTeam']['name']][u'4사구'])
    essentialSentence=essentialSentence.replace('BN',Parser_KBO.boxScore['loseTeam']['pitRecord'].ix[Parser_DaumKBO.winlosePitcher['loseTeam']['name']][u'타자'])
    essentialSentence=essentialSentence.replace('NP',Parser_KBO.boxScore['loseTeam']['pitRecord'].ix[Parser_DaumKBO.winlosePitcher['loseTeam']['name']][u'투구수'])
    essentialSentence=essentialSentence.replace('SO',Parser_KBO.boxScore['loseTeam']['pitRecord'].ix[Parser_DaumKBO.winlosePitcher['loseTeam']['name']][u'삼진'])            
    essentialSentence=essentialSentence.replace('ER',Parser_KBO.boxScore['loseTeam']['pitRecord'].ix[Parser_DaumKBO.winlosePitcher['loseTeam']['name']][u'자책'])
    essentialSentence=essentialSentence.replace('R',Parser_KBO.boxScore['loseTeam']['pitRecord'].ix[Parser_DaumKBO.winlosePitcher['loseTeam']['name']][u'실점'])
    essentialSentence=essentialSentence.replace('H',Parser_KBO.boxScore['loseTeam']['pitRecord'].ix[Parser_DaumKBO.winlosePitcher['loseTeam']['name']][u'피안타'])
    essentialSentence=essentialSentence.replace('E',Parser_KBO.boxScore['loseTeam']['pitRecord'].ix[Parser_DaumKBO.winlosePitcher['loseTeam']['name']][u'자책'])
    #------- END ESSESNTIAL-------#

    return sentence1+sentence2+essentialSentence


# In[94]:

def writeEnd(Parser_KBO,Parser_DaumKBO):
    
    teamrank = parser_KBO.rank
    gab = []
    gameN = []
    upper=u''
    down=u''
    tmp=0
    add=u''

    winTeamName = parser_KBO.boxScore['winTeam']['name']
    awayTeamName = parser_KBO.boxScore['home']['name']
    teamPointer = int(parser_KBO.rank.loc[parser_KBO.rank[u'팀명']==winTeamName].index[0])-1
    prevIndex = teamrank.index
    l=len(teamrank)
    teamrank.index=np.array(range(l))

    for i in teamrank.index:    
        gab.append(teamrank.loc[i,u'게임차'])
#         print teamrank
        gameN.append(int(teamrank.loc[i,u'승']) + int(teamrank.loc[i,u'패']) + int(teamrank.loc[i,u'무']))

    for i in range(0,9):
        upper = teamrank.loc[i,u'팀명']
        down = teamrank.loc[i+1,u'팀명']
        if((float(gab[i+1]) - float(gab[i])) <= 1 and gameN[i] < 144 and gameN[i+1] < 144):
            tmp=(float(gab[i+1]) - float(gab[i]))
            if(upper == winTeamName or down == winTeamName ):
                add+=u' 내일 경기결과에 따라 순위 변동의 가능성이 보인다.'
                break
                
        elif((float(gab[i+1]) - float(gab[i])) <= 3 and gameN[i]+6 < 144 and gameN[i+1]+6 < 144):
            upper = teamrank.loc[i,u'팀명']
            down = teamrank.loc[i+1,u'팀명']
            tmp=(float(gab[i+1]) - float(gab[i]))
            if(upper == winTeamName or down == winTeamName):
                add+= u' 앞으로의 경기가 중요하게 되었다.'
                break

        if(float(gab[teamPointer]) - float(gab[4]) < 144 - gameN[teamPointer] and teamPointer > 4):
            add+=changeWithParam(u' winTeam은 () () gap경기를 ()',
                                       [u' 가을야구로',u'포스트 시즌으로'],
                                       [u' 진출하기 위해서는', u'출전하기 위해서는'],
                                       [u' 따내야 한다.',u'잡아야 한다.',u'승리해야 한다.']
                                      )
            break
            
            
    teamrank.index=prevIndex     
            
            
    sentence5=changeWithParam(u' upperTeam와 downTeam은 ()',
                              [u' gabOfGame게임 차이가 되었다.',u' gabOfGame게임 차이로 좁혀졌다.',u' gabOfGame게임차로 줄어들었다.'] if tmp!=0 else [u'승차가 타이를 이루게 되었다.'])
    sentence5+=add
    sentence5=sentence5.replace('winTeam',Parser_KBO.boxScore['winTeam']['name'])        
    sentence5=sentence5.replace('upperTeam',upper)
    sentence5=sentence5.replace('downTeam',down)
    sentence5=sentence5.replace('gabOfGame',str(tmp))
    sentence5=sentence5.replace('gap',str(float(gab[teamPointer]) - float(gab[4])))
    
    return sentence5


# In[70]:

# 결론작성
def writeConc(Parser_KBO,Parser_DaumKBO,contextClassifier):
#     문장뭉치
    sentence1Group=[
    changeWithParam(u' () winTeam_name은 winTeam_win_lose_winCount승 winTeam_win_lose_drawCount무 winTeam_win_lose_loseCount패를 기록하게 되었다.',
                    [u'이날의 승리로',u'오늘의 승리로',u'이로인해',u'오늘 열렸던 경기로',u'오늘 치뤄진 경기로']),
#     changeWithParam(u' () () away_name은 away_win_lose_winCount승 away_win_lose_drawCount무 away_win_lose_loseCount패, home_name은 home_win_lose_winCount승 home_win_lose_drawCount무 home_win_lose_loseCount패를 기록하게 되었다.',
#                     [u'이날의',u'오늘의',u'오늘 있었던',u'오늘 열렸던',u'오늘 치뤄진'],
#                     [u'경기로',u'승부로',u'대결로'])
    ]
    
    sentence2Group=[
    changeWithParam(u' () loseTeam_name은 loseTeam_win_lose_winCount승 loseTeam_win_lose_drawCount무 loseTeam_win_lose_loseCount패를 기록하게 되었다.',
#                     1:승리/2:접전/3:역전/4:완승 각 경우에 대한 다른 문장
                    [u'패배의 아픔을 맛본',u'패배한'] if contextClassifier==1 else 
                    [u'아쉽게 패배한',u'안타깝게 패배한',u'접전끝에 패배한'] if contextClassifier==2 else
                    [u'역전을 당한',u'역전을 허용한'] if contextClassifier==3 else
                    [u'완패한',u'큰 점수차로 패배한']
    )]
    
    print Parser_KBO.rank
    
#     순위 변동,연승의 내용은 필수
    essentialSentence=''
    #      순위가 올라간경우
    if parser_DaumKBO.rank['winTeam'][1]>0:
        rankNum=Parser_KBO.rank.loc[Parser_KBO.rank[u'팀명'] == Parser_KBO.boxScore['winTeam']['name']]
        prevIndex = rankNum.index
        l=len(rankNum)
        rankNum.index=np.array(range(l))
        nextTeam=Parser_KBO.rank.ix[str(int(rankNum.index[0])+1)][u'팀명']
        essentialSentence+=changeWithParam(u' winTeam_name은 리그winTeam_rank+1위에서 () winTeam_rank위로 nextTeam을 ()  ()',
                                           [u'1순위 올라가',u'한 순위 올라간'],
                                           [u'밟고',u'밀치고 올라가'],
                                           [u'한순위 더 높이 안착하게 되었다.',u'팀의 순위가 상승하였다.']
                                          )
        rankNum.index=prevIndex
    
    #      순위가 내려간 경우
    if parser_DaumKBO.rank['loseTeam'][1]<0:
        essentialSentence+=changeWithParam(u' 한편, loseTeam_name은 리그 loseTeam_rank-1위에서 () loseTeam_rank위로 ()',
                                           [u'1순위 내려가',u'한 순위 내려간'],
                                           [u'안착하게 되었다.',u'팀의 순위가 하락하였다.']
                                          )
        
    #     연승을 하게된 경우
    if parser_DaumKBO.accumulation['winTeam'] > 1:
        essentialSentence+=changeWithParam(u' () winTeam_name은 () () ()',
                                           [u'또한'],
                                           [u'이번 경기로',u'이번 승리로',u'오늘의 경기로'],
                                           [u'winTeam_accumulation연승을',u'연속 winTeam_accumulation승을'],
                                           [u'달려나가고 있다.',u'행진하고 있다.',u'이루고 있다.']
                                          )
    #     연패를 하게된 경우
    if parser_DaumKBO.accumulation['loseTeam'] < -1:
        essentialSentence+=changeWithParam(u' () loseTeam_name은 () loseTeam_accumulation연패를 ()',
                                           [u'하지만',u'안타깝게도'],
                                           [u'이번 패배로',u'오늘의 패배로'],
                                           [u'끊어내기 위한 연습이 필요할 것이다.',u'잘라내기위한 노력이 필요할 것이다.']
                                          )
        
    #     문장뽑기
    sentence1=sentence1Group[random.randint(0,len(sentence1Group)-1)]
    sentence2=sentence2Group[random.randint(0,len(sentence2Group)-1)]
    
    #     문장만들기
    sentence1=sentence1.replace('winTeam_name',Parser_KBO.boxScore['winTeam']['name'])
    sentence1=sentence1.replace('winTeam_win_lose_winCount',str(Parser_DaumKBO.win_lose['winTeam'][0]))
    sentence1=sentence1.replace('winTeam_win_lose_loseCount',str(Parser_DaumKBO.win_lose['winTeam'][2]))
    sentence1=sentence1.replace('winTeam_win_lose_drawCount',str(Parser_DaumKBO.win_lose['winTeam'][1]))
    sentence1=sentence1.replace('away_name',Parser_KBO.boxScore['away']['name'])
    sentence1=sentence1.replace('away_win_lose_winCount',str(Parser_DaumKBO.win_lose['away'][0]))
    sentence1=sentence1.replace('away_win_lose_loseCount',str(Parser_DaumKBO.win_lose['away'][2]))
    sentence1=sentence1.replace('away_win_lose_drawCount',str(Parser_DaumKBO.win_lose['away'][1]))
    sentence1=sentence1.replace('home_name',Parser_KBO.boxScore['home']['name'])
    sentence1=sentence1.replace('home_win_lose_winCount',str(Parser_DaumKBO.win_lose['home'][0]))
    sentence1=sentence1.replace('home_win_lose_loseCount',str(Parser_DaumKBO.win_lose['home'][2]))
    sentence1=sentence1.replace('home_win_lose_drawCount',str(Parser_DaumKBO.win_lose['home'][1]))
    
    sentence2=sentence2.replace('loseTeam_name',Parser_KBO.boxScore['loseTeam']['name'])
    sentence2=sentence2.replace('loseTeam_win_lose_winCount',str(Parser_DaumKBO.win_lose['loseTeam'][0]))
    sentence2=sentence2.replace('loseTeam_win_lose_loseCount',str(Parser_DaumKBO.win_lose['loseTeam'][2]))
    sentence2=sentence2.replace('loseTeam_win_lose_drawCount',str(Parser_DaumKBO.win_lose['loseTeam'][1]))
    
    essentialSentence=essentialSentence.replace('winlosePitcher_winTeam_winCount',str(Parser_DaumKBO.winlosePitcher['winTeam']['winCount']))
    essentialSentence=essentialSentence.replace('winlosePitcher_winTeam_loseCount',str(Parser_DaumKBO.winlosePitcher['winTeam']['loseCount']))
    essentialSentence=essentialSentence.replace('winTeam_name',Parser_KBO.boxScore['winTeam']['name'])
    essentialSentence=essentialSentence.replace('loseTeam_name',Parser_KBO.boxScore['loseTeam']['name'])
    essentialSentence=essentialSentence.replace('home_name',Parser_KBO.boxScore['home']['name'])
    essentialSentence=essentialSentence.replace('away_name',Parser_KBO.boxScore['away']['name'])  
    essentialSentence=essentialSentence.replace('winTeam_rank+1',str(Parser_DaumKBO.rank['winTeam'][0]+1))
    essentialSentence=essentialSentence.replace('winTeam_rank',str(Parser_DaumKBO.rank['winTeam'][0]))
    essentialSentence=essentialSentence.replace('winTeam_accumulation',str(Parser_DaumKBO.accumulation['winTeam']))
    essentialSentence=essentialSentence.replace('loseTeam_rank-1',str(Parser_DaumKBO.rank['loseTeam'][0]+1))
    essentialSentence=essentialSentence.replace('loseTeam_rank',str(Parser_DaumKBO.rank['loseTeam'][0]))
    essentialSentence=essentialSentence.replace('loseTeam_accumulation',str(abs(Parser_DaumKBO.accumulation['loseTeam'])))

    
    if 'nextTeam' in essentialSentence:
        essentialSentence=essentialSentence.replace('nextTeam',nextTeam)
    
    Conclusion=sentence1+sentence2+essentialSentence
    
    return Conclusion


# In[71]:

def getEmblem(Parser_KBO):
    emblem=TransformeTeamName.get(Parser_KBO.boxScore['winTeam']['name'])
    return emblem


# In[72]:

# 본문작성
def writeMain(Parser_KBO,Parser_DaumKBO):
    criticalInning=sorted(Parser_DaumKBO.criticalInning['home']+Parser_DaumKBO.criticalInning['away'])
    importantBattingKeyword=[u'안타',u'홈런',u'루타']

    #     문장뭉치
    #     Main1 : 승부처에 관한 내용
    #------- BEGIN Main1 -------#
    sentence1Group=[
    #         승부처 이닝이 없는 경기에 대한 문장들
        changeWithParam(u''),
        changeWithParam(u' () 이닝없이 경기는 진행되었다.',
                       [u' 결정적인']
                       ),
        changeWithParam(u' () 점수차에 영향을 준 이닝은 없었다.',
                       [u' 결정적으로',u'크게']
                       ),
        changeWithParam(u' 결정적이 이닝이 없었던 ()',
                       [u' 그저그런 경기의 연속이었다.'],
                       [u' 물흐르듯 지나가는 이닝이 대부분이었다.']
                       ),
        changeWithParam(u' 승부가 어느이닝에서 판가름 났다고 얘기하기는 어려웠다.') 
    ] if len(criticalInning)==0 else [
    #         승부처 이닝이 있는 경기에 대한 문장들
        changeWithParam(u' ()의 ()은 () criticalInning이닝에서 () ',
                        [u'승부',u'대결'],
                        [u'양상',u'흐름',u'분위기'],
                        [u'',u'결국'],
                        [u'갈렸다.',u'나뉘었다.',u'두드러졌다.']
                        )]
    #------- END Main1 -------#
    
    
    #     Main2는 sentenceGroup없이 바로 문장을 만든다
    #     Main2 : 승부처 이닝에 있었던 경기내용
    #------- BEGIN Main2 -------#
    sentence2=''
    inningWithPlayer={}
    

    #     inningWithPlayer[이닝][[선수명,행동][선수명,행동]]
    #     승부처 이닝을 검사
    for inning in criticalInning:
        #         10이닝 이상은 흐름을 KBO에서 알수 없음
        if inning <10:
        #         각 이닝에 타자들을 검사
            inningWithPlayer[inning]=[]
            for battingSequence in Parser_KBO.situation['winTeam'][inning-1]:
                #             해당 타자가 안타,루타,홈런이 있는지 검사
                for keyWord in importantBattingKeyword:
                    if keyWord in battingSequence['act']:
                        inningWithPlayer[inning].append({
                            'player':battingSequence['player'],
                            'act':battingSequence['act'],
                            })
                        break
                    
    #     inningWithPlayer로 문장만들기
    for inning in criticalInning:
        if inning<10:
            sentence2+=str(inning)+u'이닝 '
            sentence2+=','.join([player['player']+u'선수의 '+player['act'] for player in inningWithPlayer[inning]])
    
    #     마무리 짓기
    if len(sentence2)>0:
        sentence2+=changeWithParam(u'등의 () 팀의 승리에 기여하였다.',
                                   [u'활약들이',u'요인들이'])
    #------- END Main2 -------#
    

    #     Main3 : 키플레이어 관한 내용
    #------- BEGIN Main3 -------#
    #     boxScore['winTeam']['batRecord'].ix[u'허경민'][u'타수']
    #     승리팀에 키플레이어가 있으면
    sentence3Group=[]
    if Parser_DaumKBO.keyPlayer['winTeam']:
        # 타점+득점 >=2이상 일때만 키플레이어로 기사작성
        if int(parser_KBO.boxScore['winTeam']['batRecord'].ix[parser_DaumKBO.keyPlayer['winTeam'][1]][u'타점'])+int(parser_KBO.boxScore['winTeam']['batRecord'].ix[parser_DaumKBO.keyPlayer['winTeam'][1]][u'득점'])>=2:
            #if Parser_KBO.boxScore['winTeam'][]
            sentence3Group=[
                    changeWithParam(u' winTeam_name의 winTeam_keyPlayer[1]선수(winTeam_keyPlayer[0])가 AT타수 HITS안타 RBI타점 RUNS득점 BATTING타율을 기록하여 () ',
                                    [u'팀의 키플레이어 역할을 해주었다.',
                                     u'승리를 이끌도록 하였다.',
                                     u'팀을 승리로 리드하였다.',
                                     u'winTeam_name를 승리로 이끌었다.',
                                     u'loseTeam_name을 승리의 제물로 만들었다.',
                                     u'winTeam_name의 핵심 득점원이 되주었다.']
                                   )
            ]
    sentence4Group=[]                 
    if Parser_DaumKBO.keyPlayer['loseTeam']:
        # 타점+득점 >=2이상 일때만 키플레이어로 기사작성
        if int(parser_KBO.boxScore['loseTeam']['batRecord'].ix[parser_DaumKBO.keyPlayer['loseTeam'][1]][u'타점'])+int(parser_KBO.boxScore['loseTeam']['batRecord'].ix[parser_DaumKBO.keyPlayer['loseTeam'][1]][u'득점'])>=2:
            sentence4Group=[u'',
                changeWithParam(u' loseTeam_name의 loseTeam_keyPlayer[1] 선수(loseTeam_keyPlayer[0])가 AT타수 HITS안타 RBI타점 RUNS득점 BATTING타율을 ()',
                                [u'기록했지만 아쉽게도 팀의 승리는 힘들었다.',
                                u'기록했지만 팀을 승리로 이끌기에는 역부족이었다.',
                                u'했지만 팀의 승리를 리드하기에는 턱없이 부족했다.',
                                u'했지만 loseTeam_name의 승리를 돕기에는 부족했다.',
                                u'했지만 아쉬운 결과였다.']
                               )
            ]
                                
    #------- END Main3 -------#

                
#     문장뽑기
    sentence1=sentence1Group[random.randint(0,len(sentence1Group)-1)]
    sentence3=sentence3Group[random.randint(0,len(sentence3Group)-1)] if Parser_DaumKBO.keyPlayer['winTeam'] and len(sentence3Group)>0 else u''
    sentence4=sentence4Group[random.randint(0,len(sentence4Group)-1)] if Parser_DaumKBO.keyPlayer['loseTeam'] and len(sentence4Group)>0 else  u''
    
#    문장 만들기
    sentence1=sentence1.replace('criticalInning',', '.join((map(str,criticalInning))))
    sentence2=sentence2
    sentence3=sentence3.replace('winTeam_name',Parser_KBO.boxScore['winTeam']['name'])
    sentence3=sentence3.replace('loseTeam_name',Parser_KBO.boxScore['loseTeam']['name'])
    if Parser_DaumKBO.keyPlayer['winTeam']:
        sentence3=sentence3.replace('winTeam_keyPlayer[1]',Parser_DaumKBO.keyPlayer['winTeam'][1])
        sentence3=sentence3.replace('winTeam_keyPlayer[0]',getPositionName(Parser_DaumKBO.keyPlayer['winTeam'][0]))
        sentence3=sentence3.replace('BATTING',Parser_KBO.boxScore['winTeam']['batRecord'].ix[Parser_DaumKBO.keyPlayer['winTeam'][1]][u'타율'])
        sentence3=sentence3.replace('RUNS',Parser_KBO.boxScore['winTeam']['batRecord'].ix[Parser_DaumKBO.keyPlayer['winTeam'][1]][u'득점'])
        sentence3=sentence3.replace('HITS',Parser_KBO.boxScore['winTeam']['batRecord'].ix[Parser_DaumKBO.keyPlayer['winTeam'][1]][u'안타'])
        sentence3=sentence3.replace('RBI',Parser_KBO.boxScore['winTeam']['batRecord'].ix[Parser_DaumKBO.keyPlayer['winTeam'][1]][u'타점'])
        sentence3=sentence3.replace('AT',Parser_KBO.boxScore['winTeam']['batRecord'].ix[Parser_DaumKBO.keyPlayer['winTeam'][1]][u'타수'])    

    if Parser_DaumKBO.keyPlayer['loseTeam']:
        sentence4=sentence4.replace('loseTeam_name',Parser_KBO.boxScore['loseTeam']['name'])
        sentence4=sentence4.replace('loseTeam_keyPlayer[1]',Parser_DaumKBO.keyPlayer['loseTeam'][1])
        sentence4=sentence4.replace('loseTeam_keyPlayer[0]',getPositionName(Parser_DaumKBO.keyPlayer['loseTeam'][0]))
        sentence4=sentence4.replace('BATTING',Parser_KBO.boxScore['loseTeam']['batRecord'].ix[Parser_DaumKBO.keyPlayer['loseTeam'][1]][u'타율'])
        sentence4=sentence4.replace('RUNS',Parser_KBO.boxScore['loseTeam']['batRecord'].ix[Parser_DaumKBO.keyPlayer['loseTeam'][1]][u'득점'])
        sentence4=sentence4.replace('HITS',Parser_KBO.boxScore['loseTeam']['batRecord'].ix[Parser_DaumKBO.keyPlayer['loseTeam'][1]][u'안타'])
        sentence3=sentence3.replace('RBI',Parser_KBO.boxScore['loseTeam']['batRecord'].ix[Parser_DaumKBO.keyPlayer['loseTeam'][1]][u'타점'])
        sentence4=sentence4.replace('AT',Parser_KBO.boxScore['loseTeam']['batRecord'].ix[Parser_DaumKBO.keyPlayer['loseTeam'][1]][u'타수'])
    
                               
    return sentence1+sentence2+sentence3+sentence4


# In[73]:

tday=datetime.date.today()


# In[74]:

# yesterday
tday=tday - datetime.timedelta(1)


# In[75]:

todayStr=str('%04d%02d%02d'%(tday.year,tday.month,tday.day))


# In[83]:

# 최신날짜
# startDate=todayStr
startDate='20160919'
# 예전날짜
# endDate=todayStr
endDate='20160919'
urlParserForKBO = UrlParserForKBO(startDate,endDate)


# In[21]:

# MySQL conf
con=MySQLdb.connect(host='218.150.181.131',user='root',passwd='1234',db='link10th',charset='utf8', use_unicode=True)

for url in urlParserForKBO.urlList:
    print url
    parser_KBO=Parser_KBO(url)
    parser_DaumKBO=Parser_DaumKBO(parser_KBO.boxScore['date'],parser_KBO.boxScore['away']['name'])
    
#     try:
    date=writeDate(parser_KBO)
    contextClassifier=getClassifier(parser_KBO,parser_DaumKBO)
    Head=writeHead(parser_KBO,parser_DaumKBO,contextClassifier)
    Intro=writeIntro(parser_KBO,parser_DaumKBO,contextClassifier)
    Main=writeMain(parser_KBO,parser_DaumKBO)
    Conc=writeConc(parser_KBO,parser_DaumKBO,contextClassifier)
    End=writeEnd(parser_KBO,parser_DaumKBO)
    emblem=getEmblem(parser_KBO)
    homeT=TransformeTeamName.get(parser_KBO.boxScore['home']['name'])
    awayT=TransformeTeamName.get(parser_KBO.boxScore['away']['name'])
    A1=parser_KBO.boxScore['away']['score'][0]
    A2=parser_KBO.boxScore['away']['score'][1]
    A3=parser_KBO.boxScore['away']['score'][2]
    A4=parser_KBO.boxScore['away']['score'][3]
    A5=parser_KBO.boxScore['away']['score'][4]
    A6=parser_KBO.boxScore['away']['score'][5]
    A7=parser_KBO.boxScore['away']['score'][6]
    A8=parser_KBO.boxScore['away']['score'][7]
    A9=parser_KBO.boxScore['away']['score'][8]
    A10=parser_KBO.boxScore['away']['score'][9]
    A11=parser_KBO.boxScore['away']['score'][10]
    A12=parser_KBO.boxScore['away']['score'][11]
    AR=parser_KBO.boxScore['away']['score'][12]
    AH=parser_KBO.boxScore['away']['score'][13]
    AE=parser_KBO.boxScore['away']['score'][14]
    AB=parser_KBO.boxScore['away']['score'][15]

    H1=parser_KBO.boxScore['home']['score'][0]
    H2=parser_KBO.boxScore['home']['score'][1]
    H3=parser_KBO.boxScore['home']['score'][2]
    H4=parser_KBO.boxScore['home']['score'][3]
    H5=parser_KBO.boxScore['home']['score'][4]
    H6=parser_KBO.boxScore['home']['score'][5]
    H7=parser_KBO.boxScore['home']['score'][6]
    H8=parser_KBO.boxScore['home']['score'][7]
    H9=parser_KBO.boxScore['home']['score'][8]
    H10=parser_KBO.boxScore['home']['score'][9]
    H11=parser_KBO.boxScore['home']['score'][10]
    H12=parser_KBO.boxScore['home']['score'][11]
    HR=parser_KBO.boxScore['home']['score'][12]
    HH=parser_KBO.boxScore['home']['score'][13]
    HE=parser_KBO.boxScore['home']['score'][14]
    HB=parser_KBO.boxScore['home']['score'][15]
#     except:
#         sys.stderr.write(unicode.format(u'********** 날짜 : %s %s와 %s의 경기 파싱오류 ********** '%(parser_KBO.boxScore['date'],parser_KBO.boxScore['away']['name'],parser_KBO.boxScore['home']['name'])))
    
    #교정부분
    checkInstance=String_checker(Intro)
    Intro=checkInstance.reSentence()
    checkInstance=String_checker(Main)
    Main=checkInstance.reSentence()
    checkInstance=String_checker(Conc)
    Conc=checkInstance.reSentence()
    checkInstance=String_checker(End)
    End=checkInstance.reSentence()
    
    cursor=con.cursor()
    #-------BEGIN Article TABLE-------#
    sql='''
    INSERT INTO Article(date,Head,Intro,Main,Conc,End,url,emblem,homeT,awayT,
    A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,AR,AH,AE,AB,
    H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11,H12,HR,HH,HE,HB,
    awayH,awayHR,awaySB,awayBB,awaySO,awayE,awayGDP,awayLOB,
    homeH,homeHR,homeSB,homeBB,homeSO,homeE,homeGDP,homeLOB
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s
    )
    '''
    placeholder=[date,Head,Intro,Main,Conc,End,url,emblem,
                 TransformeTeamName.get(parser_KBO.boxScore['home']['name']),
                 TransformeTeamName.get(parser_KBO.boxScore['away']['name']),
                 parser_KBO.boxScore['away']['score'][0],
                 parser_KBO.boxScore['away']['score'][1],
                 parser_KBO.boxScore['away']['score'][2],
                 parser_KBO.boxScore['away']['score'][3],
                 parser_KBO.boxScore['away']['score'][4],
                 parser_KBO.boxScore['away']['score'][5],
                 parser_KBO.boxScore['away']['score'][6],
                 parser_KBO.boxScore['away']['score'][7],
                 parser_KBO.boxScore['away']['score'][8],
                 parser_KBO.boxScore['away']['score'][9],
                 parser_KBO.boxScore['away']['score'][10],
                 parser_KBO.boxScore['away']['score'][11],
                 parser_KBO.boxScore['away']['score'][12],
                 parser_KBO.boxScore['away']['score'][13],
                 parser_KBO.boxScore['away']['score'][14],
                 parser_KBO.boxScore['away']['score'][15],
                 parser_KBO.boxScore['home']['score'][0],
                 parser_KBO.boxScore['home']['score'][1],
                 parser_KBO.boxScore['home']['score'][2],
                 parser_KBO.boxScore['home']['score'][3],
                 parser_KBO.boxScore['home']['score'][4],
                 parser_KBO.boxScore['home']['score'][5],
                 parser_KBO.boxScore['home']['score'][6],
                 parser_KBO.boxScore['home']['score'][7],
                 parser_KBO.boxScore['home']['score'][8],
                 parser_KBO.boxScore['home']['score'][9],
                 parser_KBO.boxScore['home']['score'][10],
                 parser_KBO.boxScore['home']['score'][11],
                 parser_KBO.boxScore['home']['score'][12],
                 parser_KBO.boxScore['home']['score'][13],
                 parser_KBO.boxScore['home']['score'][14],
                 parser_KBO.boxScore['home']['score'][15],
                 parser_DaumKBO.batRecord['away']['H'],
                 parser_DaumKBO.batRecord['away']['HR'],
                 parser_DaumKBO.batRecord['away']['SB'],
                 parser_DaumKBO.batRecord['away']['BB'],
                 parser_DaumKBO.batRecord['away']['SO'],
                 parser_DaumKBO.batRecord['away']['E'],
                 parser_DaumKBO.batRecord['away']['GDP'],
                 parser_DaumKBO.batRecord['away']['LOB'],
                 parser_DaumKBO.batRecord['home']['H'],
                 parser_DaumKBO.batRecord['home']['HR'],
                 parser_DaumKBO.batRecord['home']['SB'],
                 parser_DaumKBO.batRecord['home']['BB'],
                 parser_DaumKBO.batRecord['home']['SO'],
                 parser_DaumKBO.batRecord['home']['E'],
                 parser_DaumKBO.batRecord['home']['GDP'],
                 parser_DaumKBO.batRecord['home']['LOB']                 
                 ]
    cursor.execute(sql,placeholder)
    #-------END Article TABLE-------#
    
    #-------BEGIN CriticalVOD_Url TABLE-------#
    for url in parser_DaumKBO.criticalInningVOD_Url: 
        sql="""      
        INSERT INTO CriticalVOD_Url(Article_Id,vodUrl)
        VALUES(getArticleId(%s,%s),%s);      
        """  
        placeholder=[int(parser_KBO.boxScore['date'][:8]),parser_KBO.boxScore['away']['name'],url]
        print sql
        print placeholder
        cursor.execute(sql,placeholder)
    #-------END CriticalVOD_Url TABLE-------#
    
    #-------BEGIN winlosePitcher TABLE ------#
    parser_DaumKBO.winlosePitcher['winTeam']['winCount']
    
    sql="""
    INSERT INTO winlosePitcher(Article_Id,winPlayerName,winPlayerWinCount,winPlayerLoseCount,winPlayerERA,winPlayerFaceUrl,
    losePlayerName,losePlayerWinCount,losePlayerLoseCount,losePlayerERA,losePlayerFaceUrl)
    VALUES(getArticleId(%s,%s),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    placeholder=[int(parser_KBO.boxScore['date'][:8]),parser_KBO.boxScore['away']['name'],
                 parser_DaumKBO.winlosePitcher['winTeam']['name'],parser_DaumKBO.winlosePitcher['winTeam']['winCount'],parser_DaumKBO.winlosePitcher['winTeam']['loseCount'],parser_DaumKBO.winlosePitcher['winTeam']['ERA'],parser_DaumKBO.winlosePitcher['winTeam']['faceUrl'],
                 parser_DaumKBO.winlosePitcher['loseTeam']['name'],parser_DaumKBO.winlosePitcher['loseTeam']['winCount'],parser_DaumKBO.winlosePitcher['loseTeam']['loseCount'],parser_DaumKBO.winlosePitcher['loseTeam']['ERA'],parser_DaumKBO.winlosePitcher['loseTeam']['faceUrl']
                ]
    print sql
    print placeholder
    cursor.execute(sql,placeholder)
    #-------END winlosePitcherTABLE-------#
    
    
#     MySQL disconnect
    con.commit()
    cursor.close()
con.close()


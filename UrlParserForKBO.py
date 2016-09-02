
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import time
import urllib2
import os


# In[6]:

class UrlParserForKBO:
#     초기화때 날짜를 입력(박스스코어 확인 날짜)
    def __init__(self,startDate,endDate):
#       박스스코어의 url을 담는 리스트
        self.urlList=[]
    
        today=datetime.date.today()
        date=str(startDate)
        yy=int(date[:4])
        mm=int(date[4:6])
        dd=int(date[6:])
        date=datetime.date(yy,mm,dd)
        
#         startDate로 이동
        backCount=(today-date).days
    
    # 크롬창 
        if os.name=='nt':
            browser = webdriver.Chrome(executable_path='./chromedriver.exe')
        else:
            browser = webdriver.Chrome(executable_path='./chromedriver')
            # 접속        
        browser.get('http://www.koreabaseball.com/Schedule/ScoreBoard/ScoreBoard.aspx')
        
        for i in range(backCount):
#             이전일 버튼
            browser.find_element_by_id('cphContainer_cphContents_btnPreDate').click()
            time.sleep(0.7)
        
        endYY=int(endDate[:4])
        endMM=int(endDate[4:6])
        endDD=int(endDate[6:])
        endDate=datetime.date(endYY,endMM,endDD)
        
        backCount=(date-endDate).days

        # backCount일 전의 경기들의 BoxScore 갯수 btnList에 저장
        for i in range(backCount+1):
        #     이전일 버튼            
            btnList = browser.find_elements_by_css_selector('a[href^="/Schedule/Game/BoxScore.aspx?"]')
            for href_in_btnList in btnList:
                self.urlList.append(href_in_btnList.get_attribute('href'))
            browser.find_element_by_id('cphContainer_cphContents_btnPreDate').click()
            time.sleep(0.7)
        browser.quit()
        self.urlList.reverse()
        
        def getUrlList(self):
            return self.urlList


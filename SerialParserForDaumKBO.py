
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import sys
import urllib2


# In[3]:

#날짜와 AWAY팀이름을 넣으면 url상의 serial을 반환
class SerialParserForDaumKBO:
    def __init__(self,date,awayTeam):
        year=date[:4]
        month=date[4:4+2]
        day=date[4+2:(4+2)+2]
        
        url='http://score.sports.media.daum.net/schedule/baseball/kbo/main.daum?game_year=%s&game_month=%s'%(year,month)
        page=urllib2.urlopen(url)
        html=BeautifulSoup(page)
        s=unicode(html)
        # date_index=s.find(str.format('<td class="time_date" rowspan="5">%d<span class="txt_day">'%(int(day))))
        date_index=s.find(str.format('%d<span class="txt_day">'%(int(day))))
#         찾는 데이터가 없을때
        if date_index==-1:
            sys.stderr.write('******* Cannot found Game with date : %s awayTeam : %s data******* '%(date,awayTeam))
            return None
        
        s=s[date_index:]
        
        s=s[s.find(awayTeam):]
        serial_find_url='http://sports.media.daum.net/sports/gamecenter/'
        serial_start_index=s.find(serial_find_url)+len(serial_find_url)
        serial=s[serial_start_index:serial_start_index+8]
        self.serial=serial
        
    def getSerial(self):
        return self.serial


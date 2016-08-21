
# coding: utf-8

# In[13]:

class getInitialTeamName:
    # 이니셜이름을 반환해주는 메서드
    @staticmethod
    def get(teamName):
        if teamName==u'삼성':
            initialName=u'SS'
        elif teamName==u'한화':
            initialName=u'HH'
        elif teamName==u'SK':
            initialName=u'SK'
        elif teamName==u'KIA':
            initialName=u'HT'
        elif teamName==u'LG':
            initialName=u'LG'
        elif teamName==u'두산':
            initialName=u'OB'
        elif teamName==u'롯데':
            initialName=u'LT'
        elif teamName==u'넥센':
            initialName=u'WO'
        elif teamName==u'kt':
            initialName=u'KT'
        elif teamName==u'NC':
            initialName=u'NC'
        else:
            initialName=None

        return initialName


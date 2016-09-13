
# coding: utf-8

# In[3]:

class TransformeTeamName:
    # 이니셜이름을 반환해주는 메서드
    @staticmethod
    def get(teamName):
        if teamName==u'삼성':
            initialName=u'SS'
        elif teamName==u'SS':
            initialName=u'삼성'

        elif teamName==u'한화':
            initialName=u'HH'
        elif teamName==u'HH':
            initialName=u'한화'

        elif teamName==u'SK':
            initialName=u'SK'
            
        elif teamName==u'KIA':
            initialName=u'HT'
        elif teamName==u'HT':
            initialName=u'KIA'
            
        elif teamName==u'LG':
            initialName=u'LG'
            
        elif teamName==u'두산':
            initialName=u'OB'
        elif teamName==u'OB':
            initialName=u'두산'
            
        elif teamName==u'롯데':
            initialName=u'LT'
        elif teamName==u'LT':
            initialName=u'롯데'
            
        elif teamName==u'넥센':
            initialName=u'WO'
        elif teamName==u'WO':
            initialName=u'넥센'
            
        elif teamName==u'kt':
            initialName=u'KT'
        elif teamName==u'KT':
            initialName=u'kt'
            
        elif teamName==u'NC':
            initialName=u'NC'
            
        else:
            initialName=None

        return initialName


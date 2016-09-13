
# coding: utf-8

# In[29]:


#은는이가을를
class String_checker:
    
    def __init__(self, sentences):
        self.sentences = sentences
    def reSentence(self):
        self.count = 0
        self.sTeam = []
        self.s1 = u'삼성'
        self.s2 = u'한화'
        self.s3 = u'롯데'
        self.s4 = u'두산'
        self.s5 = u'넥센'
        self.s6 = u'SK'
        self.s7 = u'KIA'
        self.s8 = u'kt'
        self.s9 = u'NC'
        self.s10 = u'LG'
        if(self.sentences.find(self.s1+u'는')!=-1 or \
           self.sentences.find(self.s1+u'가')!=-1 or \
           self.sentences.find(self.s1+u'를')!=-1 or \
           self.sentences.find(self.s1+u'와')!=-1):
            self.count+=1
            self.sTeam.append(u'삼성')
            self.sentences = self.sentences.replace(u'삼성는', u'삼성은')
            self.sentences = self.sentences.replace(u'삼성가', u'삼성이')
            self.sentences = self.sentences.replace(u'삼성를', u'삼성을')
            self.sentences = self.sentences.replace(u'삼성와', u'삼성과')
        if(self.sentences.find(self.s2+u'은')!=-1 or \
           self.sentences.find(self.s2+u'이')!=-1 or \
           self.sentences.find(self.s2+u'을')!=-1 or \
           self.sentences.find(self.s2+u'과')!=-1):
            self.count+=1
            self.sTeam.append(u'한화')
            self.sentences = self.sentences.replace(u'한화은', u'한화는')
            self.sentences = self.sentences.replace(u'한화이', u'한화가')
            self.sentences = self.sentences.replace(u'한화을', u'한화를')
            self.sentences = self.sentences.replace(u'한화과', u'한화와')
        if(self.sentences.find(self.s3+u'은')!=-1 or \
           self.sentences.find(self.s3+u'이')!=-1 or \
           self.sentences.find(self.s3+u'을')!=-1 or \
           self.sentences.find(self.s3+u'과')!=-1):
            self.count+=1
            self.sTeam.append(u'롯데')
            self.sentences = self.sentences.replace(u'롯데은', u'롯데는')
            self.sentences = self.sentences.replace(u'롯데이', u'롯데가')
            self.sentences = self.sentences.replace(u'롯데을', u'롯데를')
            self.sentences = self.sentences.replace(u'롯데과', u'롯데와')
        if(self.sentences.find(self.s4+u'는')!=-1 or \
           self.sentences.find(self.s4+u'가')!=-1 or \
           self.sentences.find(self.s4+u'를')!=-1 or \
           self.sentences.find(self.s4+u'와')!=-1):
            self.count+=1
            self.sTeam.append(u'두산')
            self.sentences = self.sentences.replace(u'두산는', u'두산은')
            self.sentences = self.sentences.replace(u'두산가', u'두산이')
            self.sentences = self.sentences.replace(u'두산를', u'두산을')
            self.sentences = self.sentences.replace(u'두산와', u'두산과')
        if(self.sentences.find(self.s5+u'는')!=-1 or \
           self.sentences.find(self.s5+u'가')!=-1 or \
           self.sentences.find(self.s5+u'를')!=-1 or \
           self.sentences.find(self.s5+u'와')!=-1):
            self.count+=1
            self.sTeam.append(u'넥센')
            self.sentences = self.sentences.replace(u'두산는', u'두산은')
            self.sentences = self.sentences.replace(u'두산가', u'두산이')
            self.sentences = self.sentences.replace(u'두산를', u'두산을')
            self.sentences = self.sentences.replace(u'두산와', u'두산과')
        if(self.sentences.find(self.s6+u'은')!=-1 or \
           self.sentences.find(self.s6+u'이')!=-1 or \
           self.sentences.find(self.s6+u'을')!=-1 or \
           self.sentences.find(self.s6+u'과')!=-1):
            self.count+=1
            self.sTeam.append(u'SK')
            self.sentences = self.sentences.replace(u'SK은', u'SK는')
            self.sentences = self.sentences.replace(u'SK이', u'SK가')
            self.sentences = self.sentences.replace(u'SK을', u'SK를')
            self.sentences = self.sentences.replace(u'SK과', u'SK와')
        if(self.sentences.find(self.s7+u'은')!=-1 or \
           self.sentences.find(self.s7+u'이')!=-1 or \
           self.sentences.find(self.s7+u'을')!=-1 or \
           self.sentences.find(self.s7+u'과')!=-1):
            self.count+=1
            self.sTeam.append(u'KIA')
            self.sentences = self.sentences.replace(u'KIA은', u'KIA는')
            self.sentences = self.sentences.replace(u'KIA이', u'KIA가')
            self.sentences = self.sentences.replace(u'KIA을', u'KIA를')
            self.sentences = self.sentences.replace(u'KIA과', u'KIA와')
        if(self.sentences.find(self.s8+u'은')!=-1 or \
           self.sentences.find(self.s8+u'이')!=-1 or \
           self.sentences.find(self.s8+u'을')!=-1 or \
           self.sentences.find(self.s8+u'과')!=-1):
            self.count+=1
            self.sTeam.append(u'kt')
            self.sentences = self.sentences.replace(u'kt은', u'kt는')
            self.sentences = self.sentences.replace(u'kt이', u'kt가')
            self.sentences = self.sentences.replace(u'kt을', u'kt를')
            self.sentences = self.sentences.replace(u'kt과', u'kt와')
        if(self.sentences.find(self.s9+u'은')!=-1 or \
           self.sentences.find(self.s9+u'이')!=-1 or \
           self.sentences.find(self.s9+u'을')!=-1 or \
           self.sentences.find(self.s9+u'과')!=-1):
            self.count+=1
            self.sTeam.append(u'NC')
            self.sentences = self.sentences.replace(u'NC은', u'NC는')
            self.sentences = self.sentences.replace(u'NC이', u'NC가')
            self.sentences = self.sentences.replace(u'NC을', u'NC를')
            self.sentences = self.sentences.replace(u'NC과', u'NC와')
        if(self.sentences.find(self.s10+u'은')!=-1 or \
           self.sentences.find(self.s10+u'이')!=-1 or \
           self.sentences.find(self.s10+u'을')!=-1 or \
           self.sentences.find(self.s10+u'과')!=-1):
            self.count+=1
            self.sTeam.append(u'LG')
            self.sentences = self.sentences.replace(u'LG은', u'LG는')
            self.sentences = self.sentences.replace(u'LG이', u'LG가')
            self.sentences = self.sentences.replace(u'LG을', u'LG를')
            self.sentences = self.sentences.replace(u'LG과', u'LG와')
        return self.sentences




#import pyttsx3
from processor import textProcessor as tp
from browsing import browse as br

'''
speech_engine = pyttsx3.init('espeak')


speech_engine.setProperty('rate', 120)
speech_engine.setProperty('voice', 'female5')
'''

class speech_syn:

    def __init__(self, name, text):
        self._name = name
        self._greet = text
   #     self.greet()

    def who_are_you(self):
        self.speak("Hey,  I'm "+self._name)


    def greet(self):
        intro = tp.textProcessor().self_intro()
        labelling_intro = tp.textProcessor().put_frequency(intro)
        
        for token in labelling_intro: 
            self.do_syn(token)

    def reply(self, text):        
        tokens = tp.textProcessor().tokenize(text)

        openable = br.browse().is_openable_browser(tokens)
        
        if openable[0] == 1:
            br.browse().open_browser("www."+openable[2]+".com")
            labelling_str_reply = tp.textProcessor().put_frequency("ok i am going to open it")
            for token in labelling_str_reply:
                self.do_syn(token)
            return ""

        searchable = br.browse().is_searchable_browser(tokens)
        if searchable[0] == 1:
            br.browse().search_browser(searchable[2])
            labelling_str_reply = tp.textProcessor().put_frequency("ok i am going to open it")
            for token in labelling_str_reply:
                self.do_syn(token)
            return ""
        


        str_tokens = tp.textProcessor().put_underscore(tokens)

        str_reply = tp.textProcessor().get_reply(str_tokens)
        print('==============================================================> str_reply -->  ', str_reply )
        return str_reply
'''
        
        if len(str_reply)-2 == 0:
            labelling_str_reply = tp.textProcessor().put_frequency("sorry i could not understand you")
            
            
            for token in labelling_str_reply:
                self.do_syn(token)
            return 

        labelling_str_reply = tp.textProcessor().put_frequency(str_reply)

        if labelling_str_reply == 0:
            return

        #print("labelling_str_reply -----> ", labelling_str_reply)

'''

'''
        for token in labelling_str_reply: 
            self.do_syn(token)


g = speech_syn('Gizmo', 'Hi')
'''

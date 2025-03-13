import re
from values.translatorData import TranslatorData
from utils.globalLogger import log

class Translator:
    def __init__(self,Data:TranslatorData):
        log("Loading Translator")
        self.Data = Data
    def Translate(self):
        self.Patterns = self.Data.Patterns
        self.Code = self.Data.Code
        #print(self.Patterns)
        #print(self.Code)
        for Pattern, MatchData in self.Patterns.items():
            Replacement = MatchData[0]
            Whitespace = MatchData[1]
            if (not Replacement) or (Replacement == None):
                Replacement = ""
            log(f"Translating: {Pattern} with {Replacement}")
            if Whitespace == False:
                print("whitespace")
                Regex = re.compile(r'^\s*(' + Pattern + ')')
                self.Code = "\n".join([Regex.sub(r'\1', Line) for Line in str(self.Code).splitlines()])
            else:
                self.Code = (re.sub(Pattern,Replacement,self.Code)).lower()
        self.Output = self.Code.strip()
    def GetTranslated(self):
        return self.Output
import re
from values.translatorData import TranslatorData
from lib.compiler.regexTranslate import RegexTranslate
from lib.compiler.libraryHandler import LibraryHandler
from utils.globalLogger import log

class Translator:
    def __init__(self,Data:TranslatorData):
        log("Loading Translator")
        self.Data = Data
        self.Code = self.Data.Code

    def Translate(self):
        log("Translating")
        self.LibraryTranslator = LibraryHandler(self.Data)
        self.LibraryTranslator.Main()
        self.Code = self.LibraryTranslator.GetOutput()
        log("Finished Library Translate")
        self.Data.Code = self.Code
        self.RegexTranslator = RegexTranslate(self.Data)
        self.RegexTranslator.Translate()
        self.Code = self.RegexTranslator.GetTranslated()
        self.Output = self.Code.strip()
    def GetTranslated(self):
        return self.Output
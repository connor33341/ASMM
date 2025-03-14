from values.translatorData import TranslatorData
from lib.compiler.byLines import ByLines
from utils.globalLogger import log

class LibraryHandler:
    def __init__(self,Data: TranslatorData):
        self.Data = Data
        self.Running = True
        log("Running Library Handler")
    
    def Main(self):
        self.CurrentFile = ByLines(self.Data.Code)
        while self.Running:
            self.CurrentLine = self.CurrentFile.ReadNext()
            self.LineIndex = self.CurrentFile.Index
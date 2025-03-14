from values.translatorData import TranslatorData
from lib.compiler.byLines import ByLines
from utils.globalLogger import log

class LibraryHandler:
    def __init__(self,Data: TranslatorData):
        self.Data = Data
        self.Running = True
        self.Output = ""
        log("Library Handler Init")
    
    def Main(self):
        log("Library Handler Running")
        self.CurrentFile = ByLines(self.Data.Code)
        while self.Running:
            self.CurrentLine = self.CurrentFile.ReadNext()
            self.LineIndex = self.CurrentFile.Index
            log(f"Reading Line: {self.LineIndex}")
            if type(self.CurrentLine) == str:
                pass
            else:
                self.Running = False
                log("Finished Handling Libraries")
        self.Output = self.CurrentFile.Stitch()

    def GetOutput(self):
        return self.Output
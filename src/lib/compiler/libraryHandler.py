from values.translatorData import TranslatorData
from lib.compiler.byLines import byLines
from utils.globalLogger import log

class LibraryHandler:
    def __init__(self,Data: TranslatorData):
        self.Data = Data
        self.LineReader = ByLines()

    
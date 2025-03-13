import xml
import logging
import xml.etree.ElementTree as ET
from utils.globalLogger import log

class PatternLoader:
    def __init__(self,File: str = ""):
        log("Pattern Loader Init")
        self.FileName = File
    def Load(self):
        log(f"Loading Pattern File: {self.FileName}")
        self.Tree = ET.parse(self.FileName)
        self.Root = self.Tree.getroot()
        self.Patterns = {}
        for Rule in self.Root.findall("rule"):
            Pattern = Rule.find("pattern").text
            Replacement = Rule.find("replacement").text
            self.Patterns[Pattern] = Replacement
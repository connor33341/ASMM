from utils.globalLogger import log

class ByLines:
    def __init__(self,Data: str = ""):
        self.Data = Data
        self.Index = 0
        self.Lines = str(self.Data).splitlines()
        self.Length = len(self.Lines)
        self.EditedLines = self.Lines
        self.EditedData = ""
    
    def ReadLine(self,Index: int):
        return self.Lines[Index]
    
    def ReadNext(self):
        NewIndex = self.Index + 1
        if NewIndex <= self.Length:
            self.Index = NewIndex
            return self.ReadLine(NewIndex)
        else:
            return False
        
    def EditLine(self,Index: int,Data: str):
        self.EditedLines.pop(Index)
        self.EditedLines.insert(Index,Data)

    def Stitch(self):
        self.EditedData = ""
        for Line in self.EditedLines:
            self.EditedData = self.EditedData + f"{Line}\n"
        return self.EditedData
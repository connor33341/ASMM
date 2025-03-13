import logging
import uuid
from lib.argParser import ArgParser
from utils.patternLoader import PatternLoader
from utils.loadProject import LoadProject
from utils.globalLogger import log
from values.outputType import OutputType
from values.project import Project
from values.args import Args

ID = str(uuid.uuid4())
print(f"[INFO]: Initalizing, ID: {ID}")
logging.basicConfig(level=logging.INFO,filename=f"src/logs/{ID}.log")

class Main:
    def __init__(self):
        self.ArgParser = ArgParser()
        self.ArgParser.Parse()
        self.Args = self.ArgParser.Args
        self.ArgClass = Args(self.Args)
        self.Project = Project()
        self.Project.Args = self.ArgClass
        self.Project.HandleArgs()
        self.Project.LoadProject()
        self.PatternLoader = PatternLoader("src/config/regex.xml")
        self.PatternLoader.Load()
        self.Patterns = self.PatternLoader.Patterns
if __name__ == "__main__":
    log("Initalization")
    MainClass = Main()

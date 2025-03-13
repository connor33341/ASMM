import logging
import uuid
from lib.argParser import ArgParser
from lib.translator import Translator
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
        self.PatternLoader = PatternLoader("src/config/regex.xml")
        self.PatternLoader.Load()
        self.Patterns = self.PatternLoader.Patterns
        self.Project.Patterns = self.Patterns
        self.Project.LoadProject()
        log("Build Completed")
if __name__ == "__main__":
    log("Initalization")
    MainClass = Main()

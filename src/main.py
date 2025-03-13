import logging
import uuid
from lib.argParser import ArgParser
from utils.loadProject import LoadProject
from values.outputType import OutputType
from values.project import Project
from values.args import Args

ID = str(uuid.uuid4())
print(f"[INFO]: Initalizing, ID: {ID}")
logging.basicConfig(level=logging.INFO,filename=f"src/logs/{ID}.log")
logger = logging.getLogger(__name__)
def log(Text: str,Level: str = "INFO",Throws: bool = False):
    if Level == "INFO":
        logger.info(Text)
    elif Level == "ERROR":
        logger.error(Text)
        if Throws:
            raise Exception(Text)
    print(f"[{Level}]: {Text}")

class Main:
    def __init__(self):
        self.ArgParser = ArgParser()
        self.ArgParser.Parse()
        self.Args = self.ArgParser.Args
        self.ArgClass = Args(self.Args)
        self.Project = Project(self.Args.config)
        self.Project.Args = self.ArgClass
if __name__ == "__main__":
    log("Initalization")
    MainClass = Main()

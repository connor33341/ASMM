import argparse
import logging
from values.args import Args
from utils.loadProject import LoadProject

logger = logging.getLogger(__name__)
def log(Text: str,Level: str = "INFO",Throws: bool = False):
    if Level == "INFO":
        logger.info(Text)
    elif Level == "ERROR":
        logger.error(Text)
        if Throws:
            raise Exception(Text)
    print(f"[{Level}]: {Text}")

class Project:
    def __init__(self,ProjectFile: str = ""):
        log("Project INIT")
        self.ProjectFile = ProjectFile
        self.Args: Args

    def HandleArgs(self):
        log("Handling Args")
        self.Args.ToJson()
        ProjectFile = self.Args.ArgExists("config")
        if type(ProjectFile) == bool:
            log("Config Argument Missing","ERROR",True)
        self.ProjectFile = ProjectFile
        log(f"Project File: {self.ProjectFile}")

    def LoadProject(self):
        log("Loading Project")
        self.ProjectLoader = LoadProject(self.ProjectFile)
        self.ProjectLoader.LoadJson()
        self.ValidDirs = self.ProjectLoader.ValidateFiles()
        if self.ValidDirs:
            log("Directory Validated")
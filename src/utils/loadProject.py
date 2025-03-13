import json
import logging
import os
from values.outputType import OutputType
from utils.globalLogger import log

class LoadProject():
    def __init__(self,ProjectFile: str = ""):
        if (ProjectFile == "") or (not ProjectFile):
            log("Project File is missing","ERROR")
            raise Exception("Missing File")
        self.ProjectFile = ProjectFile
    
    def LoadJson(self):
        log(f"Loading File: {self.ProjectFile}")
        with open(self.ProjectFile,"r") as File:
            self.Config = json.loads(File.read())
            File.close()
        log("File Loaded")
        try:
            self.Files = self.Config["files"]
            self.Target = self.Config["target"]
            self.OutputDir = self.Config["output"]
            self.Version = self.Config["version"]
            self.Compile = self.Config["compile"]
            log(f"BuildFile Version: {self.Version}")
            log(f"Building: {len(self.Target)} files")
            self.Workspace = os.path.dirname(self.ProjectFile)
            log(f"Workspace: {self.Workspace}")
        except Exception as Error:
            log(f"JSON File may have errors: {Error}","ERROR")
    def NormalizeDir(self,Dir: str) -> str:
        return os.path.join(self.Workspace,Dir)
    
    def ValidateFiles(self) -> bool:
        self.NormalizedOutput = self.NormalizeDir(self.OutputDir)
        #print(self.NormalizedOutput)
        OutputExists = os.path.isdir(self.NormalizedOutput)
        if not OutputExists:
            os.makedirs(self.NormalizedOutput,exist_ok=True)
        log("Files exist")
        return True
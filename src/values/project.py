import argparse
import logging
import io
import os
from values.args import Args
from values.translatorData import TranslatorData
from utils.loadProject import LoadProject
from utils.globalLogger import log
from lib.translator import Translator

class Project:
    def __init__(self,ProjectFile: str = ""):
        log("Project INIT")
        self.ProjectFile = ProjectFile
        self.Args: Args
        self.Patterns = {}

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
        self.Files = self.ProjectLoader.Files
        for File in self.Files:
            log(f"Translating File: {File}")
            FileData = TranslatorData()
            FileData.Patterns = self.Patterns
            try:
                NormalizedFile = self.ProjectLoader.NormalizeDir(File)
                log(f"Normalized Dir: {NormalizedFile}")
                with io.open(NormalizedFile,"r") as IOFile:
                    FileData.Code = IOFile.read()
                    IOFile.close()
            except Exception as Error:
                log(Error,"ERROR",True)
            FileTranslator = Translator(FileData)
            FileTranslator.Translate()
            AssemblyData = FileTranslator.GetTranslated()
            FileName = os.path.basename(str(File).split(".")[0])
            OutputFileDir = self.ProjectLoader.NormalizedOutput+"/"+FileName+".asm"
            with io.open(OutputFileDir,"w") as OutputFile:
                OutputFile.write(AssemblyData)
                OutputFile.close()
            log("File Written")


            
import argparse
import logging
from utils.globalLogger import log

class ArgParser:
    def __init__(self):
        log("Argument Parser Started")
        try:
            self.Parser = argparse.ArgumentParser(description=".asmm x86 Translator/Compiler")
            self.Parser.add_argument("--config",required=True,help="Project File, can be generated with a wrapper")
        except Exception as Error:
            log(f"Invalid Args: {Error}","ERROR",True)

    def Parse(self) -> None:
        log("Parsing")
        self.Args = self.Parser.parse_args()
        #print(type(self.Args)) argparse.Namespace
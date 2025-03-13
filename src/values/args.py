import argparse
import json

class Args:
    def __init__(self,Arguments: argparse.Namespace):
        self.Args = Arguments
        self.JsonArgs = {}

    def ToJson(self):
        for Arg in vars(self.Args):
            self.JsonArgs[str(Arg)] = str(getattr(self.Args,Arg))

    def ArgExists(self,Key: str):
        Exists = False
        try:
            Value = self.JsonArgs[Key]
            if Value:
                Exists = True
        except Exception as Error:
            pass
        if Exists:
            return Value
        else:
            return False
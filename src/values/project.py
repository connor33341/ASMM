import argparse
from values.args import Args
class Project:
    def __init__(self,ProjectFile: str = ""):
        self.ProjectFile = ProjectFile
        self.Args: Args
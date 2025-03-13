import argparse
import logging

logger = logging.getLogger(__name__)
def log(Text: str,Level: str = "INFO",Throws: bool = False):
    if Level == "INFO":
        logger.info(Text)
    elif Level == "ERROR":
        logger.error(Text)
        if Throws:
            raise Exception(Text)
    print(f"[{Level}]: {Text}")

class ArgParser:
    def __init__(self):
        log("Argument Parser Started")
        self.Parser = argparse.ArgumentParser()
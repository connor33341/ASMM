import logging
import inspect

def log(Text: str,Level: str = "INFO",Throws: bool = False):
    From = inspect.stack()[1]
    Module = inspect.getmodule(From[0])
    logger = logging.getLogger(Module.__name__)
    if Level == "INFO":
        logger.info(Text)
    elif Level == "ERROR":
        logger.error(Text)
        if Throws:
            raise Exception(Text)
    print(f"[{Level}]: {Text}")
#TODO: import 5 python methods we want to fuzz
#from scanner import isValidUserName
import random
import string
#from parserFuzzer import userNameFuzzer
from graphtaintFuzzer import constructHelmStringFuzzer
from myLogger import giveMeLoggingObject
#TODO: implement fuzzer

def fuzzer():
    #create logger
    logger = giveMeLoggingObject()
    
    #userNameFuzzer()
    try:
        logger.info("Logging constructHelmStringFuzzer() from graphtaint.py:")
        logger.info("Result {}", constructHelmStringFuzzer())
        logger.info("Logging getHelpTemplateContent() form graphtaint.py:")
        logger.info("Result {}", getHelmTemplateContentFuzzer())
    except Exception as e:
        logger.error("An error occurred:\n", exc_info=True)
    return 0

if __name__=='__main__':
    fuzzer()


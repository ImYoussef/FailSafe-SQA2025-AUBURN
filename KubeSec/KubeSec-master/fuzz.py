#TODO: import 5 python methods we want to fuzz
#from scanner import isValidUserName
import random
import string
#from parserFuzzer import userNameFuzzer
from graphtaintFuzzer import constructHelmStringFuzzer
from myLogger import giveMeLoggingObject
from parser import checkIfWeirdYAML
from scanner import scanForDefaultNamespace
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

#Youssef's Methods
def fuzzCheckIfWeirdYAML():
    for i in range(10):
        fuzz_input = random.choice([
            123,
            3.14,
            None,
            True,
            [],
            {},
            set(),
            ''.join(random.choices(string.printable, k=20))
        ])
        try:
            checkIfWeirdYAML(fuzz_input)
        except Exception as e:
            print(f"[{i}] Exception Caught in checkIfWeirdYAML:\n\t EXCEPTION: {e}")

def fuzzScanForDefaultNamespace():
    for i in range(10):
        fuzz_input = ''.join(random.choices(string.printable, k=15))
        try:
            scanForDefaultNamespace(fuzz_input)
        except Exception as e:
            print(f"[{i}] Exception Caught in scanForDefaultNamespace:\n\t EXCEPTION: {e}")

def formatException(eText):
    print(f"Exception Caught in function checkIfWeirdYAML from parser.py:\n\t EXCEPTION: {eText}")

if __name__=='__main__':
    fuzzer()
    fuzzCheckIfWeirdYAML()
    fuzzScanForDefaultNamespace()

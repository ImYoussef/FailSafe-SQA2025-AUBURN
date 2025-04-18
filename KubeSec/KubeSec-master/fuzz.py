#TODO: import 5 python methods we want to fuzz
from scanner import isValidUserName
import random
import string
from parserFuzzer import userNameFuzzer
from graphtaintFuzzer import constructHelmStringFuzzer

#TODO: implement fuzzer
def fuzzer():
    userNameFuzzer()
    constructHelmStringFuzzer()
    return 0

if __name__=='__main__':
    fuzzer()


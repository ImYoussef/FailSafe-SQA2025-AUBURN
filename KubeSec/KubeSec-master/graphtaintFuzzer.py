from graphtaint import constructHelmString
import random
import string

def constructHelmStringFuzzer():
    #input non tuples
    print("Trying input: 123", constructHelmString(123))
    print("Trying input: test", constructHelmString("test"))
    print("Trying input: None", constructHelmString(None))
    print("Trying input: True", constructHelmString(True))
    print("Trying input: False", constructHelmString(False))
    print("Trying input: ()", constructHelmString(()))
    
    
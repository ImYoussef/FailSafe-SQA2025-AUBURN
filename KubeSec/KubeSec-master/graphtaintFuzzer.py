from graphtaint import constructHelmString, getHelmTemplateContent
import random
import string

def constructHelmStringFuzzer():
    #input non tuples
    print("Fuzzing constructHelmString() from graphtaint.py")
    print("Trying input: 123", constructHelmString(123))
    print("Trying input: test", constructHelmString("test"))
    print("Trying input: None", constructHelmString(None))
    print("Trying input: True", constructHelmString(True))
    print("Trying input: False", constructHelmString(False))
    print("Trying input: ()", constructHelmString(()))
    
def getHelmTemplateContentFuzzer():
    print("Fuzzing getHelmTemplateContent() from graphtaint.py")
    print("Trying bad file path", getHelmTemplateContent("not/a/file"))
    print("Trying non-file path", getHelmTemplateContent("not-a-file"))

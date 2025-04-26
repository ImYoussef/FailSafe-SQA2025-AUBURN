#TODO: import 5 python methods we want to fuzz
from scanner import isValidUserName
import random
import string
from constants import (
    FORBIDDEN_USER_NAMES,
    SECRET_USER_LIST,
    SECRET_PASSWORD_LIST,
    FORBIDDEN_PASS_NAMES,
    INVALID_SECRET_CONFIG_VALUES,
    LEGIT_KEY_NAMES,
    VALID_KEY_STRING
)

#parser.py | getValsFromKey()
#def getValsFromKey(dict_, target, list_holder  ):
   # '''
   # If you give a key, then this function gets the corresponding values 
   # Multiple values are returned if there are keys with the same name  
   # '''    
   # if ( isinstance( dict_, dict ) ):
   #     for key, value in dict_.items():
   #         # print( key, len(key) , target, len( target ), value  )
   #         if key == target:
   #             list_holder.append( value )
   #         else: 
   #             if isinstance(value, dict):
   #                 getValsFromKey(value, target, list_holder)
   #             elif isinstance(value, list):
   #                 for ls in value:
   #                     getValsFromKey(ls, target, list_holder)

#Fuzzer for isValidUserName()
def userNameFuzzer():
    #Test data using constants
    forbidden_usernames = FORBIDDEN_USER_NAMES
    secret_user_list = SECRET_USER_LIST
    secret_password_list = SECRET_PASSWORD_LIST
    forbidden_pass_names = FORBIDDEN_PASS_NAMES

    #Generate variations of forbidden usernames
    forbidden_variations = []
    for name in forbidden_usernames:
        forbidden_variations.extend([
            name.upper(),
            name.lower(),
            name.capitalize(),  
        ])
    
    #Generate random variations of forbidden usernames
    # Specific test strings with non-ASCII characters
    SPECIFIC_TEST_STRINGS = [
        "usér\u0301name",  # Username with acute accent (é)
        "user\u4F60\u597D",  # Username with Chinese characters (你好)
        "user\u1F600name",  # Username with emoji (😀)
        "user\u200Bname",  # Username with zero-width space
        "user\u0300\u0301name"  # Username with combining accents
    ]
    
    for i in forbidden_usernames:
        print("Trying input: ", i)
        res = isValidUserName(i)

    for i in secret_user_list:
        print("Trying input: ", i)
        res = isValidUserName(i)

    for i in secret_password_list:
        print("Trying input: ", i)
        res = isValidUserName(i)
    
    for i in forbidden_pass_names:
        print("Trying input: ", i)
        res = isValidUserName(i)

    for i in SPECIFIC_TEST_STRINGS:
        print("Trying input: ", i)
        res = isValidUserName(i)
    # Create a string that contains a null byte
    crash_input = "user\0name"
    print("Trying input with null byte: ", crash_input)
    res = isValidUserName(crash_input)
    # Create a string containing all possible byte values (0-255)
    all_bytes = bytes(range(256)).decode('latin1', errors='ignore') 
    print("Trying input with all possible byte values: ", all_bytes)
    res = isValidUserName(all_bytes)
    

    return res

-e 
# Automated Comment

'''
handy tools to enhance lyx orignal CAS support
'''
import sys
from math_client_configure import *

import socket


import re


def parse_expr(expr):
    '''a simple backend to add some map'''
    for i in mapping_list:
        expr = expr.replace(i[0], i[1])
    with open(HISTORY_FILES[MATH_TYPE], "a") as f:
        f.write(expr)

    return expr

import pickle
import os
def main_run():
    global MATH_TYPE
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if(os.path.isfile(CONFIGURATION_FILE)):
        with open(CONFIGURATION_FILE,"rb") as f:
            MATH_TYPE=pickle.load(f)
    else:
        MATH_TYPE = 0
        with open(CONFIGURATION_FILE,"wb") as f:
            pickle.dump(MATH_TYPE,f)
    expression = sys.stdin.read()
    '''add support to remove automatically apply TeXForm, as it is buggy for new freature like machine learning'''
    expression = expression[8:-2]
    expression = parse_expr(expression)
    if("=" not in expression):
        expression=expression+"//TeXForm"
    else:
        expression=expression+";"
    if("$0" in expression):
        result="->0"
        MATH_TYPE=0
    elif("$1" in expression):
        result="->1"
        MATH_TYPE=1
    else:
        s.connect((HOST[MATH_TYPE], PORT[MATH_TYPE]))
        s.send(expression.encode())
        result = s.recv(1024).decode()
        s.close()

    if(result=="None"):
        result="."

    with open(CONFIGURATION_FILE,"wb") as f:
        pickle.dump(MATH_TYPE,f)
    print(template % (MATH_NAME[MATH_TYPE],expression, result))
    
        

if __name__ == "__main__":
    main_run()

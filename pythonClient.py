import sys
import socket
import pythonServerConfigure as psc
import socketServerUtils as ssu
import re
import os.path
import mathServerConfigure as msc

file_temp = "/home/chengzhengqian/pythonclient.py"
transformRules ={"!t":"//TeXForm","D":"\[CapitalDelta]"}

def runTransform(code):
    '''transform a string to another according to transformRules '''
    if code in transformRules:
        return transformRules[code]
    else:
        return code
    

def runMathCode(code, backend=0):
    '''
    string->int->IO()
    '''
    HOST = msc.HOST
    PORT = msc.PORT[backend]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    ssu.send(s,code)
    result = ssu.receive(s)
    s.close()
    return result


'''
backend=0 sage
backend=1 python3

'''
    
def runCode(code, backend=1):
    ''' 
    string->IO (string)
    '''

    HOST = psc.HOST
    PORT = psc.PORT[backend]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    with open(file_temp, "w+") as f:
        f.write(code)
    if(backend == 1):
        '''python'''
        ssu.send(s, ("exec(open(\"{0}\").read(),globals())".format(file_temp)))
    if(backend == 0):
        '''sage'''
        ssu.send(s, ("execfile(\"{0}\")".format(file_temp)))
    result = ssu.receive(s)
    s.close()
    return result

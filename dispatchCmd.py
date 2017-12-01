import re
import lyxFunc  as lfc
import threading
import pythonClient as pclt

NOTIFY_PATTERN = "NOTIFY:(.*)\n"
NOTIFY_RE = re.compile(NOTIFY_PATTERN)
MATH_PATTERN="In\\[\\d*\\]:=([\s\S]*)"
MATH_RE=re.compile(MATH_PATTERN)

class dispatchCmd (threading.Thread):
    '''
    string-> Thread ()
    '''
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd=cmd
    def run(self):
        m = NOTIFY_RE.search(self.cmd)
        if(m):
            keyPressed=m.group(1)
            print(keyPressed)
            code=lfc.getClipboard().decode()
            print("get:",code)
            serverName=""
            '''
            *********
            Add these entries to customize your key bindings.
            *********
            '''
            if(keyPressed=="Ctrl+C R"):
                result=pclt.runCode(code,1)
                serverName="python"
            if(keyPressed=="Ctrl+C S"):
                result=pclt.runCode(code,0)
                serverName="sage"
            if(keyPressed=="Ctrl+C M"):
                result=pclt.runMathCode(code,0)
                serverName="math"
                # math_m=MATH_RE.search(result)
                # if(math_m):
                #     result=math_m.group(1)
            if(keyPressed=="Ctrl+C T"):
                serverName="transform:"
                result=pclt.runTransform(code)
                lfc.insertString(result)

            print(serverName, result)
            lfc.lineEnd()
            lfc.pasteToClipboard(result)
            lfc.message(serverName+":"+result)
        else:
            print(self.cmd)


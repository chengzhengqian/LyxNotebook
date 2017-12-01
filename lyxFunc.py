import subprocess

def getClipboard():
    '''IO(string)'''
    xsel = ('xsel', '-o', '--clipboard')
    ps = subprocess.Popen(xsel, stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    return ps.stdout.read()

def pasteToClipboard(content):
    '''
    string->IO()
    '''
    xsel = ('xsel', '-i', '--clipboard')
    ps = subprocess.Popen(xsel, stdin=subprocess.PIPE)
    ps.stdin.write(content.encode())
    ps.stdin.close()
    ps.wait()

FIFO_LYX_IN = '/home/chengzhengqian/.lyxpipe.in'
LYX_CMD_FORMAT = '"LYXCMD:lyxFunc:{0}:{1}"'


def runLyxFunction(action, args):
    '''
    string->string->IO()
    '''
    cmd = "echo " + LYX_CMD_FORMAT.format(action, args) + " > " + FIFO_LYX_IN
    print("exec:", cmd)
    subprocess.Popen(["bash", '-c', cmd])


def insetEnd():
    '''
    IO()
    '''
    runLyxFunction("inset-end", '')

def lineEnd():
    '''
    IO()
    '''
    runLyxFunction("line-end", '')

def charForward():
    runLyxFunction("char-forward",'')

def charBackward():
    runLyxFunction("char-backward",'')

def listingInsert():
    runLyxFunction("listing-insert",'')

def copy():
    runLyxFunction("copy",'')

def paste():
    runLyxFunction("paste",'')

def insertString(content):
    runLyxFunction("self-insert",content)
    
def message(msg):
    runLyxFunction("message",msg)

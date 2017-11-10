import os
import dispatchCmd as dpc


FIFO_LYX='/home/chengzhengqian/.lyxpipe.out'

def listen(fifo, func_thread):
    '''listen a given named pipe continously
    listen:IO()
    fifo: string
    func_dispatch: string->Thread()
    '''
    while True:
        with open(fifo) as f:
            while True:
                command=f.readline()
                if len(command)==0:
                    print("pipe closed\n")
                    break
                else:
                    dispatchThread=func_thread(command)
                    dispatchThread.start()
        print("--------------------------")

if __name__=="__main__":
    listen(FIFO_LYX,dpc.dispatchCmd)
    

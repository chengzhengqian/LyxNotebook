import socket
from subprocess import Popen, PIPE
import time
from mathServerConfigure import *
from socketServerUtils import *
import _thread as thread
import sys
import re
import fcntl
import os

s = False
process = False
backend = 0


def validate_ouput(text):
    '''check whether output is complete'''
    pattern = re.compile(VALIDATE_OUTPUT_PATTERN[backend])
    if pattern.search(text):
        # print("complete")
        return True
    else:
        return False


def read_from_process(p, N_times=100):
    '''if there is no further output for 100*0.05=5 sec, automatically stop, this is useful when some command taking too long and block lyx'''
    is_continue = True
    is_running = False
    output = ""
    # print("read")
    times = 0
    while is_continue:
        try:
            d = p.stdout.read()
            if d:
                output += DECODE(d)
                # print(output)
                times = 0
        except IOError:
            print("IOError!")
            is_continue = False
        if validate_ouput(output):
            is_continue = False
        times += 1
        time.sleep(0.05)
        if(times > N_times):
            print("Time out! read_from_process will return ")
            print("---->%s<-----" % output)
            break
    return output


def extract_result(result):
    '''extract the result, it seems that regular expression sometimes breaks down'''
    # returns = backend_dependent_preprocessing(returns)

    # p = re.compile(EXTRACT_RESULTS_FOR_REMOTE[backend])
    # s = p.search(returns)
    # if(s):
    #     print_result_for_remote(s.group(1))
    #     return s.group(1)
    # else:
    #     print("result:", returns, "no match!")
    #     return "None"
    for rule in RESULT_FILTERS:
        result = re.sub(rule[0], rule[1], result)
    print_result_for_remote(result)
    return result


def backend_dependent_preprocessing(returns):
    # if(backend==1):
    #     '''python'''
    #     returns=re.sub("Out\[\d*\]:","", returns)
    return returns


def extract_result_for_terminal(result):
    # '''some backend dependent preprocessing'''
    # returns = backend_dependent_preprocessing(returns)
    # p = re.compile(EXTRACT_RESULTS_FOR_LOCAL[backend])
    # s = p.search(returns)
    # if(s):
    #     return s.group(1)
    # else:
    #     print(returns)
    #     return ""
    for rule in RESULT_FILTERS:
        result = re.sub(rule[0], rule[1], result)
    return result


def print_result_for_remote(content):
    print(content + "\n"+"-" * 20 + "\n>>>")


def extract_info(returns):
    returns = backend_dependent_preprocessing(returns)
    p = re.compile(EXTRACT_RESULTS_FOR_INFO[backend])
    s = p.search(returns)
    if(s):
        print_result_for_remote(s.group(1))
        return " \\text{%s}" % s.group(1)
    else:
        print("Output:", returns, "is not understood!")
        return "None"


def start_kernel():
    global process
    print("start %s" % COMMAND[backend])
    process = Popen(COMMAND[backend], stdin=PIPE, stdout=PIPE)
    fcntl.fcntl(process.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)
    read_from_process(process)
    '''write some intial command here'''
    process.stdin.write(ENCODE("\n"))
    process.stdin.flush()
    read_from_process(process)


def listen(backend=0):
    global s, process
    print("listen")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT[backend]))
    s.listen(5)

    start_kernel()
    
    while True:
        conn, addr = s.accept()
        content = receive(conn)
        print("\n" + "-" * 20 + "\n%s" % (content) + "\n" + "=" * 20)
        content = content + "\n"
        process.stdin.write(ENCODE(content))
        process.stdin.flush()
        send_content = read_from_process(process)
        # if(re.search("\?", content)):
        #     send_content = extract_info(send_content)
        # else:
        #     send_content = extract_result(send_content)
        send(conn, extract_result(send_content))
        conn.close()


def main_run():
    try:
        backend = 0
        if(len(sys.argv) > 1):
            backend = int(sys.argv[1])
            print("Get %s" % COMMAND_NAME[backend])
        thread.start_new_thread(listen, (backend,))

        while True:
            content = input(">>>")
            '''processing special command'''
            if(content == "!k"):
                print("kill the kernel")
                process.kill()
                start_kernel()
            elif(content == "!r"):
                print("read redudande output")
                read_from_process(process)
            else:
                content = content + "\n"
                process.stdin.write(ENCODE(content))
                process.stdin.flush()
                print(extract_result_for_terminal(read_from_process(process)))

    except (KeyboardInterrupt, SystemExit):
        s.close()
        process.kill()

if __name__ == "__main__":
    main_run()

import socket
from pythonServerConfigure import *
from socketServerUtils import *
from sage.all import *
import thread as thread
import rlcompleter
import readline
from cStringIO import StringIO
import sys
'''this is for sage'''
backend = 0


def listen():
    s_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_.bind((HOST, PORT[backend]))
    s_.listen(5)
    print("start %s" % COMMAND_NAME[backend])

    while True:
        conn_, addr_ = s_.accept()
        content_ = receive(conn_)
        print("\n" + "-" * 20 + "\n%s" % (content_) + "\n" + "=" * 20 + "\n")
        try:
            original_stdout = sys.stdout
            sys.stdout = current_stdout = StringIO()
            eval(content_, globals())
            sys.stdout = original_stdout
            result_ = current_stdout.getvalue()

        except Exception as e:
            print(e)
            result_ = "error"
        print(result_ + "\n" + "-" * 20)
        send(conn_, result_)
        conn_.close()


def main_run():
    try:
        thread.start_new_thread(listen, ())
        while True:
            readline.parse_and_bind("tab: complete")
            command = raw_input(">>>")
            try:
                exec(command)
            except Exception as e:
                print(e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main_run()

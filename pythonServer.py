import socket
from pythonServerConfigure import *
from socketServerUtils import *

import _thread as thread
import rlcompleter
import readline
import io
from contextlib import redirect_stdout

'''this is for python3'''
backend = 1


def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT[backend]))
    s.listen(5)
    print("start %s" % COMMAND_NAME[backend])

    while True:
        conn, addr = s.accept()
        content = receive(conn)
        print("\n" + "-" * 20 + "\n%s" % (content) + "\n" + "=" * 20 + "\n")
        try:
            with io.StringIO() as buf, redirect_stdout(buf):
                eval(content, globals())
                result = buf.getvalue()
        except Exception as e:
            print(e)
            result = "error"
        print(result + "\n" + "-" * 20)
        send(conn, result)
        conn.close()


def main_run():
    try:
        thread.start_new_thread(listen, ())
        while True:
            readline.parse_and_bind("tab: complete")
            command = input(">>>")
            try:
                exec(command)
            except Exception as e:
                print(e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main_run()

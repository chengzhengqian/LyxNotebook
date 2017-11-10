'''this improves the previous way for fixed lenght
 by using a given protocal to send '''


def DECODE(obj):
    return obj.decode()


def ENCODE(obj):
    return obj.encode()


def receive(conn):
    len_ = DECODE(conn.recv(64))
    len_s_byte = int(len_)
    conn.send(ENCODE("OK"))
    return DECODE(conn.recv(len_s_byte))


def send(conn, s):
    '''socket->string->IO()'''
    s_byte = ENCODE(s)
    len_s_byte = ENCODE(str(len(s_byte)))
    conn.send(len_s_byte)
    conn.recv(64)
    conn.send(s_byte)

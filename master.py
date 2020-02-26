import os
import threading
import subprocess

def recv():
    while 1:
        res = subprocess.check_output(["head","/dev/ttyS1","-n","1"])
        if res!=b"" and res!=b'\n':
            recv = res.decode("utf-8")[:-1]
            date = subprocess.check_output(["date","+%Y-%m-%d"]).decode("utf-8")[:-1]
            time = subprocess.check_output(["date","+%H:%M:%S"]).decode("utf-8")[:-1]
            print("[RECV",date,time+"]",recv)

def send():
    while 1:
        input_str = input()
        if(input_str!=""):
            os.system("echo "+input_str+" >> /dev/ttyS0")
            date = subprocess.check_output(["date","+%Y-%m-%d"]).decode("utf-8")[:-1]
            time = subprocess.check_output(["date","+%H:%M:%S"]).decode("utf-8")[:-1]
            print("[SEND",date,time+"]",input_str)

S = threading.Thread(target=send, name='sendThread')
R = threading.Thread(target=recv, name='recvThread')
S.start()
R.start()
S.join()
R.join()

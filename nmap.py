import socket
import threading
from queue import Queue

target = "192.168.0.1"
queue = Queue()
openPorts = []

def portScan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False

def fillQ(portList):
    for port in portList:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print("Port {} is open!".format(port))
            openPorts.append(port)

def exploit():
    portList = range(1,500)
    fillQ(portList)
    threadList = []

    for t in range(500):
        thread = threading.Thread(target=worker)
        threadList.append(thread)

    for thread in threadList:
        thread.start()

    for thread in threadList:
        thread.join()

    print("Open port(s) are: ", openPorts)

if __name__ == '__main__':
    exploit()

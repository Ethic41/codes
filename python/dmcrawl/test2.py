import threading
import os

def main():
    threadList = []
    with open(os.getcwd()+"/test1.dmd", "a+") as f:
        thread1 = threading.Thread(target=writer, args=(f,))
        thread2 = threading.Thread(target=reader, args=(f,))
        threadList.append(thread1)
        threadList.append(thread2)

        for thread in threadList:
            thread.start()

        for thread in threadList:
            thread.join()

def writer(f):
    for i in range(10):
        f.write("i am no %s\n"%str(i))

def reader(f):
    for i in range(10):
        text = f.readline().strip("\n")
        print(text)

main()

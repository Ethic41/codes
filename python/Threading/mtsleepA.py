from time import *
import thread

def main():
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)

def loop0():
    print("started 0 at "+ctime()+"\n")
    start_time = time()
    sleep(2)
    print("0 done in: "+str(time() - start_time)+" at "+ctime())

def loop1():
    print("started 1 at "+ctime())
    start_time = time()
    sleep(4)
    print("1 done in: "+str(time() - start_time)+ " at " +ctime())

if __name__=="__main__":
    main()

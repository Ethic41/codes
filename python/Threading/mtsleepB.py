from time import *
import thread

loops = [4,2,3]

def loop(nloop, nsec, lock):
    start_time = time()
    print("loop "+str(nloop)+" started at "+ctime()+"\n")
    sleep(nsec)
    print(str(nloop) +" done in "+str(time() - start_time))
    lock.release()

def main():
    locks = []
    nloop = range(len(loops))

    for i in nloop:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloop:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloop:
        while locks[i].locked():
            pass
    print "done at "+ctime()

if __name__=="__main__":
    main()

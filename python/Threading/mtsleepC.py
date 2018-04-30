from time import time, ctime, sleep
import threading

loops = [4,1,3]
def loop(nloop, nsec):
    start_time = time()
    print("loop "+str(nloop)+" started at "+ctime()+"\n")
    sleep(nsec)
    print(str(nloop)+" done in "+ str(time() - start_time)+"secs")

def main():
    start_time = time()
    threads = []
    nloop = range(len(loops))

    for i in nloop:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloop:
        threads[i].start()

    for i in nloop:
        threads[i].join()

    print "total time taken: "+str(time() - start_time)+"secs"

if __name__ == "__main__":
    main()

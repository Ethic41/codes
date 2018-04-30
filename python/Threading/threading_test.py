from time import time, ctime
import threading
import hashlib

with open("smalldict.txt", "r") as f:
    lines = f.readlines()

def main():
    threads = []
    nthreads = input("Number of threads:\n")
    start_time = time()
    lent = len(lines)
    div = lent/nthreads
    nloop = range(nthreads)

    h = open("hashes_sha1.txt", "a")
    s = 0
    e = div
    for i in nloop:
        t = threading.Thread(target=output, args=(i, (s,e), h))
        s = e
        e += div
        threads.append(t)

    for i in nloop:
        threads[i].start()

    for i in nloop:
        threads[i].join()

    print("finished in "+str(time() - start_time)+"secs")

def output(nt, (s,e), h):
    for i in range(s,e):s
        word = lines[i].strip('\n')
        h.write(hashlib.sha1(word).hexdigest()+"\n")
    print(str(nt)+" done... at "+ctime())



if __name__=="__main__":
    main()

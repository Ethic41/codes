from time import time, ctime
import hashlib
import threading

def main():
    with open("smalldict.txt", "r")as f:
        list = f.readlines()
    with open("sha_1_no.txt", "a")as s:
        start_time = time()
        for i in list:
            word = i.strip("\n")
            t = threading.Thread(target=threads, args=(s, word))
            t.start()
    print("finished in "+str(time() - start_time))

def threads(s, word):
    s.write(hashlib.sha1(word).hexdigest()+"\n")

if __name__=="__main__":
    main()

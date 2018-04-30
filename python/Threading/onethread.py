from time import *
def main():
    start_time = time()
    print("loop started")
    loop0()
    loop1()
    end_time = time()
    print("loop ended total time taken:"+ str(end_time - start_time) + "sec")

def loop0():
    sleep(4)

def loop1():
    sleep(2)

if __name__ == "__main__":
    main()

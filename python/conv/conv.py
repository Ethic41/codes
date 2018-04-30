
def conv():
    try:
        print("Welcome to conv, type 'quit' or 'ctrl-c' to exit:"+"\n")
        ex_rate = input("Enter conversion rate:"+"\n")
        while True:
            cur_val = input("Enter the value:"+"\n")
            if str(type(cur_val))=="<type 'int'>":
                print(cur_val * ex_rate)
            elif str.lower(cur_val) == "quit":
                print "quitting..."
                exit()
            else:
                print("Sir, that's not a number...")
    except KeyboardInterrupt,e:
        print("quittig...")
        exit()
    except NameError,e:
        print 'Incorrect input...'
        exit()
    except Exception,e:
        exit()

if __name__=="__main__":
    conv()

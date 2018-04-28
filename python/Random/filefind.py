import os, time

pri_dir = os.getcwd()

def main():
    try:
        if not os.path.exists("crawled.txt"):
            open("crawled.txt", "w")
        if not os.path.exists("dir.txt"):
            open("dir.txt", "w")
        if not os.path.exists("found.txt"):
            open("found.txt", "w")
        if not os.path.exists("base.txt"):
            open("base.txt", "w")
        with open("base.txt","r")as f:
            base_content = f.readline()
        time_stamp = raw_input("Enter the file time stamp in this format <dd-mm-yy>:"+"\n")
        file_beg = raw_input("Enter optional file begining:"+"\n")
        ff = raw_input("Enter optional file format:"+"\n")
        if base_content == "":
            file_path = raw_input("Please specify a file path to start searching 4rm:"+"\n")
            if os.path.exists(file_path):
                print("Searching...")
                retrieve(file_path,time_stamp,file_beg,ff)
        else:
            while(True):
                req = raw_input("An existing path was found '"+str(base_content).strip("\n")+"'do you want to continue:\n <Yes> or <No> to specify a new path:")
                if str(req).lower() == "yes":
                    print("Searching...")
                    retrieve(file_path, time_stamp, file_beg, ff)
                    break
                elif str(req).lower() == "no":
                    file_path = raw_input("Enter file path:"+"\n")
                    with open("base.txt","w")as b:
                        b.write(str(file_path))
                    print("Searching...")
                    retrieve(file_path, time_stamp, file_beg, ff)
                else:
                    pass
    except WindowsError:
        pass
    except RuntimeError:
        pass
    print("Done...")


def retrieve(file_path, time_stamp, file_beg="", ff=""):
    try:
        os.chdir(file_path)
        dir_list = os.listdir(os.getcwd())
        for dir in dir_list:
            dir = dir.strip("\n")
            if os.path.isdir(dir) and dir[:1]!=".":
                with open(pri_dir+"\\dir.txt","a")as f:
                    f.write(os.getcwd()+"\\"+dir+"\n")
            elif os.path.isfile(dir) and dir[:len(file_beg)]==file_beg and dir[-len(ff):]==ff:
                file_time = os.path.getmtime(dir)
                file_time_stamp = time.strftime("%d-%m-%y", time.gmtime(file_time))
                if time_stamp == file_time_stamp:
                    with open(pri_dir+"\\found.txt", "a") as a:
                        a.write(os.getcwd()+"\\"+dir+"\n")
                        print("Found match at: "+os.getcwd()+"\\"+dir)
        with open(pri_dir+"\\crawled.txt","a")as c:
            c.write(file_path+"\n")
        recurse(pri_dir, time_stamp, file_beg, ff)
    except WindowsError:
        pass
    except RuntimeError:
        pass

def recurse(pri_dir,time_stamp, file_beg="", ff=""):
    try:
        with open(pri_dir+"\\dir.txt", "r")as f:
            content = f.readlines()
            for dir in content:
                with open(pri_dir+"\\crawled.txt", "r")as c:
                    crawl_cont = c.readlines()
                if dir not in crawl_cont:
                    file_path = dir.strip("\n")
                    retrieve(file_path, time_stamp, file_beg, ff)
    except WindowsError:
        pass
    except RuntimeError:
        pass




def error(e):
	print("Error: "+str(e))
	print("Initiating Forceful shutdown...")

if __name__ == "__main__":
    main()

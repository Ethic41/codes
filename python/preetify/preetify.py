import os
from bs4 import BeautifulSoup as bs
import logging
import chromalog
from chromalog.mark.helpers.simple import error as red
from chromalog.mark.helpers.simple import warning as warn
from chromalog.mark.helpers.simple import success
from validate_filename import validate

chromalog.basicConfig(format="%(message)s", level=logging.INFO)
log = logging.getLogger()

def main():
    try:
        log.info("%s", success(
            """
                ##############>>>>>>>>>>^^<<<<<<<<<<##############
                #               ***Preetify***                   #
                #                 By Ethical                     #
                #                July 16th, 2017                 #
                #    This Script uses the bs4's BeautifulSoup    #
                #    preetify function to clean a html file      #
                ##############>>>>>>>>>>^^<<<<<<<<<<##############
               """))
        req()
    except KeyboardInterrupt:
        log.info("%s", warn("Going to shutdown..."+"\n"))
    except Exception, e:
        log.info("%s", warn(e + ": Shutting down..."+"\n"))

def req():
    try:
        dir = raw_input("Enter the directory of the file you want to clean:"+"\n")
        os.chdir(dir)
        file_list = []
        for file in os.listdir(os.getcwd()):
            if os.path.isfile(file) and file[-5:] == ".html":
                file_list.append(file)
        while True:
            try:
                preety(file_list)
            except Exception, e:
                error(e)
    except Exception, e:
        error(e)

def preety(file_list):
    try:
        if not os.path.exists(os.getcwd()+r"/pretty"):
            os.mkdir("pretty")
        for file in file_list:
            with open(file, "r") as fp:
                soup = bs(fp, 'html.parser')
                clean_file = soup.prettify("utf-8")
                os.chdir("pretty")
            with open(file, "w") as f:
                f.write(clean_file)
                os.chdir("..")
        log.info("%s", success("\n"+"Files have been successfully cleaned...exiting..."+"\n"))
        exit()
    except IndexError:
        log.info("%s", red("\n"+"at least on of the file numbers you picked is Incorrect...check your inputs..."))
    except Exception,e:
        error(e)

def error(e):
	log.info("%s", warn("\n"+"Error: "+str(e)))
	log.info("%s",warn("\n"+"Initiating Forceful shutdown..."))

if __name__=="__main__":
    main()

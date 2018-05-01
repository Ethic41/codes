#CodeName: init.py
#Author: Dahir Muhammad Dahir
#Date: 1st-May-2018
#About: this script will initialize my
#       python projects in the format i specify


import os

thisDir = os.getcwd()


def main():
    projectName = raw_input("Specify project name:\n")
    if not os.path.exists(thisDir+"/%s"%(projectName)):
        os.mkdir(thisDir+"/%s"%(projectName))
        with open(thisDir+"/%s/%s.py"%(projectName, projectName), "a") as f:
            f.write("#CodeName: \n#Author: \n#Date: \n#About: \n\n\n\n\ndef main():%sif __name__ == '__main__':\n\tmain()"%(10*"\n"))

        with open(thisDir+"/%s/test.py"%projectName, "a") as f:
            pass
        with open(thisDir+"/%s/%s.dmd"%(projectName, projectName), "a") as f:
            f.write("#test")
    else:
        print("path already exist...")


if __name__ == '__main__':
    main()

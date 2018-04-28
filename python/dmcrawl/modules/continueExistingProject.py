#Module_Name: continueExistingProject
#Author: Dahir Muhammad Dahir
#Date: 27-February-2018
#About: this module allows us to continues existing projects that have
#       not yet been completed.

from showUncompletedProject import showUncompletedProject
from crawler import initCrawler

def continueExistingProject(): #ask the user to choose which project to continue
    uncompletedProjectList = showUncompletedProject()
    for project in uncompletedProjectList:
        print("\n{%d} ==> %s\n"%(uncompletedProjectList.index(project)+1, project))
    selectProject = raw_input("choose from [1 - %d] [only one selection is allowed]\n\n"%len(uncompletedProjectList))
    if selectProject:
        selectedProject = uncompletedProjectList[int(selectProject)-1]
        initCrawler(contProject=True, projectName=selectedProject)
    else:
        print("Invalid choice")







if __name__ == "__main__":
    continueExistingProject()

#Module_Name: updateExistingProject
#Author: Dahir Muhammad Dahir
#Date: 27-February-2018
#About: this module update Existing project that has been completed but now has
#       a new update
import os
from showCompletedProject import showCompletedProject
from crawler import initCrawler

thisDir = os.getcwd() #i will be calling this alot
projectDir = thisDir+"/projects/" #same as above

def updateExistingProject():
    completedProjectList = showCompletedProject()
    for project in completedProjectList:
        print("\n{%d} ==> %s\n"%(completedProjectList.index(project)+1, project))
    selectProject = raw_input("choose from [1 - %d] [only one selection is allowed]\n\n"%len(completedProjectList))
    if selectProject:
        selectedProject = completedProjectList[int(selectProject)-1]
        initCrawler(update=True, projectName=selectedProject)
    else:
        print("Invalid choice")



if __name__ == "__main__":
    updateExistingProject()

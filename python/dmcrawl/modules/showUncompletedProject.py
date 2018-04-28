#Module_Name: showUncompletedProject
#Author: Dahir Muhammad Dahir
#Date: 27-February-2018
#About: contain all the funtions to show uncompleted projects
import os

thisDir = os.getcwd() #i will be calling this alot
projectDir = thisDir+"/projects/" #same as above

def showUncompletedProject(listOnly=""): #if listOnly is set to true when function is called den just list
    directoryList = os.listdir(projectDir)
    uncompletedProject = []
    for directory in directoryList:
        with open(projectDir+directory+"/status.dmd", "r") as f:
            status = f.readline().strip("\n")
        if status == "unfinished":
            uncompletedProject.append(directory)
    if not listOnly:
        return uncompletedProject
    else:
        for project in uncompletedProject:
            print("\n\n{#} ==> %s\n"%project)
        print("Summary: %d Unfinished projects"%len(uncompletedProject))



if __name__ == "__main__":
    showUncompletedProject()

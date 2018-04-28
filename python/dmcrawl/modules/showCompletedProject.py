#Module_Name: showCompletedProject
#Author: Dahir Muhammad Dahir
#Date: 27-February-2018
#About: this module shows the completed projects

import os

thisDir = os.getcwd() #i will be calling this alot
projectDir = thisDir+"/projects/" #same as above



def showCompletedProject(listOnly=""): #if listOnly is set to true when function is called den just list
    directoryList = os.listdir(projectDir)
    completedProject = []
    for directory in directoryList:
        with open(projectDir+directory+"/status.dmd", "r") as f:
            status = f.readline().strip("\n")
        if status == "finished":
            completedProject.append(directory)
    if not listOnly:
        return completedProject
    else:
        for project in completedProject:
            print("\n\n{#} ==> %s\n"%project)
        print("Summary: %d completed"%len(completedProject))



if __name__ == "__main__":
    main()

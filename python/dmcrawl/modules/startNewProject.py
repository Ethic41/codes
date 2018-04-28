#Module_Name: startNewProject
#Author: Dahir Muhammad Dahir
#Date: 27-February-2018
#About: start a new project or task
import os
from crawler import initCrawler

thisDir = os.getcwd() #i will be calling this alot
projectDir = thisDir+"/projects/" #same as above
extDir = thisDir+"/extensions/" #same as above


#start new project function, in charge of creating the project directory and initilizing the projects files

def startNewProject():
    projectName = raw_input("\n\nEnter a name for your new project [it will be created within the projects folder]:\n")
    if not os.path.isdir(thisDir+"/projects"): #initialize the projects folder if it does not exist
        os.mkdir(thisDir+"/projects")
    if projectName: #checking if a valid name is specified
        if not os.path.isdir(projectDir+projectName):
            os.mkdir(projectDir+projectName)
            with open(projectDir+projectName+"/status.dmd", "w") as f:
                f.write("unfinished")
            print("project '%s' has been created"%projectName)
            projectType = raw_input("""
Select a Project type:\n
{1} ==> Get files only [get only the file extension specified]
{2} ==> Mirror a Site [mirror a complete site]\n\n"""
            )
            if projectType == "1":
                getFilesOnly(projectName)
            elif projectType == "2":
                mirrorSite(projectName)
        else:
            print("'%s' project already exist."%projectName)
    else:
        print("\nInvalid project Name.")

def getFilesOnly():
    if not os.path.isdir(extDir): #create the extension directory if it does not exist
        os.mkdir(thisDir+"extensions")
        print("\nextensions directory has been created.\n")

    if not os.path.isfile(extDir+"extensions.dmd"): #same as above, for the extension file
        with open(extDir+"extensions.dmd", "w") as f:
            pass

    with open(extDir+"extensions.dmd", "r") as f: #we open the extension file for reading available extensions
        extensions = []
        extensionsRead = f.readlines()
        for extension in extensionsRead: #we are stripping the newline character here
            extension = extension.strip("\n")
            extensions.append(extension)

    if extensions:
        for extension in extensions:
            print("{%d} ==> %s" %(extensions.index(extension)+1, extension)) #print a numbered form of the extensions
        selectExtension = raw_input("\nChoose from [1 - %s], you can choose multiple extensions e.g 1,2,3:\n"%len(extensions))
        if selectExtension: #if an extension has been selected add it to selectedExtensions list
            selectedExtensions = []
            selectExtension = selectExtension.split(",")
            for selection in selectExtension:
                extension = extensions[int(selection)-1]
                selectedExtensions.append(extension)
            initCrawler(getFilesOnly=True, extensions=selectedExtensions, projectName=projectName)
        else:
            print("Invalid Selection...")
    else:
        print("'extensions.dmd' file is empty, please add your own extensions...")




def mirrorSite():
    initCrawler(mirrorSite=True, projectName=projectName)


if __name__ == "main":
    startNewProject()

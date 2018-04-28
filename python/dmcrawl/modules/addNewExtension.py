#Module_Name: addNewExtension
#Author: Dahir Muhammad Dahir
#Date: 27-February-2018
#About: this module allows us to add new file extensions to our record
import os

thisDir = os.getcwd() #i will be calling this alot
projectDir = thisDir+"/projects/" #same as above
extDir = thisDir+"/extensions/" #same as above

def addNewExtension():
    if not os.path.isdir(extDir): #create the extension directory if it does not exist
        os.mkdir(thisDir+"extensions")
        print("\nextensions directory has been created.\n")

    if not os.path.isfile(extDir+"extensions.dmd"): #same as above, for the extension file
        with open(extDir+"extensions.dmd", "w") as f:
            pass
    savedExtensions = [] #this list holds the extensions that already exist in the extension file
    with open(extDir+"extensions.dmd", "r") as f:
        extensions = f.readlines()
    for extension in extensions:
        extension = extension.strip("\n")
        savedExtensions.append(extension)

    newExtension = raw_input("Enter the new extension [comma seperated for multiple]:\n\n")
    if newExtension:
        newExtension = newExtension.split(",")
        with open(extDir+"extensions.dmd", "a") as f:
            for extension in newExtension:
                extension = extension.replace(" ", "")
                if extension in savedExtensions:
                    print("\n%s already exist it will not be written."%extension)
                else:
                    f.write(extension+"\n")
        print("\n\nExtensions were added successfully...")
    else:
        print("invalid input")


if __name__ == "__main__":
    addNewExtension()

#Module_Name: initProject
#Author: Dahir Muhammad Dahir
#Date: 27-February-2018
#About: this module initialize the projects, allows the user
#       to choose what the want to do.

from startNewProject import startNewProject
from continueExistingProject import continueExistingProject
from updateExistingProject import updateExistingProject
from addNewExtension import addNewExtension
from showCompletedProject import showCompletedProject
from showUncompletedProject import showUncompletedProject

def start():
    print("""
                {#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}
                {#}                                                         {#}
                {#}              <======:: DMCRAWL ::=======>               {#}
                {#}                                                         {#}
                {#}  <=======::  Author: Dahir Muhammad Dahir  ::=======>   {#}
                {#}         <=======:: 27th-February-2018::========>        {#}
                {#} <===:: spider:crawl:download || whatever u want ::===>  {#}
                {#}                                                         {#}
                {#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}{#}
    """
    )
    task = raw_input(
    """
{1} ==> Start a new Project
{2} ==> Continue Existing Project [Unfinished]
{3} ==> Updating Existing project
{4} ==> Add new file extension
{5} ==> Show completed projects
{6} ==> Show Uncompleted projects
{7} ==> Exit

What do you want to do? Choose [1 - 7]\n""")
    if task == "1":
        startNewProject()
    elif task == "2":
        continueExistingProject()
    elif task == "3":
        updateExistingProject()
    elif task == "4":
        addNewExtension()
    elif task == "5":
        showCompletedProject(listOnly=True)
    elif task == "6":
        showUncompletedProject(listOnly=True)
    elif task == "7":
        exit()
    else:
        print("Invalid Entry, please choose from option [1 - 7]")
















if __name__=="__main__":
    start()

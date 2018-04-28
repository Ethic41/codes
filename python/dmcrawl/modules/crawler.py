#Module_Name: crawler
#Author: Dahir Muhammad Dahir
#Date: 28-February-2018
#About: the main bad guy
import os
from bs4 import BeautifulSoup as bs
import requests

thisDir = os.getcwd() #i will be calling this alot
projectDir = thisDir+"/projects/" #same as above
extDir = thisDir+"/extensions/" #same as above

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}


def initCrawler(getFilesOnly="", mirrorSite="", contProject="", update="", extensions="", projectName=""):
    if !(contProject) and !(update):
        address = raw_input("enter the address you want to crawl:\n\n")
        if address:
            with open(projectDir+projectName+"/startAddress.dmd") as f:
                f.write(address)
            if getFilesOnly:
                with open(projectDir+projectName+"/projType.dmd", "w") as f:
                    f.write("getFilesOnly")
                if extensions:
                    with open(projectDir+projectName+"/validExtension.dmd", "a") as f:
                        for extension in extensions:
                            f.write(extension+"\n")
            elif mirrorSite:
                with open(projectDir+projectName+"/projType.dmd", "w") as f:
                    f.write("mirrorSite")
            crawler(projectName, new=True)
        else:
            print("\nInvalid address supplied, please supply a valid address.\n")

    elif contProject:
        crawler(projectName, cont=True)

    elif update:
        crawler(projectName, update=True)

def crawler(projectName, new="", cont="", update=""):
    if new:
        if not os.path.isfile(projectDir+projectName+"/linksToCrawl.dmd"):
            with open(projectDir+projectName+"/linksToCrawl.dmd", "w") as f:
                with open(projectDir+projectName+"/startAddress.dmd", "r") as x:
                    address = x.readline()
                f.write(address+"\n")
    elif update:
        address = raw_input("provide a link to start the update from:\n\n")
        with open(projectDir+projectName+"/linksToCrawl.dmd", "w") as f:
            f.write(address+"\n")

    while(True):
        with open(projectDir+projectName+"/linksToCrawl.dmd", "r") as f:
            addresses = f.readlines()

        with open(projectDir+projectName+"/projectType.dmd", "r") as f:
            projectType = f.readline()
        if addresses:
            for address in addresses:
                address = address.strip("\n")
                links = linkRetriever(address)
                validExtension = []
                if projectType == "getFilesOnly":
                    with open(projectDir+projectName+"/validExtension.dmd", "r") as f:
                        extensions = f.readlines()
                    for extension in extensions:
                        extension = exetension.strip("\n")
                        validExtension.append(extension)
                    linksFilter(links, validExtension, projectName)
                elif projectType == "mirrorSite":
                    linksFilter(links, validExtension="", projectName)
        else:
            print("Done. No more links to crawl")


def linkRetriever(address):
    linksList = []
    with requests.Session() as s:
        page = s.get(address, headers=headers)
        page = page.content

    soup = bs(str(page), 'html.parser')
    cleanSoup = soup.prettify("utf-8")
    soup = bs(cleanSoup, "html.parser")
    links = soup.find_all("a", attrs={"href":True})
    for link in links:
        linkSoup = bs(str(link), "html.parser")
        link = (linkSoup.a["href"]).encode("utf8")
        linksList.append(link)
    return linksList


def linksFilter(links, validExtension="", projectName):
    validSubLinks = []
    links = validateDomain(links, projectName)
    if links:
        if validExtension:
            for link in links:
                for extension in exetensions:
                    if link.endswith(extension):
                        getFile(link, projectName)
                        



def validateDomain(link, projectName):
    validLinks = []
    with open(projectDir+projectName+"/startAddress.dmd", "r")as f:
        validDomain = f.readline()
    for link in links:
        link = link.strip("\n").strip(" ")
        if link[:len(validDomain)] == validDomain:
            validLinks.append(link)
    return validLinks


















if __name__ == "__main__":
    crawler()

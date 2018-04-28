from bs4 import BeautifulSoup as bs
import os
import threading
import requests
import random


host = "http://index-of.co.uk/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
"""
with requests.Session() as s:
    page = s.get("http://index-of.co.uk/ASP/", headers=headers)

soup = bs(str(page.content), "html.parser")
clean = soup.prettify("utf-8")

#with open(os.getcwd()+"/ASP.html", "r") as f:
#    page = f.readlines()

#soup = bs(open(os.getcwd()+"/home.html", "r"), "html.parser")
#clean = soup.prettify("utf-8")
with open(os.getcwd()+"/ASP.html", "w") as f:
    f.write(clean)


def link_is_file(link):
    if link[:4] == "http":
        return False
    elif link[-1] == "/":
        return False
    elif not link[0].isupper():
        return False
    else:
        return True


soup = bs(open(os.getcwd()+"/ASP.html", "r"), "html.parser")
a_tags = soup.find_all("a")
for a in a_tags:
    link = a["href"]
    if link_is_file(link):
        print link


#soup = bs(str(a_tags), "html.parser")
#print(soup.a["href"])
"""
def main():
    a = one()
    print("Done at main")

def one():
    threads_list = []
    for i in range(3):
        new_thread = threading.Thread(target=two, args=([3]))
        threads_list.append(new_thread)
    for thread in threads_list:
        thread.start()
    for thread in threads_list:
        thread.join()
    print "Done"


def two(num):
    vals = []
    for x in range(num):
        vals.append(x)
    print vals


if __name__ == "__main__":
    main()

from bs4 import BeautifulSoup as bs
import os
import threading
import requests

host = "http://index-of.co.uk/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}


def main():
    site_dir_list = get_site_dir_list() #get the directory link from the site to cmpre incase there is new
    create_threads(site_dir_list)

def create_threads(dir_link):
    with open(os.getcwd()+"/retrieved_dir.dmd", "r") as f: # open the retrieved dirs file and read the content
        retrieved = f.readlines()

    with open(os.getcwd()+"/dirs.dmd", "r") as f: # open the dirs.dmd file and read the content
        dir_links = f.readlines()

    for link in retrieved: # remove any dir that has alreay been retrieved completely
        if link in dir_links:
            dir_links.remove(link)

    while dir_links != []:
        if not os.path.isfile(os.getcwd()+"/links.dmd"): # check if the links.dmd file exist [keep track of the time]
            with open(os.getcwd()+"/links.dmd", "w") as f:
                pass
            retrieved_links = []
        else:
            with open(os.getcwd()+"/links.dmd", "r") as f: # it exist so opening it for reading
                retrieved_links = f.readlines()
        threads_list = []
        for _ in range(10):
            if dir_links != []:
                new_thread = threading.Thread(target=get_links, args=(dir_links[-1].strip("\n"), retrieved_links))
                threads_list.append(new_thread)
                print("trying to remove %s \n"%dir_links[-1])
                dir_links.remove(dir_links[-1])
                print("new length of list is %d \n"%len(dir_links))
            else:
                print("Exhausted directory links")
        if threads_list != []: #confirms that threads list is not empty
            for thread in threads_list:
                thread.start()
            for thread in threads_list:
                thread.join()
        else:
            print("Exhausted Threads list")
        if new_links != []:
            with open(os.getcwd()+"/links.dmd", "a") as f: #we are updating the retrieved links file
                for link in new_links:
                    f.write(link+"\n")
                    print("wrote new links")
        if retrieved_dirs != []:
            with open(os.getcwd()+"/retrieved_dir.dmd", "a") as f:
                for dir in retrieved_dirs:
                    f.write(dir+"\n")


def get_links(dir_link):
    with requests.Session() as s:
        page = s.get(host+"/"+dir_link, headers=headers) #open the page of the current directory
    if not os.path.isdir(os.getcwd()+"/"+dir_link): #check if the directory has not been created
        os.mkdir(os.getcwd()+"/"+dir_link)  # create the directory
    files_link = get_files_link(page.content) # call the function that retrieve and returns the links
    with requests.Session() as s:
        for link in files_link:
            file_name = validate_filename(link)
            if not os.path.isfile(os.getcwd()+"/"+dir_link+file_name):
                link = link.strip("\n")
                print("trying to retrieve %s from %s \n"%(file_name, dir_link))
                file_get = s.get(host+"/"+dir_link+link, headers=headers)
                with open(os.getcwd()+"/"+dir_link+file_name, "wb") as f:
                    f.write(file_get.content)
                print("Retrieved %s \n"%file_name)


def validate_filename(link):
    name = link.replace("%20", "_")
    return name


def get_files_link(page):
    links = []
    soup = bs(str(page), "html.parser")
    a_tags = soup.find_all("a")
    for a in a_tags:
        link = a["href"]
        if link_is_file(link):
            links.append(link)
    return links


def link_is_file(link):
    if link[:4] == "http":
        return False
    elif link[-1] == "/":
        return False
    elif not link[0].isupper():
        return False
    else:
        return True


def get_dir_list():
    with open(os.getcwd()+"/dirs.dmd", "r") as f: #if u can't read this, it's not meant 4 u
        dir_list = f.readlines()
        return dir_list

#this function retrieve the link of dirs from the site
def get_site_dir_list():
    links = []
    with requests.Session() as s:
        open_homepage = s.get(host, headers=headers) #opening the homepage of the site
    homepage = open_homepage.content # this is trivial
    soup = bs(str(homepage), "html.parser")
    a_tags = soup.find_all("a")
    all_links = []
    for a in a_tags:
        link = a["href"] #extracting the link text with bs
        all_links.append(link)
    for link in all_links:
        if is_link_dir(link):
            links.append(link)
    return links

# performs simple checks if don't get this too, this code is not for u
def is_link_dir(link):
    if link[:4] == "http":
        return False
    elif link[-1] != "/":
        return False
    elif not link[0].isupper():
        return False
    else:
        return True
if __name__=="__main__":
    main()
"""

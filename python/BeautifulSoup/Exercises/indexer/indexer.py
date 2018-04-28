from bs4 import BeautifulSoup as bs
import os
import threading
import requests
from time import sleep, ctime

host = "http://index-of.co.uk/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"} # spoofed user agent

fully_retrieved_dir = []


def main():
    try:
        if not os.path.isfile(os.getcwd()+"/retrieved_dir.dmd"): # checking if retrieved_dir.dmd file exists
            with open(os.getcwd()+"/retrieved_dir.dmd", "w") as f: # else create it
                pass
        with open(os.getcwd()+"/retrieved_dir.dmd", "r") as f: #opening for reading
            dirs = f.readlines()
        if dirs != []: # if the retrieved_dir.dmd file has been written to b4
            for dir in dirs:
                dir = dir.strip("\n")
                if dir in site_dir_list:
                    site_dir_list.remove(dir)
        create_threads() # call create threads function
    except Exception:
        save()
        #exit() # exit cleanly
def create_threads():
    try:
        threads_list = []
        for i in range(6): # i want to be creating 5 threads at a time
            if site_dir_list != []: # checking in case the remaining directories are less than five
                new_thread = threading.Thread(target=start_job, args=()) #create the thread with a directory
                threads_list.append(new_thread) # sending the thread to the list

        for i in range(len(threads_list)):
            threads_list[i].start() # initiate threading
            sleep(1)

        for i in range(len(threads_list)):
            threads_list[i].join()
    except Exception:
        save()


def start_job():
    while site_dir_list != []:
        dir = site_dir_list[-1]
        site_dir_list.remove(dir)
        get_links(dir)
        save()


def get_links(dir):
    try:
        with requests.Session() as s:
            page = s.get(host+"/"+dir, headers=headers) #open the page of the current directory
        if not os.path.isdir(os.getcwd()+"/"+dir): #check if the directory has not been created
            os.mkdir(os.getcwd()+"/"+dir)  # create the directory
        files_link = get_files_link(page.content) # call the function that retrieve and returns the links
        files_link = remove_duplicate(files_link) # u get the point
        with requests.Session() as s:
            for link in files_link:
                file_name = validate_filename(link)
                if not os.path.isfile(os.getcwd()+"/"+dir+file_name):
                    file_get = s.get(host+"/"+dir+link, headers=headers)
                    with open(os.getcwd()+"/"+dir+file_name, "wb") as f:
                        f.write(file_get.content)
                    print("Retrieved %s \n"%(file_name,))
            fully_retrieved_dir.append(dir)
    except Exception:
        save()


def validate_filename(link):
    try:
        name = link.replace("%20", "_")
        return name
    except Exception:
        save()


def get_files_link(page):
    try:
        links = []
        soup = bs(str(page), "html.parser")
        a_tags = soup.find_all("a")
        for a in a_tags:
            link = a["href"]
            if link_is_file(link):
                links.append(link)
        return links
    except Exception:
        save()


def remove_duplicate(links):
    unique_links = [] #this list does not contain duplicates
    for link in links:
        if link not in unique_links:
            unique_links.append(link)
    return unique_links


# performs simple checks if don't get this too, this code is not for u
def is_link_dir(link):
    try:
        if link[:4] == "http":
            return False
        elif link[-1] != "/":
            return False
        elif not link[0].isupper():
            return False
        else:
            return True
    except Exception:
        save()

def link_is_file(link):
    try:
        if link[:4] == "http":
            return False
        elif link[-1] == "/":
            return False
        elif not link[0].isupper():
            return False
        else:
            return True
    except Exception:
        save()
#this function is called to save the name of directories that have been retrieved
def save():
    with open(os.getcwd()+"/retrieved_dir.dmd", "a") as f:
        if fully_retrieved_dir != []:
            for i in range(len(fully_retrieved_dir)):
                f.write(fully_retrieved_dir[i]+"\n")
    for i in fully_retrieved_dir:
        fully_retrieved_dir.remove(i)

#this function retrieve the link of dirs from the site
def get_site_dir_list():
    try:
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
    except Exception:
        save()

#placed here cos the function needs to be initialized
site_dir_list = get_site_dir_list() # get the directory link from the site
site_dir_list = remove_duplicate(site_dir_list) # this fucntion remove duplicate links
main()

#if __name__=="__main__":
#    main()

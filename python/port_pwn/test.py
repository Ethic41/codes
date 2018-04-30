from bs4 import BeautifulSoup as bs
import os
import requests

"""
soup = bs(open(os.getcwd()+"/hawwa.html", "r"), "html.parser")
clean_page = soup.prettify()
soup = bs(clean_page, "html.parser")
print(soup.input.input.input["value"])
"""

host = "https://portal.abu.edu.ng"
payload = {"username":"u13ce1096", "password":"zamfara"}
with requests.Session() as s:
    login = s.post(host+"/index.php", data=payload)
    print("logged in as %s"%payload['username'])
    #acc_page = s.get(host+"/abudashboard/?t=wu3povrfdj")
    page_cont = s.get(host+"/abudashboard/sites/accommodation/accommodation.php")
print(page_cont.content)

"""
with open(os.getcwd()+"/acc_cont.html", "w") as f:
    f.write(page_cont.content)
print("Done")

soup = bs(open(os.getcwd()+"/acc_cont.html", "r"), "html.parser")
#clean = soup.prettify()
#soup = bs(clean, "html.parser")
#a_tags = soup.find("a", attrs={"target":"_blank"})
#soup = bs(str(a_tags), "html.parser")
link = soup.a["href"]
print(link)
"""

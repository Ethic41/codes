from bs4 import BeautifulSoup4 as bs
import os
import requests

host = "https://portal.abu.edu.ng"

def get_acc_info(s):
    acc_page = s.get(host+"/abudashboard/sites/accommodation/accommodation.php")
    page = acc_page.content
    soup = bs(str(page), "html.parser")
    link = soup.a["href"]
    undertaking = s.get(link)
    stdid, date, year = get_values(undertaking.content)
    payload = {"stdid":stdid, "date":date, "session":year, "checkbox":"on",\
    "button":"I Accept", "MM_insert":"form2", "token":link[59:]}
    return payload

def get_values(page):
    soup = bs(str(page), "html.parser")
    stdid = soup.input["value"]
    date = soup.input.input["value"]
    year = soup.input.input.input["value"]
    return stdid, date, year


if __name__=="__main__":
    get_acc_info(s)

import requests
from bs4 import BeautifulSoup as bs
import os

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

def main():
    with open(os.getcwd()+"/file.dmd", "w") as f:
        f.write("TimeIsOne")
    with open(os.getcwd()+"/file.dmd", "r") as f:
        value = f.readline()
    print(len(value))


if __name__=="__main__":
    main()

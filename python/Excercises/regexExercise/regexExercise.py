#codeName: regexExercise.py
#Author: Dahir Muhammad Dahir
#Date: 28th-March-2018
#About: regular expressions exercises

import re


def main():
    #exercise1()
    #exercise2()
    #exercise3()
    #exercise4()
    exercise5()


def exercise1():
    while(True):
        validWords = re.compile("[bh][aiu]t")
        word = raw_input("Enter a valid:\n")
        if validWords.match(word):
            print("%s is a valid word"%(word))
        elif word == "exit":
            break
        else:
            print("Invalid word")


def exercise2():
    while(True):
        userName = re.compile("[A-Z][a-z]{1,}\s{1,1}[A-Z][a-z]{1,}")
        name = raw_input("Enter your username:\n")
        if userName.match(name):
            print("%s is a valid userName"%(name))
        elif name == "exit":
            break
        else:
            print("invalid userName")


def exercise3():
    while(True):
        userName = re.compile("[A-Z][a-z]{1,}\s{1,1}[A-Z]{1,1}$")
        name = raw_input("Enter userName:\n")
        if userName.match(name):
            print("%s is a valid userName"%(name))
        elif name == "exit":
            break
        else:
            print("invalid userName")

def exercise4():
    while(True):
        validIdentifier = re.compile(r"^[A-Za-z_][A-Za-z0-9_]{1,}\b")
        identifier = raw_input("Enter an identifier:\n")
        if validIdentifier.match(identifier):
            print("%s is a valid python identifier"%(identifier))
        elif identifier == "exit":
            break
        else:
            print("invalid python identifier")


def exercise5():
    while(True):
        validStreetAdress = re.compile("^[0-9]{1,} {1,1}([A-Z]{1,1}[a-z]{1,} {0,1}){1,}\b")
        validStreet = raw_input("Enter a street address:\n")
        if validStreetAdress.match(validStreet):
            print("%s is a valid Street address"%(validStreet))
        elif validStreet == "exit":
            break
        else:
            print("invalid street address")


if __name__=="__main__":
    main()

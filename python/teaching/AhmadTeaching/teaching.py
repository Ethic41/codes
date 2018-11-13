#Date: 24th-October-2018
#Author: Dahir Muhammad Dahir


#for loop
#while loop
#break
#continue

#takes usernames and print it out
"""
while True:
    username = raw_input("Enter ur name and i will print it out:\n")
    print(username)
"""

#print out odd numbers only from 0..100
"""
counter = 1
while(counter < 100):
    if counter % 2 != 0:
        print(counter)
    counter += 1
"""
"""
#while with conditions
command = ""
while(command != "exit"):
    print("\n\navailable commands: print <something> ==> to print something to screen\ngreet <someone> ==> to greet someone\ncry ==> to cry\nlaugh ==> to laugh\nexit ==> to..you know what")
    command = raw_input(">")
    if command.startswith("print"):
        print(command[6:])
    elif command.startswith("greet"):
        print("hello " + command[6:])
    elif command == "cry":
        print("can't cry babe!")
    elif command == "laugh":
        print("laughing...")
    elif command == "exit":
        exit()
    else:
        print("command unknown...please use available commands")

print("we broke out")
"""
"""
database = {"tahir":1234, "ahmad":2018, "musty":1122} 

retry_check = {}
while(True):
    username = raw_input ('Enter username: ')
    pin = input ('Passcode: ')

    if username in database:
        if username not in retry_check:
            retry_check[username] = 0
        if(retry_check[username] < 3):
            if database[username] != pin:
                print("=-=={ Access Denied }==-=")
                retry_check[username] += 1
            elif database[username] == pin:
                print("=-=={ Access Granted }==-=")
                retry_check[username] = 0
                break
        else:
            print("=-=={ Banned for Life }==-=")
            break
"""

"""
counter = 1
while True:
    if username,pin in database:
        print "access granted"
    elif username,pin not in database:
        counter += 1
    if counter = 4:
        exit()
"""

#function Declaration
def main():
    ahmad("abdulhamid", 1234)
    tahir("musa", "10-10-2018", "hope", "faith", "time")

def ahmad(username, password, gender="male"):
    print("welcome %s, to ahmad function"%(username))
    print("your password is %d"%(password))
    print("Gender: %s"%(gender))
    

def tahir(username, dateofbirth, **cool):
    print("welcome %s, to tahir function"%(username))
    print("date of birth is %s"%(dateofbirth))
    print(cool)


main()

#if __name__=="__main__":
#    main()
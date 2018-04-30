import requests
import argparse
from time import ctime
import os
import threading
from get_std_info import get_acc_info

host = "https://portal.abu.edu.ng"

def main():
    parser = argparse.ArgumentParser(description="port_pwn is currently just \
    capable of accommodation", formatter_class=argparse.RawDescriptionHelpFormatter,\
     epilog="\nExample:\n   port_pwn.py -u u13ceXXXX -p xxxxxx -r 12")
    parser.add_argument("-u", "--username", help="specify a username or list of\
     usernames", required=True)
    parser.add_argument("-p", "--password", help="specify a password or list of\
     password for the corresponding usernames", required=True)
    parser.add_argument("-r", "--roomid", help="specify the roomid",\
     required=True)
    args = parser.parse_args()
    username_list = args.username.split(",") # split the usernames by ","
    password_list = args.password.split(",")
    create_threads(username_list, password_list, args.roomid) #calling the threading function


def create_threads(username_list, password_list, roomid):
    threads_list = []
    if len(username_list) == len(password_list):
        for i in range(len(username_list)):
            new_thread = threading.Thread(target=login, \
            args=(username_list[i], password_list[i], roomid))
            threads_list.append(new_thread)

        for thread in threads_list:
            thread.start()

        for thread in threads_list:
            thread.join()
    else:
        print("incorrect number of username or password was supplied")


def login(username, password, roomid):
    payload = {"username":username, "password":password}
    while True:
        login_trial,s = do_login(payload) #we try to login
        login_status = check_status_OK(login_trial.status_code) #check if login was successful
        content_check = "Failed to connect to database." not in login_trial.content #check if connection was successful
        if login_status == True and content_check:
            print("Successfully logged In for %s"%username)
            break
    accom_status = get_accommodation(roomid, s)
    print("[%s]: Reservation for %s returned %s"%(ctime(), username, str(accom_status)))


def do_login(payload):
    with requests.Session() as s:
        login = s.post(host+"/index.php", data=payload)
    return login,s


#this function check the status code of request it takes only one argument
def check_status_OK(status_code):
    if status_code == 200:
        return True
    else:
        return False


def get_accommodation(roomid, s):
    payload = get_acc_info(s)
    payload2 = {"reason": "reservation", "rid":roomid, "stdid":payload["stdid"], \
    "session":payload["session"]}
    page = s.post(host+"/accommodation/reservation.php", data=payload)
    reserve = s.post(host+"/accommodation/reservation.php", data=payload2)
    return reserve.content


if __name__=="__main__":
    main()


#Code_Name: reverse_string
#Author: Dahir Muhammad Dahir
#Date: 28-January-2018 9:29AM
#About: the program infinitely loop waiting for the user
#       to enter a string and then it print out the reversed string.

def reverse():
    try:
        while(True):
            string = raw_input("Enter a string to reverse:%s"%"\n")
            reversed = ""
            for i in range(1, len(string)+1):
                reversed += string[-i]
            print(reversed)
    except Exception:
        exit()

if __name__ == "__main__":
    reverse()

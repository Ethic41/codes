
#Code_Name: is_palindrome
#Author: Dahir Muhammad Dahir
#Date: 28-January-2018
#About: this program checks if the user specified string is is_palindrome

def is_palindrome():
    try:
        while(True):
            string = raw_input("Enter string:%s"%"\n")
            string = string.lower()
            reversed = ""
            for i in range(1, len(string)+1):
                reversed += string[-i]
            if string == reversed:
                print("%s is a palindrome ==> %s"%(string, reversed))
            else:
                print("%s is not palindrome ==> %s"%(string, reversed))
    except Exception:
        exit()

if __name__=="__main__":
    is_palindrome()

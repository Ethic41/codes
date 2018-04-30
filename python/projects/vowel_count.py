
#Code_Name: vowel_count
#Author: Dahir Muhammad Dahir
#Date: 28-January-2018 10:25AM
#About: the program takes the user input
#       and output the number of vowels therein

def vowels_count():
    try:
        while(True):
            string = raw_input("Enter a string: %s"%"\n")
            string = string.lower()
            A,E,I,O,U = 0,0,0,0,0
            for i in string:
                if i == "a":
                    A +=1
                elif i == "e":
                    E +=1
                elif i == "i":
                    I +=1
                elif i == "o":
                    O += 1
                elif i == "u":
                    U += 1
            print(" '%s' Summary:%s A ==> %d%s E ==> %d%s I ==> %d%s O ==> %d%s U ==> %d" %(string, "\n", A, "\n", E, "\n", I, "\n", O, "\n", U,))
    except Exception:
        exit()

if __name__=="__main__":
    vowels_count()

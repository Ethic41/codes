
def format(data): # format data in a fancy ascii way.
    try:
        if data != "":
            data = "\n+"+2*"-"+len(data)*"-"+2*"-"+"+\n"+"|"+2*" "+data+2*" "+"|\n"+"+--"+len(data)*"-"+"--+"
            return data
        else:
            return data
    except Exception, e:
        error(e)


def error(e):
    print("Error: "+str(e)+" exiting...")
    exit()


if __name__=="__main__":
    main()
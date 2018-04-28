from time import ctime


def time_format(data): # format data in a fancy ascii way with time.
    try:
        data1 = ctime() #get current time
        if len(data)<=len(data1):
            margin = len(data1)
            diff = len(data1)-len(data)+2
            diff1=2
        else:
            margin = len(data)
            diff = 2
            diff1 = len(data) - len(data1)+2
        if data != "":
            data = "\n+"+2*"+"+margin*"-"+2*"-"+"+\n"+"|"+2*" "+data1+diff1*" "+"|\n"+"+"+2*"-"+margin*"-"+2*"-"+"+\n"+"|"+2*" "+data+diff*" "+"|\n"+"+--"+margin*"-"+"--+"
            return data
        else:
            return data
    except Exception, e:
        print(e)
        pass

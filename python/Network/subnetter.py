#subnetter take an ip address in format "192.168.43.236" and return the form
#"192.168.43." removing the last part
def subnetter(ip):
    while ip[-1] != ".":
        ip = ip[0:-1]
    return ip

if __name__=="__main__":
    subnetter(ip)

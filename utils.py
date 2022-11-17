import re

def checkValidIpAddress(addr:str) :
    #Check si l'adresse ip match la regex suivante 
    match = re.match(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", addr)
    if not bool(match) :
        return False
    
    ipOctets = addr.split(".")

    #Check si les bytes de l'addresse sont correcte
    for octets in ipOctets :
        if (int(octets) < 0 or int(octets) > 256) :
            return False
        
    return True

def checkValidPort(port:int) :
    if (port < 0 or port > 65535) :
        return False
    return True

    
    
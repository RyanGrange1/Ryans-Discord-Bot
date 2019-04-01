def hashName(name):
    hash = "";
    for i in name:
        hash += str(ord(i))
    return hash

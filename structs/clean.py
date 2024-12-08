def cleanString(byteObj):
    return byteObj.decode().rstrip('\x00')
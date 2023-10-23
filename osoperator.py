from sys import platform

def operator():
    opr = ''
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        opr = '&&'
    elif platform == "win32":
        opr = ';'
    return opr
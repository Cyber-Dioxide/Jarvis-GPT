import platform

def check():
    if "Windows" in platform.platform():
        return True
    else:
        return False

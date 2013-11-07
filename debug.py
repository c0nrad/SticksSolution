import traceback

# DEBUG STUFF
ERROR = '\033[91m' # Red
WARNING = '\033[93m' # Yello
NORMAL = '\033[0m' # Black
GOOD = '\033[92m' # Green

def green(*items):
    global GOOD
    out = GOOD
    for item in items:
        out += str(item)
    return out + NORMAL

def red(*items):
    global ERROR
    out = ERROR
    for item in items:
        out += str(item)
    return out + NORMAL

def errorMessage(*items):
    global ERROR
    out = ERROR + "[-] "
    for item in items:
        out += str(item)
    print out + NORMAL

def warningMessage(*items):
    global WARNING
    out = WARNING + "[-] "
    for item in items:
        out += str(item)
    print out + NORMAL

def infoMessage(*items):
    global NORMAL
    out = NORMAL + "[+] "
    for item in items:
        out += str(item)
    print out + NORMAL    

def goodMessage(*items):
    global GOOD
    out = GOOD + "[*] "
    for item in items:
        out += str(item)
    print out + NORMAL

def debug(f):
    def _debug(*args, **kw):
        tab = "  " * (len(traceback.extract_stack())/2 - 1)
        arguments = kw.copy()
        arguments.update(dict(zip(f.func_code.co_varnames, args)))
        goodMessage(tab,"[+] %s::%s:" % (f.__module__, f.__name__), arguments)
        return f(*args, **kw)
    return _debug

@debug
def factorial(n):
    if n in (0, 1):
        warningMessage("n in (0, 1)")
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    errorMessage("FAILED TO INIT SOMETHING")
    warningMessage("The baby is in the oven")
    infoMessage("I LIKE TRAINS")
    goodMessage("The oven is off")
    print "NOWAI"

    factorial(5)
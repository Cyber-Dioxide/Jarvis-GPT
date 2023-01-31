import sys
import time


def sprint(text):
    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)


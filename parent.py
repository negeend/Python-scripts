import os
import sys

pid = os.fork()

if pid == 0: 
    print("I am the child process")
    os.execl(sys.executable, "python3", "child.py")
    print("this should not be printed")
elif pid == -1:
    print("fork failed")
else:
    print("Running parent", pid)
    waitval = os.wait
    print("I am the parent process with pid,", pid)
    # print("exit status", waitval[1]>>8)

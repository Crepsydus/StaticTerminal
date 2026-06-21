import subprocess as sp
import colorful as c
from sys import executable

si = sp.STARTUPINFO()
si.dwFlags |= sp.STARTF_USESHOWWINDOW
si.wShowWindow = 3
process = sp.Popen(
            [executable, '-u', "starter.py", "test.py"],
            creationflags=sp.CREATE_NEW_CONSOLE,
            startupinfo=si,
        )

try:
    while True:
        if process.poll() is not None:
            print(c.F.color(1) + "Not alive (Terminating process)")
            quit()
except KeyboardInterrupt:
    print(c.F.color(1) + "Keyboard interrupt (Terminating process)")
    process.terminate()

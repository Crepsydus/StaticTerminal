from static_terminal import StaticTerminal
from sys import argv

maximized = bool(int(argv[1]))
s = StaticTerminal(maximized, auto_update=True)

i = 0
while True:
    s.roll("0",str(i))
    i+=1
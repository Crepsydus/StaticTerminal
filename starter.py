from static_terminal import StaticTerminal
from sys import argv

script = argv[1]
maximized = bool(int(argv[2]))
custom_trigger = argv[3]
args = argv[4:]
s = StaticTerminal(maximized)
s.start(script, custom_trigger,args)
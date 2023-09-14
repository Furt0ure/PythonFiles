# module    = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts

#improt messages import *   = imports all (AKA dangerous for big files, can use for small... but not optimal)
#from messages import hello,bye
import messages as msg

msg.hello()
msg.bye()

#help("modules")
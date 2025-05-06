import time as t  , sys

print("Program to print a zig-zag pattern!!")
t.sleep(0.2)
print("press Ctrl-c to stop the pattern!!")
t.sleep(0.2)
stars=30
min_indent=30
max_indent=60
indent=max_indent

indent_increase=True
try:
    while True:
        print(" "*indent,end="")
        print("*"*stars)
        t.sleep(0.01)
    
        if indent_increase==True:
            indent-=1
            if indent==min_indent:
                indent_increase=False    
        else:
            indent+=1
            if indent==max_indent:
                indent_increase=True

 
except KeyboardInterrupt:
    sys.exit()

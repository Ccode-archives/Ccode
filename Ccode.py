#imports and settings
import os
os.system("cp ~/Ccode/scripts/main.js ~/Ccode/")

try:
    file = open('main.cc', 'r')
    text = file.readlines()
except FileNotFoundError:
    print("main.cc missing, aborting")

#js writing command
def js(out):
    f = open("main.js", "a")
    f.write("\n")
    f.write(out)
    f.close()

#unknown command message
def NU():
    print("unknown command")

#loop start
for line in text:
    #input
    inp = line.strip()
    #print
    if inp.startswith("print "):
        println = inp.replace("print ", "")
        out = "console.log(" + println + ");"
        js(out)
    elif inp == "":
        out = "null"
    #while
    elif inp.startswith("while ") and inp.endswith(" {"):
        out = inp.replace("while ", "")
        out = out.replace(" {", "")
        js("while (" + out + ") {")
    #if statements
    elif inp.startswith("if ") and inp.endswith(" {"):
        out = inp.replace("if ", "")
        out = out.replace(" {", "")
        js("if (" + out + ") {")
    #else
    elif inp == "else {":
        js(inp)
    #elif
    elif inp.startswith("elif ") and inp.endswith(" {"):
        out = inp.replace("elif ", "")
        out = out.replace(" {", "")
        js("else if (" + out + ") {")
    #end brackets
    elif inp == "}":
        js(inp)
    #variables
    elif inp.find("=") > -1 or inp.find(" = ") > -1:
        out = "var " + inp
        if inp.find("input") > -1:
            out = inp.replace("input", "prompt('>>')")
        js(out + ";")
    else:
        NU()
#end of loop

#run commands
os.system("./run")
os.system("rm main.js")

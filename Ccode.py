#imports and settings
import os
import sys
import distutils.spawn
import platform


def is_tool(name):
    return distutils.spawn.find_executable(name) is not None

if platform.system() == "Windows":
    raise OSError("Don't run on Windows!")
if not is_tool("node"):
    raise OSError("Node.js is not installed!")
if not os.path.exists(os.path.expanduser("~") + "/Ccode"):
    raise OSError("Ccode language is not installed in the home directory!")
if not os.path.exists(os.path.expanduser("~") + "/Ccode/lib/builtins"):
    raise OSError("Builtins library is not installed!")

#check if the directory is a node project
node = os.path.exists("main.js") or os.path.exists("node_modules") or os.path.exists("package.json") or os.path.exists("lib")
if os.getcwd().endswith("Ccode"):
    node = True
# run code at end
runjs = True
#js writing command
def js(out):
    #If dir is node project don't write to temp.js
    if not node:
        f = open("temp.js", "a")
        f.write("\n")
        f.write(out)
        f.close()
    else:
        return
#copy project to current dir unless it is a node project
if not node:
    os.system("cp -r ~/Ccode/node_modules .")
    os.system("cp ~/Ccode/package.json .")
    os.system("cp ~/Ccode/package-lock.json .")
else:
    print("\n\nPlease don't run in node project folders.  Project will be scanned for errors but not run.\n\n")
os.system("mkdir cclib")
#make temp.js
if not node:
    os.system("touch temp.js")
# builtins
os.system("cp -r ~/Ccode/lib/builtins cclib/builtins")
builtins = open("cclib/builtins/builtins.js", "r")
data = builtins.read()
builtins.close()
js(data + "\n")
builtin_commands = open("cclib/builtins/com.txt", "r")
commands = builtin_commands.readlines()
builtin_commands.close()
os.system("rm -rf cclib/builtins")
args = sys.argv
#load script file
try:
    file = open(args[1], 'r')
    text = file.readlines()
    file.close()
except:
    try:
        print("\n\n\n\nFile " + args[1] + " missing, aborting\n\n\n\n")
    except:
        print("\n\n\n\nNo arguments given\n\n\n\n")
    if not node:
        os.system("rm -r node_modules")
        os.system("rm package.json")
        os.system("rm package-lock.json")
        os.system("rm temp.js")
    os.system("rm -rf cclib")


#unknown command message
def NU(line):
    print("error on line: " + str(line))
    global runjs
    runjs = False
line_num = 0
#loop start
for line in text:
    line_num += 1
    # debug
    #print(line.replace("\n", "") + " : \033[1;32m" + str(commands) + "\033[1;0m")
    # remove doubles in commands. (better for memmory)
    commands = list(dict.fromkeys(commands))
    #input
    inp = line.strip()
    #comments
    if inp == "" or inp.startswith("//"):
        out = "null"
    #inline js
    elif inp.startswith("js ") and inp.endswith(" js"):
        out = inp[3:][:-3]
        js(out)
    #imports
    elif inp.startswith("import "):
        imp = inp[7:]
        #get file
        try:
            os.system("cp -r ~/Ccode/lib/" + imp + " cclib")
            impfile = open("cclib/" + imp + "/" + imp + ".js", "r")
            data = impfile.read()
            impfile.close()
            js(data + "\n")
            comfile = open("cclib/" + imp + "/com.txt", "r")
            newcoms = comfile.readlines()
            comfile.close()
            commands = commands + newcoms
            os.system("rm -rf cclib/" + imp)
        except:
            print(f'module "{imp}" does not exist')
    #functions
    elif inp.startswith("func ") and inp.endswith(" {"):
        name = inp.replace("func ", "").split("(")[0]
        commands.append(name + "\n")
        out = inp.replace("func ", "function ")
        out = out.replace("{", "")
        js(out + "{")
    #while
    elif inp.startswith("while ") and inp.endswith(" {"):
        if inp.count("(") > 1:
            print("Don't put more than one function in a line!")
            NU(line_num)
            # exit on error
            break
        out = inp.replace("while ", "")
        out = out.replace(" {", "")
        js("while (" + out + ") {")
    #if statements
    elif inp.startswith("if ") and inp.endswith(" {"):
        if inp.count("(") > 1:
            print("Don't put more than one function in a line!")
            NU(line_num)
            # exit on error
            break
        out = inp.replace("if ", "")
        out = out.replace(" {", "")
        js("if (" + out + ") {")
    #else
    elif inp == "else {":
        js(inp)
    #elif
    elif inp.startswith("elif ") and inp.endswith(" {"):
        if inp.count("(") > 1:
            print("Don't put more than one function in a line!")
            NU(line_num)
            # exit on error
            break
        out = inp.replace("elif ", "")
        out = out.replace(" {", "")
        js("else if (" + out + ") {")
    #end brackets
    elif inp == "}":
        js(inp)
    #function execution
    elif inp.endswith(")"):
        if inp.count("(") > 1:
            print("Don't put more than one function in a line!")
            NU(line_num)
            # exit on error
            break
        else:
            if not "=" in inp:
                if inp.split("(")[0] + "\n" in commands:
                    js(inp + ";")
                else:
                    print("Unknown command was issued!")
                    NU(line_num)
                    # exit on error
                    break
            else:
                com = inp.split("=", 1)[1]
                com = com.split("(")[0].strip() + "\n"
                if com in commands:
                    try:
                        change = inp.replace("set ", "")
                    except:
                        change = inp
                    js("var " + change + ";")
                else:
                    print("Unknown command was issued!")
                    NU(line_num)
                    # exit on error
                    break
    #variables
    elif inp.find("=") > -1 or inp.find(" = ") > -1:
        if inp.startswith("set "):
            change = inp.replace("set ", "")
            out = "var " + change
        else:
            out = inp
        js(out + ";")
    #errors
    else:
        NU(line_num)
        # exit on error
        break
#end of loop
#if project is node directory don't delete node files or run node project made
if not node:
    if runjs:
        os.system("node temp.js " + " ".join(args[2:]))
    os.system("rm temp.js")
    os.system("rm -r node_modules")
    os.system("rm package.json")
    os.system("rm package-lock.json")
os.system("rm -rf cclib")

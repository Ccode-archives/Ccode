## Ccode
A new fast and lightweight language based on a transpiler instead of a compiler.  
Ccode has nothing to do with any other version of C, it is a separate project.

## How it works
1. It first copys main.js from scripts to the main dir.
2. It reads a file called main.cc and gets rid of whitespace such as tabs or spaces at the start or beginning of a command.
3. Once it reads all the lines it runs the Javascript it created.
4. It deletes the Javascript. (Comment the last line to turn this off)


## Requirments
1. Python3 (To run the transpiler)
2. Bash (You need to be on linux for it to work so this is installed)
3. Node.js (To run the Javascript files that are generated)


## Installation
```bash
command cd ~/
git clone https://github.com/Ccode-lang/Ccode.git
cd Ccode/
chmod +x bootstrap
./bootstrap
#You now need to follow the instructions from the last step to run the language
```

## Included commands
### Print syntax: 
```
print 'hi'
```
### Variables syntax1: 
```
h = 5
```
# syntax2:
```
h = "hi"
```
### If statements syntax: 
```
if h == 5 {  
print 'hi'  
}  
elif h == 4 {   
print 'bye'  
}  
else {  
print 'hello'  
}  
```
### Input variable syntax: 
```
h = input
```
This gets user input and stores it in the given variable.
### While
```
while h == 1 {  
print 'hi'  
}  
```


### Please record issues to get them fixed or go to disscutions if you get an error message!
This language is in the early stages of development.  
If you get a node.js error message it means you either forgot A end bracket or there is an error in the main Ccode.py file.  
If you get errors like these report them as soon as possible.  

## terminal output
The language gets user input through the node packages downloaded by the bootstrap script.   
This is th command used.
```javascript
const prompt = require('prompt-sync')();
```

## main script file
```python
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

```

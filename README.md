## Ccode
A new fast and lightweight language based on a transpiler instead of a compiler

## How it works
1. It first copys main.js from scripts to the main dir.
2. It gets user input and turns it into Javascript.
3. It dose step two until it gets the input "run".
4. Once input run in given it runs the Javascript it created.
5. It deletes the Javascript. (Comment the last line to turn this off)


## Requirments
1. Python3 (To run the transpiler)
2. Bash (You need to be on linux for it to work anyway so this is installed)
3. Node.js (To run the Javascript files that are generated)


## Installation
1. run command cd ~/
2. run git clone https://github.com/Ccode-lang/Ccode.git
3. run cd Ccode/
4. run ./bootstrap
5. You now need to follow the instructions from the last step to run the language


## Included commands
### print (syntax: print 'hi')
### variables (syntax1: h = 5 syntax2: h = "hi")
### If statements syntax: 
if h = 5 {  
print 'hi'  
}

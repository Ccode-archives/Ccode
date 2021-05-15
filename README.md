## Ccode
A new fast and lightweight language based on a transpiler instead of a compiler

## How it works
1. It first copys main.js from scripts to the main dir.
2. it reads a file called main.cc.
3. Once it reads all the lines it runs the Javascript it created.
4. It deletes the Javascript. (Comment the last line to turn this off)


## Requirments
1. Python3 (To run the transpiler)
2. Bash (You need to be on linux for it to work anyway so this is installed)
3. Node.js (To run the Javascript files that are generated)


## Installation
1. run command cd ~/
2. run git clone https://github.com/Ccode-lang/Ccode.git
3. run cd Ccode/
4. run chmod +x bootstrap
5. run ./bootstrap
6. You now need to follow the instructions from the last step to run the language


## Included commands
### Print (syntax: print 'hi')
### Variables (syntax1: var h = 5 syntax2: var h = "hi")
### If statements syntax: 
if h == 5 {  
print 'hi'  
}  
elif h == 4 {
print 'bye'  
}  
else {  
print 'hello'  
}  
### Input variable (syntax: var h = input)
This gets user input and stores it in the given variable.
### While
while h == 1 {  
print 'hi'  
}  

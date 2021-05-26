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
1. run command cd ~/
2. run git clone https://github.com/Ccode-lang/Ccode.git
3. run cd Ccode/
4. run chmod +x bootstrap
5. run ./bootstrap
7. You now need to follow the instructions from the last step to run the language


## Included commands
### Print (syntax: print 'hi')
### Variables (syntax1: h = 5 syntax2: h = "hi")
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
### Input variable (syntax: h = input)
This gets user input and stores it in the given variable.
### While
while h == 1 {  
print 'hi'  
}  


### Please record issues to get them fixed or go to disscutions if you get an error message!
This language is in the early stages of development.  
If you get a node.js error message it means you either forgot A end bracket or there is an error in the main Ccode.py file.  
If you get errors like these report them as soon as possible.  

## terminal output
after execution the terminal should say something like. 

```
~ % cd Ccode
Ccode % chmod +x bootstrap
Ccode % ./bootstrap

+ prompt-sync@4.2.0
added 3 packages from 3 contributors and audited 3 packages in 2.288s
found 0 vulnerabilities

run python3 Ccode.py to run

```

## main script file
```python

```

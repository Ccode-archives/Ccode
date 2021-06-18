## Ccode
A new fast and lightweight language that compiles to javascript.  
Ccode has nothing to do with any other version of C, it is a separate project.

## Contributing
Please send in pull requests to get your code on here.  

## How it works
1. It first copys main.js from scripts to the main dir.
2. It reads a file called main.cc and gets rid of whitespace such as tabs or spaces at the start or beginning of a command.
3. Once it reads all the lines it runs the Javascript it created.
4. It deletes the Javascript. (Comment the last line to turn this off, if turned off it may cause errors)


## Requirments
1. Python3 (To run the compiler)
2. Bash (You need to be on linux for it to work so this is installed)
3. Node.js (To run the Javascript files that are generated)


## Installation
```bash
command cd ~/
git clone https://github.com/Ccode-lang/Ccode.git
cd Ccode/
chmod +x bootstrap
./bootstrap
# You now need to follow the instructions from the last step to run the language
```

## Included commands
### Print syntax: 
```
print 'hi'
```
### Variables syntax1: 
```
set h = 5
```
# syntax2:
```
h = 5
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
### functions
declaration
```
func test(num1, num2) {
  print num1 + num2
}
```
using function
```
test(1, 2)
```

### Please record issues to get them fixed or go to disscutions if you get an error message!
This language is in the early stages of development.  
If you get a node.js error message it means you either forgoten a end bracket parenthesis or there is an error in the main Ccode.py file.  
If you get errors like these report them as soon as possible.  



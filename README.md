## Ccode
A new, fast, and statically typed language that compiles to javascript.  
Ccode has nothing to do with C, it is a separate project.  
Go to Discussions page to get help on how to use!

## Supported platforms
 * linux
 * macos
 * windows (using WSL. No plan to implement normal windows.)
## Installing third-party modules
 * Download their module folder
 * Put it in the libs folder
 * Import it
 * Done!
## Contributing
Please send in pull requests to get your features here.

## How it works
1. It first creates main.js and imports builtin module.
2. It reads a file given to it and gets rid of whitespace such as tabs or spaces at the start or end of a command.
3. Once it reads all the lines it runs the Javascript it created.
4. It deletes the Javascript.
## setup (without Ccode Command addon)
```bash
make all
```
## Running (without Ccode command addon)
```bash
# python3
python3 Ccode.py <path to Ccode file>

# python2
python Ccode.py <path to Ccode file>
# or
python2 Ccode.py <path to Ccode file>
```
## With Ccode command addon
```
Ccode <flags> # runs main.cc in current folder if no file is given with -f flag
```

## Requirments
1. Python3 or 2 (To run the compiler)
2. Bash (You need to be on linux for it to work so this is installed)
3. Node.js (To run the Javascript files that are generated)


## Installation
Go to https://github.com/Ccode-lang/Ccode-Command and follow instructions there.
> this may be out of sync!  

## Find out how to use it
See [here](https://github.com/Ccode-lang/Ccode/wiki/builtins-and-basic-use)
## Please record issues to get them fixed or go to discussion if you get an error message!
This language is in early stages of development.  
If you get a node.js error message it means you either forgoten a end bracket, parenthesis, forgot to execute a command, didn't execute a command right, or there is an error in the main Ccode.py file.  
If you get errors like these report them as soon as possible.  



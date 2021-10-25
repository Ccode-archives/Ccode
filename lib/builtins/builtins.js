// builtins.js
// imports for other modules
const { exec } = require("child_process");
// input func
const input = require('prompt-sync')();
// print func
function print(string) {
    console.log(string);
}
// sleep func
function sleep(milli) {
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milli);
}

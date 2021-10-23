// builtins.js
const input = require('prompt-sync')();
const { exec } = require("child_process");
function print(string) {
    console.log(string);
}

function sleep(milli) {
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milli);
}

// builtins.js
// input func
const input = require('prompt-sync')();
// print func
function print(string) {
    console.log(string);
}
// sleep func
function sleep(sec) {
    const milli = sec * 1000
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milli);
}
// replace func
function replace(substring, substring2, string, times=1) {
    var counter = 0;
    var string2 = string;
    do {
        counter = counter + 1
        string2 = string2.replace(substring, substring2)
    } while ( ! (counter == times));
    return string2
}

// os.js
// shell func
function shell(command) {
    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`${stdout}`);
    });
}

// shell arguments
function argv() {
    // the arguments after the file are returned
    return process.argv.slice(2);
}

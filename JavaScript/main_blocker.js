/* ================================================= */
/* ===== Website Block Schedulinig Application ===== */
/* ================================================= */

// Make a variable to store path of hosts file
const filePath =  "hosts"; 
// Note* If you are a windows user, your file path should be C:\Windows\System32\drivers\etc\hosts
/**
 * File path: C:\Windows\System32\drivers\etc\hosts
 * Backslash needs to be escaped before execurting
 * const filePath = C:\\Windows\\System32\\drivers\\etc\\hosts
 */

// Store the redirection path in a variable
// The websites in the block list will be directed to localhost (127.0.0.1)
const redirectPath = "127.0.0.1";

// List of websities to be blocked
let websites = ["www.facebook.com", "facebook.com", "twitter.com", "www.twitter.com"];

// Set delay (Time interval after which our script should execute)
let delay = 10000; // 10 seconds

// Define the blocker function
let blocker = () => {
    // Make a new object of Date
    let date = new Date ();
    // Compare whether the current time is free time or block time
    let hours = date.getHours();
    // Blocking our website from 2pm to 4pm
    if(hours >= 14 && hours < 16) {
        console.log('Time to block websites');
    } else {
        console.log('Time to unblock websites');
    }
};

blocker();
// The script should run until closed explicitly
setInterval(blocker, delay);
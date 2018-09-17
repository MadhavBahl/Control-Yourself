# Website block scheduler using JavaScript

Use this JavaScript code for blocking websites on your machine.

## To run the script

```js
sudo node blocker.js
```

## Main Concept

Adding the url to /etc/hosts file.
Basiically, it redirects the given url to 127.0.0.1 (or, whatever you have specified)

## Path to hosts file

### 1. Windows

C:\Windows\System32\drivers\etc\hosts

### 2. Linux (and, Mac)

/etc/hosts

## Explanation Of Script

## Setting Up The Variables

As I told earlier, there is no need of huge directory structuring or setting up of dev environment, all you need to do is make a JavaScript file (say, blocker.js ) and start coding.
First of all, we need to import fs (file system) node module through which we will be making changes to our hosts file. You can read the complete documentation of fs here.
const fs = require('fs');
Now, we will need to initialize 3 variables
1. filePath  -  To store the path of hosts file
2. redirectPath  -  For the redirection path (here, localhost)
3. websites  -  Array of websites to be blocked
Also, we will be making a variable named delay which will store the value of time duration (in miliseconds) after which our script will repeat itself. Basically the idea is to keep the script running all the time to check whether it is the time to block/unbock the websites. To keep it running we will be using setInterval() method in JavaScript, we can also use while (true) {} to make an infinite loop. Right now we are keeping the time after which the function repeats itself to be a constant (say, 10 seconds). But, this script can be made smarter by setting the value of delay equal to the time difference between current time and time to change the state of script (block/unblock). Doing this is much more easier than what it feels like, hence I want you (the reader) to do it yourself, and drop me a message, I would love to hear from you 😃

```js
const filePath = "/etc/hosts";
const redirectPath = "127.0.0.1";
let websites = [ "www.someRandomWebsite.com","anotherWebsite.com" ];
let delay = 10000;
```

**Note*** If you are a windows user, use this path: C:\Windows\System32\drivers\etc\hosts

## The Blocker Function

We will make a blocker function and call it from the setInterval method to keep it running after every given time interval.

```js
let blocker = () => {
    ....
    ....
};
```

## Running the code for blocker function infinitely many times :D

```js
blocker();
setInterval(blocker, delay);
```
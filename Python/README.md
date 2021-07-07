# Website blocker using python

Use this python code for blocking websites on your machine.

## Main Concept

Adding the url to /etc/hosts file.
Basiically, it redirects the given url to 127.0.0.1 (or, whatever you have specified)

## Path to hosts file

### 1. Windows

C:\Windows\System32\drivers\etc\hosts

### 2. Linux (and, Mac)

/etc/hosts

## Modifying the file

![image](https://user-images.githubusercontent.com/26179770/45574589-232fc480-b88e-11e8-8407-a341ddd752d6.png)

#### Try to open facebook now!

![image](https://user-images.githubusercontent.com/26179770/45574623-4490b080-b88e-11e8-940c-351f8f390964.png)

## What does the backup.py even do?
In order to prevent any loss or damage to your system, we have included a utility script <code>backup.py</code> that would make sure that your system configurations are safe. You can always recover your configuration files by following certain steps.

### Where are the backup configs stored?
The backup configs are stored in the following locations according to the operating system you are using:

| Operating System | Location                                 |
|------------------|------------------------------------------|
| Ubuntu / Linux   | <code>~/.ControlYourselfConfig/</code>   |
| Windows          | <code>C:\\.ControlYourselfConfig\\</code> |


### How to backup the config files?
<b>Highly Recommended: </b> Before even thinking to run any other script, you must consider running the script <code>backup.py</code><br>
* <b>Step 1:</b> From the project root folder navigate to the <code>Python/</code>
* <b>Step 2:</b> Fire up the terminal and type <code>python backup.py</code><br>
* <b>Step 3:</b> Follow the simple Menu driven steps to backup, restore or clear the stored backup  from your system.<br><br>
<b>CAUTION: Clearing the backup is not at all recommended if you are not sure what you are doing.</b>
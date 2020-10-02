<p align="left"><img src="logos/horizontalv2.png" alt="Control-Yourself" height="100px"></p>

# Control Yourself
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors)
[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/Control-Yourself/Lobby)

[![GitHub issues](https://img.shields.io/github/issues/MadhavBahlMD/Control-Yourself.svg?style=for-the-badge)](https://github.com/MadhavBahlMD/Control-Yourself/issues)
[![GitHub forks](https://img.shields.io/github/forks/MadhavBahlMD/Control-Yourself.svg?style=for-the-badge)](https://github.com/MadhavBahlMD/Control-Yourself/network)
[![GitHub stars](https://img.shields.io/github/stars/MadhavBahlMD/Control-Yourself.svg?style=for-the-badge)](https://github.com/MadhavBahlMD/Control-Yourself/stargazers)
[![GitHub license](https://img.shields.io/github/license/MadhavBahlMD/Control-Yourself.svg?style=for-the-badge)](https://github.com/MadhavBahlMD/Control-Yourself/blob/master/LICENSE)

[![HitCount](http://hits.dwyl.io/MadhavBahlMD/Control-Yourself.svg)](http://hits.dwyl.io/MadhavBahlMD/Control-Yourself)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/MadhavBahlMD/Control-Yourself/graphs/commit-activity)
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://madhavbahlmd.tech/Control-Yourself/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](http://madhavbahl.tech/contact/) 

<hr />

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

A Software to reduce your distraction caused by several non-productive websites

## Prerequisites
* Git
* NodeJs

## Getting Started
Make sure that you have installed git and nodejs on your system.
Make a fork of this repository.
Open up the Terminal(or Git Bash) and navigate to the working directory and type the following command.

```
git clone https://github.com/{USERNAME}/Control-Yourself.git
```

Make sure to replace the {USERNAME} with your github username.

Then run the following command to install all the dependencies.
```
npm install
```
Run the following command to fire up the application
```
npm start
```


## Steps to run the blocker.js

Running the blocker is very simple. Just download the blocker.js file (inside JavaScript folder) and type in the following command through your terminal,

```sh
sudo node blocker.js
```

It will block the websites in the `websites` array in `blocker.js` file from 2pm to 6pm.

**Note** If you want to block some other websites, just place those websites in the websites array at line number 21 of blocker.js file. And, if you want to change the time at which the program blocks the website, just change the time interval inside the if statement at line number 33. By default the script blocks `www.someRandomWebsite.com` (I dont know what that is, as the name suggests it is SOME RANDOM WEBSITE xD), and it blocks it from 1400 hours (2pm) to 1600 hours (4pm).

## Important Notice

Please take a backup of your hosts file (`/etc/hosts`) before running the script. I am not responsible for any damages.
## Contributors

Thanks goes to these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
| [<img src="https://avatars2.githubusercontent.com/u/26179770?v=4" width="100px;"/><br /><sub><b>MADHAV BAHL</b></sub>](http://madhavbahl.tech/)<br />[📖](https://github.com/MadhavBahlMD/Control-Yourself/commits?author=MadhavBahlMD "Documentation") [📝](#blog-MadhavBahlMD "Blogposts") [💻](https://github.com/MadhavBahlMD/Control-Yourself/commits?author=MadhavBahlMD "Code") [💡](#example-MadhavBahlMD "Examples") [🤔](#ideas-MadhavBahlMD "Ideas, Planning, & Feedback") [👀](#review-MadhavBahlMD "Reviewed Pull Requests") [✅](#tutorial-MadhavBahlMD "Tutorials") | [<img src="https://avatars2.githubusercontent.com/u/32531173?v=4" width="100px;"/><br /><sub><b>Rajdeep Roy Chowdhury</b></sub>](https://github.com/Razdeep)<br />[📖](https://github.com/MadhavBahlMD/Control-Yourself/commits?author=Razdeep "Documentation") [💻](https://github.com/MadhavBahlMD/Control-Yourself/commits?author=Razdeep "Code") [🤔](#ideas-Razdeep "Ideas, Planning, & Feedback") | [<img src="https://avatars2.githubusercontent.com/rajat19" width="100px;"/><br /><sub><b>Rajat</b></sub>](https://github.com/rajat19)<br />[📖](https://github.com/MadhavBahlMD/Control-Yourself/commits?author=rajat19 "Documentation") |
| :---: | :---: | :---: |
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind welcome!

# CUPP - Common User Passwords Profiler
By Kevin Wang, Daniel Liu  
Period 3

## Show of Hands
Who here has ever created a password that included any one of these:
* Your name?
* Nickname?
* Birthdate?
* Pet name?

The average user does this too.

## Your password is vulnerable
Probably not to rockyou.txt, but a `custom password list` that hackers can tailor to your data.

## How do hackers exploit this?
[CUPP](https://github.com/Mebus/cupp) is a tool that creates custom wordlists using your personal information.

## How does CUPP Work?



### Installation
Requirement: `Python 3`

Kali Linux:
```
$ sudo apt install cupp
```

Other:

```
$ git clone https://github.com/Mebus/cupp.git
$ cd cupp/
```

### Running
CUPP is a command line script that provides an interactive mode that allows you to easily input data about your victim:

```
$ python3 cupp.py -i
```
![cupp interactive mode](cupp.png "interactive")

![cupp interactive mode](demo.png "web form")


When running in the interactive mode, you can provide details about the victim:

* name
* nickname
* birthdate
* partner info
* child info
* pet name
* company name
* keywords associated with them

Note that any information that you leave blank will not be reflected in the final wordlist.

After providing this info, CUPP will generate a wordlist geared towards the  information you provided.

In interactive mode in CUPP, you cannot edit the cupp.cfg file in the CLI. Instead, you will have to use a text editor.
However, we have made a web form where you can input the user's data and also edit the config file. 

# Demo
Are there any volunteers willing to fork up their personal data? 

## CLI
Showcase how to use CUPP in the command line

## CLIs are cool and all...
But we created a [CUPP web app]() to streamline the process.

# Lessons

## Data leaks can make your password vulnerable
Even if your password itself is not exposed, your personal data can be used to brute force your passwords.

## USE A PASSWORD MANAGER
Password managers are not suspectable to tailored passwords, among numerous other security benefits.

[Homework](https://github.com/Stuycs-K/final-project-3-wangk-liud/blob/main/HOMEWORK.md)
# CUPP - Common User Passwords Profiler

## Show of Hands
Have you ever created a password with:
Your name?
Nickname?
Birthdate?
Pet name?

## Your password is vulnerable
Probably not to rockyou.txt, but a custom wordlist that hackers can tailor to you.

## How do hackers exploit this?
[CUPP](https://github.com/Mebus/cupp) is a tool that creates custom wordlists using personalized information.

## How do I use CUPP?

### Installation
Requirements: Python 3

Kali Linux:
```
sudo apt install cupp
```

Other:

```
git clone https://github.com/Mebus/cupp.git
cd cupp/
```

### Running
CUPP is a command line script but provides an interactive mode that allows you to easily input data about your victim:

```
./cupp.py -i
```
![cupp interactive mode](cupp.png "interactive")


When running in the interactive mode, you can provide details about the victims:

name
nickname
birthdate
partner info
child info
pet name
company name
ANY KEYWORDS ASSOCIATED WITH THEM




# CUPP - Common User Passwords Profiler

## Show of Hands
Who has ever created a password that included any one of these:
* Your name?
* Nickname?
* Birthdate?
* Pet name?

## Your password is vulnerable
Probably not to rockyou.txt, but a custom password list that hackers can tailor to your data.

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

# Demo
Any volunteers willing to fork up their personal data?

# Lessons

## Data leaks can make your password vulnerable
Your personal data can be used to bruteforce your passwords.

## USE A PASSWORD MANAGER
Password managers are not suspectable to tailored passwords, among numerous other security benefits.


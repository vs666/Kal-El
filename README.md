# Kal-El
Your daily schedule reminder  


## Installation 

To install Kal-El, 

```bash
git clone https://github.com/vs666/Kal-El.git
cd Kal-El
sudo ./setup.sh
```

#### Making a user on sql-server

Now installation will begin. It will also ask if you have a sql-server Database named as username@localhost. If yes, select -Y, else select -N

#### On selecting -N

If you have selected -N, you will need a password. This password will be used to access your sql-server user, and Kal-El account (stored locally).
The first password prompt will be your password for Kal-El and the sql-server user.
The second password will be for sudo (super user).

## Usage

To display all usage details

```bash

calel -h
```

To display today's events

```bash
 calel -s
```

To add a present/future event

```bash
calel -a
```


### In Case of Bugs


In case of bugs, please raise an issue on the github page
In case of Ideas for further improvisation or better implementation, raise an issue.
If you wish to collaborate and develop, raise an issue.

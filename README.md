# sshoney.py
### Simple SSH Honeypot for Capturing Credentials

#### $ nmap -p 22 -A localhost -Pn
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 7.4p1 Raspbian 10+deb9u2 (protocol 2.0)
####
    $ sudo python3 sshoney.py
####
    $ cat credentials.txt 
    127.0.0.1:user:asdfasdf asdf asdfa sdf
    127.0.0.1:user:#@#$@#$@#$f
    127.0.0.1:user:';oij';
# sshoney.py
### Simple SSH Honeypot for Capturing Credentials

#### $ nmap -p 22 -A localhost -Pn
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 7.4p1 Raspbian 10+deb9u2 (protocol 2.0)
####
    $ sudo python3 sshoney.py
####
    $ cat credentials.txt 
        user:asdf
        user:user
        user:jklj
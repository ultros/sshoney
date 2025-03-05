# sshoney.py
### Simple SSH Honeypot for Capturing Credentials
This Python script sets up a fake SSH server (honeypot) using Paramiko to log and monitor unauthorized login attempts. Instead of allowing SSH access, it records credentials entered by attackers and logs them for analysis.

#### Features
✅ Emulates an SSH server on port 22  
✅ Captures login attempts (username & password)  
✅ Logs credentials with timestamp & source IP  
✅ Fakes an OpenSSH banner (configurable)  
✅ Runs as a daemon on Debian (systemd compatible)  

#### How It Works
The script listens for SSH connections.  
When an attacker attempts to log in, it logs the username & password.  
Authentication always fails (it never grants access).  
Credentials are stored in /opt/sshoney/credentials.txt.  

---

### Install and Prepare the Script
    $ git clone https://github.com/ultros/sshoney /opt/sshoney
    $ cd /opt/sshoney
    $ python3 -m venv .venv
    $ ./.venv/bin/pip3 install -r /opt/sshoney/requirements.txt

### Generate an RSA keypair
You will generate a private key named "test" which the path of is hardcoded into the script. You will need to keep the private key "test" in the same directory as the sshoney.sh script.  

    $ ssh-keygen -f ./test
    > do not use a password

#### Run the Honeypot  
    $ sudo python3 sshoney.py
<br>

>[!TIP]
>Use nmap to determine if sshoney.py is running on port 22.
    
#### $ nmap -p 22 localhost
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 7.4p1 Raspbian 10+deb9u2 (protocol 2.0)
<br>

>[!TIP]
>Use "cat" to view the saved credentials file.
#### Test Connection and Log Test Credentials
    $ ssh user@localhost
    $ invalid password attempt
    
#### Print Out Credentials
    $ cat credentials.txt 
    127.0.0.1:user:password123
    127.0.0.1:user:#@#$@#$@#$f
    127.0.0.1:user:thequickbrownfox9876655asdf$

### Daemon Setup
If you want to install this as a service which runs after startup after your network is available, then follow these further instructions below.

    # vim /etc/systemd/system/sshoney.service

#### Daemon Skeleton
    [Unit]
    Description=sshoney.py
    After=network.target

    [Service]
    Type=simple
    ExecStart=/opt/sshoney/.venv/bin/python3 /opt/sshoney/sshoney.py
    Restart=always

    [Install]
    WantedBy=multi-user.target

### Daemon Setup (cont.)
    # systemctl enable /etc/systemd/system/sshoney.service
    # systemctl start /etc/systemd/system/sshoney.service
    # systemctl status /etc/systemd/system/sshoney.service

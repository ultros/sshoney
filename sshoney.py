#!/usr/bin/env python3
import socket
import paramiko
import datetime

# Use ssh-keygen to generate a key pair and provide the path to the private key here.
rsa_key = '/opt/sshoney/test'  # RSA host key
par_rsa_key = paramiko.RSAKey(filename=rsa_key)


class SshServer(paramiko.ServerInterface):
    """https://docs.paramiko.org/en/stable/api/server.html
    ServerInterface is an interface to override for server support.
    This class defines an interface for controlling the behavior of Paramiko in server mode.
    """

    def __init__(self, address):
        self.ipaddress = address[0]

    def check_auth_password(self, username, password):
        """Logs the attempted username and password.
        """
        with open('/opt/sshoney/credentials.txt', 'a') as file_obj:  # change the credentials location here
            file_obj.write(f"{datetime.datetime.now()}:{self.ipaddress}:{username}:{password}\n")

        return paramiko.common.AUTH_FAILED  # Always fail authentication.


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', 22))
    sock.listen()

    while True:
        try:
            client, address = sock.accept()
            transport = paramiko.Transport(client)
            transport.local_version = 'SSH-2.0-OpenSSH_7.4p1 Raspbian-10+deb9u2'
            transport.add_server_key(par_rsa_key)
            server = SshServer(address)
            transport.start_server(server=server)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

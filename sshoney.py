#!/usr/bin/env python3
import socket
import paramiko


# Use ssh-keygen to generate a key pair and provide the path to the private key here.
rsa_key = 'test'  # RSA host key
par_rsa_key = paramiko.RSAKey(filename=rsa_key)


class SshServer(paramiko.ServerInterface):
    """https://docs.paramiko.org/en/stable/api/server.html
    ServerInterface is an interface to override for server support.
    This class defines an interface for controlling the behavior of Paramiko in server mode.
    """

    def __init__(self):
        pass

    def check_auth_password(self, username, password):
        """Logs the attempted username and password.
        """
        with open('credentials.txt', 'a') as file_obj:
            file_obj.write(f"{username}:{password}\n")

        return paramiko.AUTH_FAILED  # Always fail authentication.


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse Address in case of "Address already in use"
    sock.bind(('', 22))
    sock.listen(100)

    while True:
        try:
            client, address = sock.accept()
            transport = paramiko.Transport(client)
            transport.add_server_key(par_rsa_key)
            server = SshServer()
            transport.start_server(server=server)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

from paramiko import SSHClient, AutoAddPolicy


class Ssh:
    def __init__(self, **kwargs):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        try:
            self.ssh.connect(
                hostname=kwargs["hostname"],
                username=kwargs["username"],
                password=kwargs["password"],
            )
        except Exception as ex:
            print(f"Error {ex}")

    def exec_cmd(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read())
        else:
            print(stdout.read())


if __name__ == "__main__":
    ssh = Ssh(hostname="127.0.0.1", username="root", password="test123")
    print(ssh.exec_cmd("ls"))

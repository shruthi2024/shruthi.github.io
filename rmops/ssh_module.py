import paramiko
import datetime

class SSHClient:
    def __init__(self, host, username, key_filename = None):
        self.hostname = host
        self.username = username
        self.key_filename = key_filename
        self.ssh_client = None
        self.log_filename = "log_file.txt" #+ str(datetime.datetime.now())

    def create_connection(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=self.hostname, username=self.username, key_filename=self.key_filename)


    def exec_command(self, commands):

        with open(self.log_filename, "w") as log_file:
            log_file.write(f"======Logs : {datetime.datetime.now()}=========")

            for command in commands:
                stdin, stdout, stderr = self.ssh_client.exec_command(command)
                cmd_op = stdout.read().decode("utf-8")
                err_op = stderr.read().decode("utf-8")

                if cmd_op:
                   log_file.write(command)
                   log_file.write(cmd_op)
                if err_op:
                   log_file.write(command)
                   log_file.write(err_op)

    def close(self):
        self.ssh_client.close()

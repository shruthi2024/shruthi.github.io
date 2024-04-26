import paramiko
import datetime

# define ssh connection parameters

host_ip = "3.91.81.26"

username="ec2-user"
key_file="Mac_EC2.pem"
log_file = "ssh_log.txt"

# List of commands to execute

commands = [
    "pwd",
    "ls -lrt",
    "df -kh",
    "upime",
    "ps -ef"
            ]


# Initialize ssh client

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# connect to remote host

ssh_client.connect(host_ip,username=username,key_filename=key_file)

# open log file in append mode

with open(log_file,"w") as file:
    file.write(f"**********SSH Log : {datetime.datetime.now()}************\n")

    # execute commands and write output to log file

    for command in commands:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        command_output = stdout.read().decode("utf-8")
        error_output = stderr.read().decode("utf-8")

        #write command output to log file

        if command_output:
            file.write("command\n")
            file.write(command)
            file.write(":\n")
            file.write(command_output)

        if error_output:
            file.write("error\n")
            file.write(command)
            file.write(":\n")
            file.write(error_output)


ssh_client.close()




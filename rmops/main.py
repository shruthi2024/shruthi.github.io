from ssh_module import SSHClient


HOST = "3.91.81.26"
USERNAME = "ec2-user"
PRIVATE_KEY = "/Users/apple/Documents/GitHub/shruthi2024.github.io/AWS/Mac_EC2.pem"
COMMANDS = [
    "pwd",
    "ls -lrt",
    "df -kh",
    "ps -ef",
    "uptime"
]

ssh_client = SSHClient(host=HOST, username=USERNAME, key_filename=PRIVATE_KEY)
ssh_client.create_connection()

# Example: execute a command on the remote server
ssh_client.exec_command(COMMANDS)

ssh_client.close()



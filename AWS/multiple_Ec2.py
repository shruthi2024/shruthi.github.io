import paramiko

# function to SS to EC2 instance/remote server  & execute set of commands

def ssh_execute(ec_ip, username, key_filename, commands):

    # create SSHClient

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:



        #connect to ec2 instance via ssh
        ssh_client.connect(ec_ip,username=username,key_filename=key_filename)

        print (ec_ip)
        #execute the commands

        for command in commands:
            print(f"Executing {command} on {ec_ip}")
            stdin, stdout, stderr = ssh_client.exec_command(command)

            #print output
            for line in stdout:
                print(line.strip())

            # check for any errors

            print(stderr.read().decode())

    except Exception as e:
        print(f"Error connecting to {ec_ip}:{e}")

    finally:
        ssh_client.close()

if __name__=="__main__":

    #EC2instance details

    instances = [
        "3.91.81.26",
        "3.91.81.26",
        "3.91.81.27"
    ]
    username = "ec2-user"
    key_filename =  "Mac_EC2.pem"

    commands=[
        "ls",
        "pwd",
        "df -kh"
    ]

    for instance in instances:
        ssh_execute(instance,username,key_filename,commands)






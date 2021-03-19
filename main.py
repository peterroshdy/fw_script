
import paramiko
import difflib


username = "root"
password = "P@622p@622"
server="172.105.248.237"
src_ip = "10.11.251.177"
dest_ip = "10.115.42.31"
d_port = "443"
first_interface = ""
second_interface = ""
first_zone = ""
second_zone = ""


def get__interface(host, username, password, lookup_ip):
    ## opens a ssh session to get the interface on the src ip
    cli = paramiko.client.SSHClient()
    cli.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    cli.connect(hostname=host, username=username, password=password)
    stdin_, stdout_, stderr_ = cli.exec_command("run show route "+lookup_ip)
    stdout_.channel.recv_exit_status()
    lines = stdout_.readlines()

    ## SPLIT THE OUTPUT AND GET THE CLOSEST MATCH TO "RETH"
    for line in lines:
        if(difflib.get_close_matches("reth", line.split())):
            interface = difflib.get_close_matches("reth", line.split())[0]
            return interface
    cli.close()

def get__zone(host, username, password, lookup_int):
    ## opens a ssh session to get the interface on the src ip
    cli = paramiko.client.SSHClient()
    cli.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    cli.connect(hostname=host, username=username, password=password)
    stdin_, stdout_, stderr_ = cli.exec_command("run show interfaces "+lookup_int)
    stdout_.channel.recv_exit_status()
    lines = stdout_.readlines()
    outputt  = []
    
    for line in lines:
        for word in line.split():
            outputt.append(word)
    first_zone = outputt[outputt.index("Zone:")+1]
    return first_zone
    
get__zone(server, username, password, "dasd")
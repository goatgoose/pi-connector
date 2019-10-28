import paramiko

IPS_FILE = open("ips.txt", "r")

EXECUTE_FILE_PATH = "execute.sh"

USERNAME = "pi"
PASSWORD = "piswitch"


for line in IPS_FILE:
    line = line.strip()
    if not line:
        continue

    line_split = line.split(" ")

    ip = line_split[-1]

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(hostname=ip, username=USERNAME, password=PASSWORD)

    ftp_client = ssh_client.open_sftp()
    ftp_client.put(EXECUTE_FILE_PATH, "execute.sh")
    ftp_client.close()

    print()
    print(ip)
    stdin, stdout, stderr = ssh_client.exec_command("sudo bash ./execute.sh", get_pty=True)
    print("STDOUT:")
    print(stdout.read().decode("utf-8"))
    print("STDERR:")
    print(stderr.read().decode("utf-8"))
    print("---------------------------------------------------\n")


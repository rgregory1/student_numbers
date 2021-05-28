import paramiko
from paramiko import sftp_client

import pathlib

import credentials

# setup connection


def grab_files(file_list, cwd):

    # Get files from RaspberryPi

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=credentials.pi_host,
        username=credentials.pi_user,
        password=credentials.pi_pass,
        port=22,
    )
    sftp_client = ssh.open_sftp()

    files = sftp_client.listdir()
    print(files)

    for file_name in file_list:
        sftp_client.get("/public/" + file_name, cwd / "data_files" / file_name)
        print(f"Retrieved {file_name} from remote")

    sftp_client.close()
    ssh.close()

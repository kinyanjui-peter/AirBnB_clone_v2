#!/usr/bin/python3
""" do_pack and do_deploy"""
from fabric.api import local, task, put, run, env
from datetime import datetime
import os
"""connection to server"""
env.hosts = ["18.209.225.212", "34.207.58.78"]
env.user = "ubuntu"
env.key_filename = "/home/peter/.ssh/school"


def do_pack():
    """ generate a content folder"""
    local("mkdir -p versions")
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    archiveName = f"web_static_{time}.tgz"
    archive_path = os.path.join("versions", archiveName)

    final = local(f"tar czvf {archive_path} web_static")

    if final.succeeded:
        print(f"{archive_path}")
        return archive_path
    else:
        print("None")
        return (final)



def do_deploy(archive_path):
    """Distribute an archive to your web servers"""
    try:
        if not os.path.exists(archive_path):
            print("False: Archive file does not exist.")
            return False

        # Extract filename without extension from the archive path
        extractedArchivePath = os.path.splitext(os.path.basename(archive_path))[0]

        # Upload the archive to the tmp directory
        put(archive_path, '/tmp/')
        run(f"sudo mkdir -p /data/web_static/releases/{extractedArchivePath}")
        run(f"sudo tar -xzvf /tmp/{extractedArchivePath}.tgz -C /data/web_static/releases/")

        # Remove the uploaded archive
        run(f"sudo rm /tmp/{extractedArchivePath}.tgz")

        # Remove symbolic link
        run("sudo rm -f /data/web_static/current")

        # Create new symbolic link
        run(f"sudo ln -s /data/web_static/releases/{extractedArchivePath} /data/web_static/current")

        print("True: Deployment successful.")
        return True

    except Exception as e:
        print(f"False: Error during deployment: {e}")
        return False
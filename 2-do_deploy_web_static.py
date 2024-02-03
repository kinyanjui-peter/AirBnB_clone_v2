#!/usr/bin/python3

from fabric.api import local, task, put, run, env
from datetime import datetime
import os

env.hosts = ["18.209.225.212", "34.207.58.78"]
env.user = ubuntu
env.key_filename = ssh -i .ssh/school


def do_pack():
    """ generate a content folder"""
    local("mkdir -p versions")
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    archiveName = f"web_static_{time}.tgz"
    archivePath = os.path.join("versions", archiveName)

    final = local(f"tar czvf {archivePath} web_static")

    if final.succeeded:
        print(f"{archivePath}")
        return archivePath
    else:
        print("None")
        return (final)



def do_deploy(archivePath):
    """Distribute an archive to your web servers"""
    try:
        if not os.path.exists(archivePath):
            print("False: Archive file does not exist.")
            return False

        # Extract filename without extension from the archive path
        extractedArchivePath = os.path.splitext(os.path.basename(archivePath))[0]

        # Upload the archive to the tmp directory
        put(archivePath, '/tmp/')
        run(f"sudo mkdir -p {extractedArchivePath}")
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
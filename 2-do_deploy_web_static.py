#!/usr/bin/python3

from fabric.api import local
from fabric import task, put, run, env
from datetime import datetime
import os

env.hosts = ["34.239.249.242", "34.207.58.78"]

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
    """distributes an archive to your web servers"""
    
    if not os.path.exists(archivePath):
        """check if the filepath exixt"""
        print("False")
        return False
    # extract file from archivepath without filename
    extractedArchivePath = os.path.basename(archivePath).split('0')[0]
    
    # upload the acrchive to the tmp directory  
    upload = put("archivePath" /tmp/)
    run(f"sudo mkdir -p extractedArchivePath")
    run(f"sudo tar -xzvf versions/web_static_20240203065022.tgz -C /data/web_static/releases/extractedArchivePath")

    # delete the archive from server 
    run(f"sudo rm {extractedArchivePath}.tgz")
    
    # delete symbolic link 
    run(f"sudo rm -f /data/web_static/current")
    
    # create new symbolic link
    run(f"sudo ln -s /data/web_static/releases/{extractedArchivePath} /data/web_static/current")
    
    print("true")
    return true

except Exception as e:
    print("False")
    return False

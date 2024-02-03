#!/usr/bin/python3

from fabric.api import local
from datetime import datetime
import os


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
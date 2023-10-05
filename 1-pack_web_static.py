#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from web_static"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of web_static"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        return None

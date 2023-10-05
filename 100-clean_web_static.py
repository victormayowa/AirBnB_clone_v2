#!/usr/bin/python3
"""Fabric script to clean up outdated archives"""

from fabric.api import env, local, run
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'


def do_clean(number=0):
    """Cleans up outdated archives"""
    number = int(number)
    if number < 2:
        number = 1
    else:
        number += 1

    local("ls -1t versions | tail -n +{} | xargs -I {{}} rm versions/{{}}"
          .format(number))

    run("ls -1t /data/web_static/releases | tail -n +{} | "
        "xargs -I {{}} rm -rf /data/web_static/releases/{{}}"
        .format(number))

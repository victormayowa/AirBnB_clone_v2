#!/usr/bin/python3
"""Fabric script to deploy the web_static archive"""

from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    """Deploys the web_static archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        filename = archive_path.split('/')[-1].split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(filename))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.format(
            filename, filename))
        run('rm /tmp/{}.tgz'.format(filename))
        run('mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/'.format(filename, filename))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ '
            '/data/web_static/current'.format(filename))

        return True

    except Exception as e:
        print(e)
        return False

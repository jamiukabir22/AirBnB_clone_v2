#!/usr/bin/python3
"""Create function to generate tgx file"""
from fabric.api import local
import time


def do_pack():
    """Generates tgz"""
    timestamp = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar-cvzf versions/web_static_{:s}.tgz web_static/".
                format(timestamp))
        return ("versions/web_static_{:s}.tgz".format(timestamp))
    except FileNotFoundError:
        return None

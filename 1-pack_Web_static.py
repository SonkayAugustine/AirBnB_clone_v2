#!/usr/bin/python3
'''
script that generates a .tgz archive from the contents of the web_static
'''
from fabric.api import *
import time
from os.path import isdir


def do_pack():
    ''' generates a .tgz archive'''
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static".forma(date))
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None

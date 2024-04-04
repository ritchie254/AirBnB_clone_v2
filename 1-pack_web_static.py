#!/usr/bin/python3
"""
fabric script to genenrate tgz achive of web_static folder
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    making an archive
    """
    tFormat = "%Y%m%d%H%M%S"
    time = datetime.now()
    archive = 'web_static_' + time.strftime(tFormat) + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None

#!/usr/bin/python
#-*- coding: UTF-8 -*-
from fabric.api import *
from fabric.contrib.console import confirm

@task
@runs_once
def tar_task():
    with lcd('/tmp/logs'):
        local('tar -czf access.tar.gz access.log')


@task
def put_task():
    run('mkdir -p /tmp/logs')
    with cd('/tmp/logs'):
        with settings(warn_only=True):
            result = put('/tmp/logs/access.tar.gz',
                    '/tmp/logs/access.tar.gz')
            if result.failed and not confirm('put file failed, Continue[Y/N]?'):
                abort('Aborting file put task!')


@task
def check_task():
    with settings(warn_only=True):
        lmd5 = local('md5sum /tmp/logs/access.tar.gz', capture=True).split(' ')[0]
        rmd5 = run('md5sum /tmp/logs/access.tar.gz').split(' ')[0]
        if lmd5 == rmd5:
            print 'OK'
        else:
            print 'Error'


@task
def go():
    execute(tar_task)
    execute(put_task)
    execute(check_task)

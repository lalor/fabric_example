import json
from fabric.api import run
from fabric.api import env

env.hosts = open('hosts').readlines()
env.port = 1046
env.user='rds-user'

print json.dumps(env, indent=4)

def hostname():
    run('hostname')

def ls(path='.'):
    run('ls {}'.format(path))

def tail(path='/etc/passwd', line=10):
    run('tail -n {0} {1}'.format(line, path))

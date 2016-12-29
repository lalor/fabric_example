import time

from fabric.api import run

def hostname():
    run('hostname')

def ls(path='.'):
    run('ls {}'.format(path))
    time.sleep(3)

def tail(path='/etc/passwd', line=10):
    run('tail -n {0} {1}'.format(line, path))

from fabric.api import run

def hostname():
    run('hostname')

def ls(path='.'):
    run('ls {}'.format(path))

def tail(path='/etc/passwd', line=10):
    run('tail -n {0} {1}'.format(line, path))

from fabric.api import (cd, run, task, env, roles, put, execute, parallel,
        hide, settings, sudo)
from fabric.colors import red, green
from fabric.contrib.files import exists


@task
def upload():
    put('run.py', '/tmp/run.py')

def check_command(cmd):
    rs = run('{0} --help >/dev/null 2>&1'.format(cmd))
    return rs.return_code == 0


@task
def install_it(package):
    sudo('pip install {0}'.format(package))
    print green('{0} installed'.format(package))


@task
def restart_app():
    with cd('/tmp'):
        if exists('/tmp/app.pid'):
            pid = run('cat /tmp/app.pid')
            run('kill -9 {}; rm /tmp/app.pid'.format(pid))
        else:
            print red('pid file not exists!')

        with settings(hide('everything'), warn_only=True):
            if not check_command('gunicorn'):
                install_it('gunicorn')

        run('nohup gunicorn -w 3 run:app -b 0.0.0.0:8000 -D -p /tmp/app.pid --log-file /tmp/app.log &')


@task
def depoly():
    execute(upload)
    execute(restart_app)

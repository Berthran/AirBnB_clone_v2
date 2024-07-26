from fabric import task
from invoke import run

@task
def whoami(c):
    result = run('whoami', hide=True)
    print("Local user:", result.stdout.strip())


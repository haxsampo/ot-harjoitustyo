from invoke import task
import os
import platform

@task
def foo(ctx):
    print("bar")

@task 
def start(ctx):
    if platform.system() == 'Windows':
        ctx.run("py src/index.py")
    else:
        ctx.run("python3 src/index.py")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")
    
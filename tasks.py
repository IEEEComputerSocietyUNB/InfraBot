from invoke import task


@task
def run(c):
    """ Run bot.py """
    c.run('python bot.py')
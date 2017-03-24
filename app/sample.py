import os


def sample_func():
    env = os.environ.get('ENV1')
    return 'Env is "{}"'.format(env)


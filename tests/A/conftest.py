import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

if os.environ.get('ENV1') != 'env1-for-test':
    raise Exception('ENV1 does not equal env1-for-test')

if os.environ.get('ENV2') != 'env2':
    raise Exception('ENV2 does not equal env2')

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or\
    'bf2wsetr92137ry3497fvf743fc'
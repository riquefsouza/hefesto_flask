#import os.path
#basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dbhefesto.sqlite')
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:abcd1234@localhost/dbhefesto"
SQLALCHEMY_TRACK_MODIFICATIONS = True

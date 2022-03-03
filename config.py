class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/todolistdb"
    SQLALCHEMY_POOL_SIZE = 50
    SQLALCHEMY_POOL_TIMEOUT = 300
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "horrible_secret_key"

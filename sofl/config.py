class BaseConfig():
    DEBUG = False
    SECRET_KEY = 'this is to be kept secret'

class Development(BaseConfig):
    DEBUG = True
    DATABASE = 'development.db'

class Testing(BaseConfig):
    TESTING = True
    DATABASE = 'testing.db'

class Production(BaseConfig):
    pass

CONFIG = {
   'development':   Development,
   'testing': Testing,
   'production': Production
}
class BaseConfig():
    DEBUG = False
    
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
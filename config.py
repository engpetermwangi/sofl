class BaseConfig():
    DEBUG = False
    
class Development(BaseConfig):
    DEBUG = True

class Testing(BaseConfig):
    TESTING = True

class Production(BaseConfig):
    pass

CONFIG = {
   'development':   Development,
   'testing': Testing,
   'production': Production
}
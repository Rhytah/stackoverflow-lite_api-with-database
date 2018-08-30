class Config:
    DEBUG=False
    TESTING = False
    CSRF_ENABLED=True
    SECRET= 'secresthere'
    



class DevelopmentConfig(Config):
    DEBUG=True

class TestingConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False


app_configuration = {

    "development":DevelopmentConfig,

    "testing":TestingConfig,
    "production":ProductionConfig

}


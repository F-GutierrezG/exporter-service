import os


class BaseConfig:
    """ Base configuration """
    TESTING = False
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(BaseConfig):
    """ Development configuration """
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class TestingConfig(BaseConfig):
    """ Testing configuration """
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class StagingConfig(BaseConfig):
    """ Staging configuration """
    pass


class ProductionConfig(BaseConfig):
    """ Production configuration """
    DEBUG = False

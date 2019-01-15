import os


class BaseConfig:
    """ Base configuration """
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    USERS_SERVICE_MOCK = False
    COMPANIES_SERVICE_MOCK = False
    SOCIAL_SERVICE_MOCK = False
    AUTH_SERVICE_URL = os.environ.get('AUTH_SERVICE_URL')
    USERS_SERVICE_URL = os.environ.get('USERS_SERVICE_URL')
    COMPANIES_SERVICE_URL = os.environ.get('COMPANIES_SERVICE_URL')
    SOCIAL_SERVICE_URL = os.environ.get('SOCIAL_SERVICE_URL')


class DevelopmentConfig(BaseConfig):
    """ Development configuration """
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    USERS_SERVICE_MOCK = False
    COMPANIES_SERVICE_MOCK = False
    SOCIAL_SERVICE_MOCK = False


class TestingConfig(BaseConfig):
    """ Testing configuration """
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    USERS_SERVICE_MOCK = True
    COMPANIES_SERVICE_MOCK = True
    SOCIAL_SERVICE_MOCK = True


class StagingConfig(BaseConfig):
    """ Staging configuration """
    USERS_SERVICE_MOCK = False
    COMPANIES_SERVICE_MOCK = False
    SOCIAL_SERVICE_MOCK = False


class ProductionConfig(BaseConfig):
    """ Production configuration """
    DEBUG = False
    USERS_SERVICE_MOCK = False
    COMPANIES_SERVICE_MOCK = False
    SOCIAL_SERVICE_MOCK = False

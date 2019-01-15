from flask import current_app
from .services import SocialServiceMock, SocialService


class SocialServiceFactory:
    def get_instance():
        if current_app.config['SOCIAL_SERVICE_MOCK']:
            return SocialServiceMock.get_instance()
        return SocialService()

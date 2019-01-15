import json
import requests

from flask import request, current_app


class SocialService:
    def get_publications(self):
        url = '{}/publications'.format(
            current_app.config['SOCIAL_SERVICE_URL'])
        bearer = request.headers.get('Authorization')
        headers = {'Authorization': bearer}
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        return response, data


class Response:
    status_code = 200


class SocialServiceMock:
    instance = None

    def __init__(self):
        self.clear()

    def clear(self):
        self.publications = []

    @staticmethod
    def get_instance():
        if SocialServiceMock.instance is None:
            SocialServiceMock.instance = SocialServiceMock()
        return SocialServiceMock.instance

    def add_company(self, publication):
        self.publications.append(publication)

    def set_publications(self, publications):
        self.publications = publications

    def get_publications(self):
        publications = []
        for publication in self.publications:
            publications.append(publication)
        return Response(), publications

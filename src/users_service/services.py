import json
import requests

from flask import request, current_app


class UsersService:
    def get(self, id):
        url = '{0}/{1}'.format(
            current_app.config['USERS_SERVICE_URL'], id)
        bearer = request.headers.get('Authorization')
        headers = {'Authorization': bearer}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.text)
        else:
            data = None
        return response, data

    def filter_by_ids(self, ids=[]):
        url = '{0}/byIds/{1}'.format(
            current_app.config['USERS_SERVICE_URL'],
            ','.join(str(v) for v in ids))
        bearer = request.headers.get('Authorization')
        headers = {'Authorization': bearer, 'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        return response, data

    def get_admin_users(self):
        url = '{0}/admins'.format(
            current_app.config['USERS_SERVICE_URL'])
        bearer = request.headers.get('Authorization')
        headers = {'Authorization': bearer}
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        return response, data

    def create_user(self, user_data):
        url = '{0}'.format(current_app.config['USERS_SERVICE_URL'])
        bearer = request.headers.get('Authorization')
        headers = {'Authorization': bearer, 'Content-Type': 'application/json'}
        response = requests.post(
            url, headers=headers, data=json.dumps(user_data))
        data = json.loads(response.text)
        return response, data


class Response:
    status_code = 200


class UsersServiceMock:
    instance = None

    def __init__(self):
        self.clear()

    def clear(self):
        self.users = []
        self.user = None

    @staticmethod
    def get_instance():
        if UsersServiceMock.instance is None:
            UsersServiceMock.instance = UsersServiceMock()
        return UsersServiceMock.instance

    def set_user(self, user):
        self.user = user

    def set_users(self, users):
        self.users = users

    def add_user(self, user):
        self.users.append(user)

    def filter_by_ids(self, ids=[]):
        users = []
        for user in self.users:
            if user['id'] in ids:
                users.append(user)
        return Response(), users

    def get_admin_users(self):
        users = []
        for user in self.users:
            if user['admin']:
                users.append(user)
        return Response(), users

    def get(self, id):
        return self.user

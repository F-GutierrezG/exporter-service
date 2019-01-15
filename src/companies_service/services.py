import json
import requests

from flask import request, current_app


class CompaniesService:
    def get_companies(self):
        url = current_app.config['COMPANIES_SERVICE_URL']
        bearer = request.headers.get('Authorization')
        headers = {'Authorization': bearer}
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        return response, data

    def get_company_users(self, company_id):
        url = '{}/{}/users'.format(
            current_app.config['COMPANIES_SERVICE_URL'],
            company_id)
        bearer = request.headers.get('Authorization')
        headers = {'Authorization': bearer}
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        return response, data


class Response:
    status_code = 200


class CompaniesServiceMock:
    instance = None

    def __init__(self):
        self.clear()

    def clear(self):
        self.companies = []
        self.users = []

    @staticmethod
    def get_instance():
        if CompaniesServiceMock.instance is None:
            CompaniesServiceMock.instance = CompaniesServiceMock()
        return CompaniesServiceMock.instance

    def set_companies(self, companies):
        self.companies = companies

    def add_company(self, company):
        self.companies.append(company)

    def set_users(self, users):
        self.users = users

    def get_companies(self):
        companies = []
        for company in self.companies:
            companies.append(company)
        return Response(), companies

    def get_company_users(self, company_id):
        users = []
        for user in self.users:
            users.append(user)
        return Response(), users

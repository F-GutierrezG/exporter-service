import io
import csv
from users_service.factories import UsersServiceFactory
from companies_service.factories import CompaniesServiceFactory


class AdminLogics:
    def csv(self):
        _, admins = UsersServiceFactory.get_instance().get_admin_users()

        file = io.StringIO()
        writer = csv.writer(file)

        writer.writerow(self.__get_admins_header())

        for admin in admins:
            writer.writerow(self.__get_row(admin))

        return file.getvalue()

    def __get_admins_header(self):
        return ['ID', 'NOMBRE', 'APELLIDO', 'E-MAIL','FECHA EXPIRACION','ESTADO USUARIO','FECHA CREACION','CREADO POR','FECHA DE ACTUALIZACION','ACTUALIZADO POR']

    def __get_row(self, admin):
        row = []
        row.append(admin['id'])
        row.append(admin['first_name'])
        row.append(admin['last_name'])
        row.append(admin['email'])
        row.append(admin['expiration'])
        row.append(admin['active'])
        row.append(admin['created'])
        row.append(admin['created_by'])
        row.append(admin['updated'])
        row.append(admin['updated_by'])

        return row


class CompaniesLogics:
    def csv(self):
        _, companies = CompaniesServiceFactory.get_instance().get_companies()

        file = io.StringIO()
        writer = csv.writer(file)

        writer.writerow(self.__get_companies_header())

        for company in companies:
            for user in self.__get_users(company['id']):
                writer.writerow(self.__get_row(company, user))

        return file.getvalue()

    def __get_users(self, company_id):
        _, users = CompaniesServiceFactory.get_instance().get_company_users(
            company_id)

        return users

    def __get_companies_header(self):
        return ['ID', 'IDENTIFICADOR', 'RAZON SOCIAL','GIRO','FECHA DE CREACION','EMPRESA CREADA POR','FECHA ULTIMA ACTUALIZACION','ACTUALIZADO POR','ID', 'NOMBRE', 'APELLIDO', 'E-MAIL','FECHA EXPIRACION','ESTADO USUARIO','FECHA CREACION','CREADO POR','FECHA DE ACTUALIZACION','ACTUALIZADO POR']

    def __get_row(self, company, user):
        row = []
        row.append(company['id'])
        row.append(company['identifier'])
        row.append(company['name'])
        row.append(company['classification']['name'])
        row.append(company['created'])
        row.append(company['created_by'])
        row.append(company['updated'])
        row.append(company['updated_by'])
        row.append(user['id'])
        row.append(user['first_name'])
        row.append(user['last_name'])
        row.append(user['email'])
        row.append(user['expiration'])
        row.append(user['active'])
        row.append(user['created'])
        row.append(user['created_by'])
        row.append(user['updated'])
        row.append(user['updated_by'])

        return row

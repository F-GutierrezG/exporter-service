import io
import csv
from users_service.factories import UsersServiceFactory
from companies_service.factories import CompaniesServiceFactory
from social_service.factories import SocialServiceFactory


class BaseLogics:
    def _get_user_names(self, id):
        _, user = UsersServiceFactory.get_instance().get(id)

        if user:
            return "{} {}".format(user['first_name'], user['last_name'])

        return ""


class AdminLogics(BaseLogics):
    def csv(self):
        _, admins = UsersServiceFactory.get_instance().get_admin_users()

        file = io.StringIO()
        writer = csv.writer(
            file, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)

        writer.writerow(self.__get_admins_header())

        for admin in admins:
            writer.writerow(self.__get_row(admin))

        return file.getvalue()

    def __get_admins_header(self):
        return ['ID', 'NOMBRE', 'APELLIDO', 'E-MAIL',
                'FECHA EXPIRACION', 'ESTADO USUARIO', 'FECHA CREACION',
                'CREADO POR', 'FECHA DE ACTUALIZACION', 'ACTUALIZADO POR']

    def __get_row(self, admin):
        row = []
        row.append(admin['id'])
        row.append(admin['first_name'])
        row.append(admin['last_name'])
        row.append(admin['email'])
        row.append(admin['expiration'])
        row.append(admin['active'])
        row.append(admin['created'])
        row.append(self._get_user_names(admin['created_by']))
        row.append(
            "" if admin['updated'] == "None" else admin['updated'])
        row.append(self._get_user_names(admin['updated_by']))

        return row


class CompaniesLogics(BaseLogics):
    def csv(self):
        _, companies = CompaniesServiceFactory.get_instance().get_companies()

        file = io.StringIO()
        writer = csv.writer(
            file, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)

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
        return ['ID', 'IDENTIFICADOR', 'RAZON SOCIAL',
                'GIRO', 'ID', 'NOMBRE', 'APELLIDO', 'E-MAIL',
                'FECHA EXPIRACION', 'ESTADO USUARIO', 'EMPRESA CREADA POR',
                'FECHA DE CREACION', 'ACTUALIZADO POR',
                'FECHA ULTIMA ACTUALIZACION']

    def __get_row(self, company, user):
        row = []
        row.append(company['id'])
        row.append(company['identifier'])
        row.append(company['name'])
        row.append(company['classification']['name'])
        row.append(user['id'])
        row.append(user['first_name'])
        row.append(user['last_name'])
        row.append(user['email'])
        row.append(user['expiration'])
        row.append(user['active'])
        row.append(self._get_user_names(company['created_by']))
        row.append(company['created'])
        row.append(
            "" if company['updated'] == "None" else company['updated'])
        row.append(self._get_user_names(company['updated_by']))
        row.append(company['updated'])

        return row


class CompanyUsersLogics(BaseLogics):
    def csv(self, company_id):
        _, users = CompaniesServiceFactory.get_instance().get_company_users(
            company_id)

        file = io.StringIO()
        writer = csv.writer(
            file, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)

        writer.writerow(self.__get_user_header())

        for user in users:
            writer.writerow(self.__get_row(user))

        return file.getvalue()

    def __get_user_header(self):
        return ['ID', 'NOMBRE', 'APELLIDO', 'E-MAIL', 'FECHA EXPIRACION',
                'ESTADO USUARIO', 'FECHA CREACION', 'CREADO POR',
                'FECHA DE ACTUALIZACION', 'ACTUALIZADO POR']

    def __get_row(self, admin):
        row = []
        row.append(admin['id'])
        row.append(admin['first_name'])
        row.append(admin['last_name'])
        row.append(admin['email'])
        row.append(admin['expiration'])
        row.append(admin['active'])
        row.append(admin['created'])
        row.append(self._get_user_names(admin['created_by']))
        row.append(
            "" if admin['updated'] == "None" else admin['updated'])
        row.append(self._get_user_names(admin['updated_by']))

        return row


class PublicationsLogics(BaseLogics):
    def csv(self):
        service = SocialServiceFactory.get_instance()
        _, publications = service.get_publications()

        file = io.StringIO()
        writer = csv.writer(
            file, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)

        writer.writerow(self.__get_publication_header())

        for publication in publications:
            for network in publication['social_networks']:
                rows = self.__get_row(publication, network)
                for row in rows:
                    writer.writerow(row)

        return file.getvalue()

    def __get_publication_header(self):
        return ['ID', 'TITLE', 'ID COMPANIA', 'IDENTIFICAROD', 'RAZON SOCIAL',
                'TEXTO ADICIONAL', 'CONTENIDO', 'REFERENCIA RED SOCIAL',
                'MESSAGE', 'STATUS', 'FECHA DE PUBLICACION', 'FECHA CREACION',
                'CREADO POR', 'FECHA ACTUALIZACION', 'ACTUALIZADOR POR',
                'RED SOCIAL', 'TAG']

    def __get_row(self, publication, network):
        row = []

        if len(publication['tags']) > 0:
            for tag in publication['tags']:
                row.append(self.__get_row_with_tag(publication, network, tag))
        else:
            row.append(self.__get_row_with_tag(publication, network))

        return row

    def __get_row_with_tag(self, publication, network, tag=""):
        service = CompaniesServiceFactory.get_instance()
        _, company = service.get_company(publication['company_id'])

        row = []

        row.append(publication['id'])
        row.append(publication['title'])
        row.append(publication['company_id'])
        row.append(company['identifier'])
        row.append(company['name'])
        row.append(publication['additional'])
        row.append(publication['image_url'])
        row.append(publication['link'])
        row.append(
            publication['message'].replace(
                "'", '"').strip().replace("\n", " ").replace("\r", ''))
        row.append(publication['status'])
        row.append(publication['date'])
        row.append(publication['created'])
        row.append(self._get_user_names(publication['created_by']))
        row.append(
            "" if publication['updated'] == "None" else publication['updated'])
        row.append(self._get_user_names(publication['updated_by']))
        row.append(network)
        row.append(tag)

        return row

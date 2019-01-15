import io
import csv
from users_service.factories import UsersServiceFactory


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

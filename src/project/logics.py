from users_service.factories import UsersServiceFactory


class UserLogics:
    def admins_csv(self):
        admins = UsersServiceFactory.get_instance().get_admin_users()

        print('*****', admins)
        header = "id,nombre,apellido"

        return header

from flask import Blueprint, Response

from project.logics import UserLogics


users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/exporter/users', methods=['GET'])
def health():
    csv = UserLogics().admins_csv()
    return Response(csv, mimetype="text/csv")

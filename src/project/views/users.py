from flask import Blueprint, Response

from project.logics import AdminLogics

from auth.decorators import authenticate


users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/exporter/admins', methods=['GET'])
@authenticate
def admins(user):
    csv = AdminLogics().csv()
    return Response(
        csv.encode('utf-16'), mimetype="text/csv; charset='utf-16'")

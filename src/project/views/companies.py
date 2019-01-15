from flask import Blueprint, Response

from project.logics import CompaniesLogics

from auth.decorators import authenticate


companies_blueprint = Blueprint('companies', __name__)


@companies_blueprint.route('/exporter/companies', methods=['GET'])
@authenticate
def companies(user):
    csv = CompaniesLogics().csv()
    return Response(
        csv.encode('utf-16'), mimetype="text/csv; charset='utf-16'")

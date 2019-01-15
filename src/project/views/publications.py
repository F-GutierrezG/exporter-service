from flask import Blueprint, Response

from project.logics import PublicationsLogics

from auth.decorators import authenticate


publications_blueprint = Blueprint('publications', __name__)


@publications_blueprint.route('/exporter/publications', methods=['GET'])
@authenticate
def publications(user):
    csv = PublicationsLogics().csv()
    return Response(
        csv.encode('utf-16'), mimetype="text/csv; charset='utf-16'")

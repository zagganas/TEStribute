import json

from werkzeug.exceptions import (BadRequest, InternalServerError)

from TEStribute import rank_services
from TEStribute.errors import (ResourceUnavailableError, ValidationError)


def RankServices(body):

    ranked_response = __post_rank_services(body)

    # TODO:
    #   handle FileNotFoundError

    return ranked_response


def __post_rank_services(params):

    try:
        response = rank_services(
            drs_ids=params.get("drs_ids"),
            drs_uris=params.get("drs_uris"),
            mode=params.get("mode"),
            resource_requirements=params.get("resource_requirements"),
            tes_uris=params.get("tes_uris")
        )
    except ValidationError as e:
        raise BadRequest(e.args) from e
    except ResourceUnavailableError as e:
        raise BadRequest(e.args) from e
    except Exception as e:
        raise InternalServerError(e.args) from e

    return response

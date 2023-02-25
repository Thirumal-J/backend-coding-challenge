"""
Exposes a simple HTTP API to search a users Gists via a regular expression.

Github provides the Gist service as a pastebin analog for sharing code and
other develpment artifacts.  See http://gist.github.com for details.  This
module implements a Flask server exposing two endpoints: a simple ping
endpoint to verify the server is up and responding and a search endpoint
providing a search across all public Gists for a given Github account.
"""

import requests
from flask import Flask, jsonify, request
from helpers import handle_error_response, search_gist_for_pattern, paginate_data
from models import GistSearchRequest
import config

app = Flask(__name__)


@app.route("/ping")
def ping() -> str:
    """Provide a static response to a simple GET request."""
    return "pong"


def gists_for_user(username: str) -> dict:
    """Provides the list of gist metadata for a given user.

    This abstracts the /users/:username/gist endpoint from the Github API.
    See https://developer.github.com/v3/gists/#list-a-users-gists for
    more information.

    Args:
        username (string): the user to query gists for

    Returns:
        The dict parsed from the json response from the Github API.  See
        the above URL for details of the expected structure.
    """
    gists_url = config.GITHUB_GISTS_URL.format(username=username)
    response = requests.get(gists_url)
    return response.json()


@app.route("/api/v1/search", methods=["POST"])
def search() -> tuple[dict, int]:
    """Provides matches for a single pattern across a single users gists.

    Pulls down a list of all gists for a given user and then searches
    each gist for a given regular expression.

    Returns:
        A Flask Response object of type application/json.  The result
        object contains the list of matches along with a 'status' key
        indicating any failure conditions.
    """
    post_data = request.get_json()

    """Validate the input data"""
    try:
        gist_search_request = GistSearchRequest.parse_obj(post_data)
    except Exception as e:
        print(f"\nError during validation--{str(e)}")
        return jsonify(handle_error_response(config.ERROR, config.VALIDATION_ERROR_MSG))

    username = gist_search_request.username
    pattern = gist_search_request.pattern
    page = gist_search_request.page
    limit = gist_search_request.limit
    include_file_info = gist_search_request.include_file_info

    result = {}

    """Fetching all the gists for the given username"""
    try:
        gists = gists_for_user(username)
    except Exception as e:
        print(f"\nError occurred fetching gists--{str(e)}")
        return jsonify(
            handle_error_response(config.ERROR, config.FETCH_GISTS_ERROR_MSG)
        )

    """Searching pattern in all the files inside all the gists for the given username"""
    matched_gists = []
    try:
        for gist in gists:
            matched_gist_info = []
            matched_gist_info = search_gist_for_pattern(
                gist, pattern, include_file_info
            )
            if len(matched_gist_info) > 0:
                matched_gists.append(matched_gist_info)
    except Exception as e:
        print(f"\nError occurred searching pattern in gist-- {str(e)}")
        return jsonify(
            handle_error_response(config.ERROR, config.SEARCH_GISTS_ERROR_MSG)
        )

    paginated_matched_gists = paginate_data(matched_gists, page, limit)

    result["status"] = config.SUCCESS
    result["username"] = username
    result["pattern"] = pattern
    result["matched_gists"] = paginated_matched_gists
    result["code"] = 200
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host=config.HOST, port=config.PORT_NUMBER)

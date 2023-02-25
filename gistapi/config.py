# URL for GitHub Gists API
GITHUB_GISTS_URL = "https://api.github.com/users/{username}/gists"

# Timeout for HTTP requests
TIMEOUT = 50

# Pagination defaults
PAGE = 1
LIMIT = 10

# Server settings
PORT_NUMBER = 9876
HOST = "0.0.0.0"

# Error messages
VALIDATION_ERROR_MSG = "Missing username or pattern field"
INVALID_INPUT_ERROR_MSG = "Invalid input"
FETCH_GISTS_ERROR_MSG = "Error occurred during fetching gists of the given user"
SEARCH_GISTS_ERROR_MSG = "Error occurred during gist search"

# Response status
SUCCESS = "success"
ERROR = "error"

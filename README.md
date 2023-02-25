# Challenge

This challenge is divided between the main task and additional stretch goals. All of those stretch goals are optional, but we would love to see them implemented. It is expected that you should be able to finish the challenge in about 1.5 hours. If you feel you are not able to implement everything on time, please, try instead describing how you would solve the points you didn't finish.

And also, please do not hesitate to ask any questions. Good luck!

## gistapi

Gistapi is a simple HTTP API server implemented in Flask for searching a user's public Github Gists.
The existing code already implements most of the Flask boilerplate for you.
The main functionality is left for you to implement.
The goal is to implement an endpoint that searches a user's Gists with a regular expression.
For example, I'd like to know all Gists for user `justdionysus` that contain the pattern `import requests`.
The code in `gistapi.py` contains some comments to help you find your way.

To complete the challenge, you'll have to write some HTTP queries from `Gistapi` to the Github API to pull down each Gist for the target user.
Please don't use a github API client (i.e. using a basic HTTP library like requests or aiohttp or urllib3 is fine but not PyGithub or similar).


## Stretch goals

* Implement a few tests (using a testing framework of your choice)
* In all places where it makes sense, implement data validation, error handling, pagination
* Migrate from `requirements.txt` to `pyproject.toml` (e.g. using [poetry](https://python-poetry.org/))
* Implement a simple Dockerfile
* Implement handling of huge gists
* Set up the necessary tools to ensure code quality (feel free to pick up a set of tools you personally prefer)
* Document how to start the application, how to build the docker image, how to run tests, and (optionally) how to run code quality checkers
* Prepare a TODO.md file describing possible further improvements to the archtiecture:
    - Can we use a database? What for? SQL or NoSQL?
    - How can we protect the api from abusing it?
    - How can we deploy the application in a cloud environment?
    - How can we be sure the application is alive and works as expected when deployed into a cloud environment?
    - Any other topics you may find interesting and/or important to cover


## Thought process

* Implement a model class using pydantic. Created a request search body, which makes input data validation easy. Can also be extended with custom messages if needed.
* Implemented a helper class to handle errors and a method to search pattern  in a gist
* Used a optional boolean parameter named `include_file_info` in the search api which is by default `False`. In case if the API request only needs gist with a pattern match, on the first match the loop will break, and sends only the matched gist ids. This helps in faster response and avoids sending unnecessary file_info making the service consume less memory. In case if the user needs all the matched gists including all the matched file infos within each gist, then setting up `inlcude_file_info` as `True` will give gist id with the all the file info in which pattern is found.
* Used config.py file to keep all the application configurations such as server settings, error messages, github gists url, pagination parameters, response status. This helps in increasing readability, security, and makes it a easier to maintain the application settings from one place.

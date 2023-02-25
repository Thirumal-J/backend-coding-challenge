## Thought process

* Implement a model class using pydantic. Created a request search body, which makes input data validation easy. Can also be extended with custom messages if needed.
* Implemented a helper class to handle errors and a method to search pattern  in a gist
* Used a optional boolean parameter named `include_file_info` in the search api which is by default `False`. In case if the API request only needs gist with a pattern match, on the first match the loop will break, and sends only the matched gist ids. This helps in faster response and avoids sending unnecessary file_info making the service consume less memory. In case if the user needs all the matched gists including all the matched file infos within each gist, then setting up `inlcude_file_info` as `True` will give gist id with the all the file info in which pattern is found.
* Used config.py file to keep all the application configurations such as server settings, error messages, github gists url, pagination parameters, response status. This helps in increasing readability, security, and makes it a easier to maintain the application settings from one place.

## Docker

* Use command `docker compose --build --no-cache` to build the docker container for the project
* Once it is completed, use command `docker compose up` to run the docker container
* Docker container should run the api in the http://localhost:9876/

# Code quality
* Used flake8 for managing the code quality



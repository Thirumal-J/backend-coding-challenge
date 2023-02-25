from pydantic import BaseModel
import config


class GistSearchRequest(BaseModel):
    username: str
    pattern: str
    page: int = config.PAGE
    limit: int = config.LIMIT
    include_file_info: bool = False

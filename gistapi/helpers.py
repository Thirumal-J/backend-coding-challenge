from typing import List
import requests
import re
import config


def handle_error_response(status: str, message: str, code: int = 400) -> dict:
    """Handle error response"""
    return {"status": status, "message": message, "code": code}


def search_gist_for_pattern(gist: dict, pattern: str, include_file_info: bool) -> dict:
    """Search for pattern in a gist"""
    gist_with_info = {}
    matched_files = []

    for file_name, file_info in gist["files"].items():
        raw_content = requests.get(
            file_info["raw_url"], stream=True, timeout=config.TIMEOUT
        ).content.decode("utf-8", errors="ignore")
        if re.search(pattern, raw_content):
            matched_files.append(file_info)
            if not include_file_info:
                gist_with_info = {"gist_id": gist["id"]}
                return gist_with_info

    if len(matched_files) > 0 and include_file_info:
        gist_with_info = {"gist_id": gist["id"], "matched_gist_files": matched_files}
        return gist_with_info


def paginate_data(data: List, page: int, limit: int) -> List:
    """Paginate data"""
    start_index = (page - 1) * limit
    end_index = start_index + limit
    return data[start_index:end_index]

import requests
import json

from typing import Union
from json.decoder import JSONDecodeError

from instalic.exceptions import UserDoesNotExist
from instalic.func.conf import *
from instalic.utils import gen_token, random_useragent

class User:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def get_id_from_username(self, username: str):
        """
        Get ID from specified username
        """
        headers = {
            "x-requested-with": "XMLHttpRequest",
            "x-csrftoken": gen_token(),
            "Connection": "Keep-Alive",
            "Accept": "*/*",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "en-US",
            "User-Agent": (
                random_useragent()
            ),
        }
        response = requests.get(
            url=CONF_web_profile_info_API.format(username),
            headers=headers
        )
        try:
            return response.json()
        except JSONDecodeError as e:
            with open('error.txt', 'w') as f:
                f.write(response.text)
            raise UserDoesNotExist
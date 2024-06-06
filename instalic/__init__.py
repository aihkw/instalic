from requests import Session
from urllib.parse import urlparse

from instalic.func import conf
from instalic.func.user import User

class Client(User):
    def __init__(
        self,
        delay_range: list = None,
        keep_session: bool = True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        conf.CONF_keep_session = keep_session
from typing import List
from application import path
from . import api

apipatterns: List = [
    path("mobile", api.check_mobile)
]

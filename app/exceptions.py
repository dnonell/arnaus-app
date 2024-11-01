from app import constants


class SessionNotFound(Exception):
    def __init__(self):
        super().__init__(constants.SESSION_NOT_FOUND)

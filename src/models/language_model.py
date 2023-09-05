from database.db import db

from .abstract_model import AbstractModel


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        self.name = data["name"]
        self.acronym = data["acronym"]

    # Req. 2
    def to_dict(self):
        return {
            "name": self.name,
            "acronym": self.acronym,
        }

    # Req. 3
    @classmethod
    def list_dicts(cls):
        raise NotImplementedError

#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            dtformat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.strptime(value, dtformat))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        name = self.__class__.__name__
        return (f"[{name}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return (my_dict)

#!/usr/bin/python3
""" Serialization and Desirialization Module """
import json


class FileStorage:
    """ FileStorage Engine Class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Gets the dict of objects method """
        return (type(self).__objects)

    def new(self, obj):
        """ Sets obj in __objects method """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize __objects to a JSON file method """
        my_dict = []
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """ Desirialize JSON file to __objects method """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                object_dict = json.load(f)
                for key, value in object_dict.items():
                    name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(name)(**value))
        except FileNotFoundError:
            pass

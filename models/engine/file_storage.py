#!/usr/bin/python3
""" Serialization and Desirialization Module """
from models.base_model import BaseModel
import json


class FileStorage:
    """ FileStorage Engine Class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Gets the dict of objects method """
        return (FileStorage.__objects)

    def new(self, obj):
        """ Sets obj in __objects method """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize __objects to a JSON file method """
        obj_dict = FileStorage.__objects
        my_dict = {}
        """print(obj_dict)
        print()"""
        for key in obj_dict.keys():
            my_dict = {key: obj_dict[key].to_dict()}
            """print(key, obj_dict[key], obj_dict[key].to_dict)
            print()
            print(my_dict)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """ Desirialize JSON file to __objects method """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                object_dict = json.load(file)
                for value in object_dict.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass

#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}


    def all(self):
        return (FileStorage.__objects)

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        my_dict = FileStorage.__objects
        obj_dict = {key: obj.to_dict() for key, obj in my_dict.items()}

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                my_dict = json.load(file)

                for k, v in my_dict.items():
                    class_name = v["__class__"]
                    FileStorage.__objects = eval(class_name)(**v)

        except FileNotFoundError:
            pass

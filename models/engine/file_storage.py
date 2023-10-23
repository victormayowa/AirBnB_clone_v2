#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        else:
            cls_dict = {}
            for key, value in self.__objects.items():
                key_split = key.split('.')[0]
                if key_split == cls.__name__:
                    cls_dict[key] = value
            return cls_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        try:
            with open(FileStorage.__file_path, 'w') as f:
                temp = {}
                temp.update(FileStorage.__objects)
                for key, val in temp.items():
                    temp[key] = val.to_dict()
                json.dump(temp, f)
        except Exception as e:
            pass

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except Exception as e:
            pass

    def delete(self, obj=None):
        ''' Deletes object(obj) from the public
        class attribute __objects if found
        '''
        if obj is None:
            return
        else:
            obj_key = obj.__class__.__name__ + '.' + obj.id
            if obj_key in self.__objects:
                del self.__objects[obj_key]
                self.save()
    def close(self):
        """Calls reload() method for deserializing the JSON file to objects"""
        self.reload()

#!/usr/bin/python3
""" DBStorage Module for HBNB project """
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os


class DBStorage():
    """ DataBase class """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize DBStorage instance """
        user = os.getenv('HBNB_MYSQL_USER')
        pswd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        conn_str = 'mysql+mysqldb://{}:{}@{}:3306/{}'
        self.__engine = create_engine(
                conn_str.format(user, pswd, host, dg),
                pool_pre_ping=True
                )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query a session
        """
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        object_dict = {}
        if cls == None:
            class_list = [User, State, City, Amenity, Place, Review]
            for class_ in class_list:
                query = self.__session.query(class_).all()
                for row in query:
                    key = class_.__class__.__name__ + '.' + class_.id
                    object_dict[key] = dict(row)
        else:
            object_dict = dict(self.__session.query(cls).all())
        return object_dict

    def new(self, object_):
        """Add object to the current database session
        """
        self.__session.add(object_)

    def save(self):
        """Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, object_=None):
        """Delete object from the current database session
        """
        if obj is not None:
            self.__session.delete(object_)

    def reload(self):
        """Create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()

#!/usr/bin/python3
"""This module contains class DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City


valid_instances = (City, State, User, Place, Review, Amenity)


class DBStorage:
    """Class DBStorage is a SQL storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all instances of a class or all classes."""
        obj_dict = {}

        if cls is None:
            for inst in valid_instances:
                for obj in self.__session.query(inst):
                    obj_dict["{}.{}".format(inst.__name__, obj.id)] = obj
        elif cls in valid_instances:
            for obj in self.__session.query(cls):
                obj_dict["{}.{}".format(cls.__name__, obj.id)] = obj
        return obj_dict

    def new(self, obj):
        """Adds an object to the db"""
        if type(obj) in valid_instances:
            self.__session.add(obj)

    def save(self):
        """Commits the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from current session"""
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads tables from the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
             expire_on_commit=False))

    def close(self):
        """ Calls remove() on self.__session. """
        self.__session.remove()

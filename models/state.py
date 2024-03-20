#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models
from sqlalchemy.orm import relationship
from models.city import City
import sqlalchemy

class State(BaseModel, Base):
    """ State class """
    if models.storage_t == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """intialization"""
        super.__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """ getter for lists of cities instances"""
            cityList = []
            allCities = models.storage.all(City)
            for city in allCities.values():
                if city.state_id == self.id:
                    cityList.append(city)
            return cityList

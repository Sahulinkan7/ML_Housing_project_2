from housing.exception import HousingException
from housing.logger import logging
import os,sys

class ModelFactory:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
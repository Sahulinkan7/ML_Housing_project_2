from housing.exception import HousingException
from housing.logger import logging
import sys

from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    try:
        # raise Exception("we are testing this exception")
        logging.info(f"we are testing this log")
        return "haha"
    except Exception as e:
        raise HousingException(e,sys) from e

app.run(debug=True)
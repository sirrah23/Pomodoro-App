import logging
from logging.handlers import RotatingFileHandler


def getHandler():
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    return handler

from fastapi import FastAPI
import logging
from logging.config import dictConfig

def setup_logging():
    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": logging.INFO,
            },
        },
        "loggers": {
            "uvicorn": {
                "handlers": ["console"],
                "level": logging.INFO,
                "propagate": False,
            },
            "myapp": {
                "handlers": ["console"],
                "level": logging.INFO,
                "propagate": False,
            },
        },
    })

app = FastAPI()

setup_logging()
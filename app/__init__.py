from flask import Flask
import logging
import sys

app = Flask(__name__)
app.config.from_object('config')
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

from app import views
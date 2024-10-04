"""
Файл для з'єдняння роутерів з об'єктом класу Flask
"""

from flask import (
    Flask
)

app = Flask(__name__) # Об'єкт класу Flask

from app.routes import *

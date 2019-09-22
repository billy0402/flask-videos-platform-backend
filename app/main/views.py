from flask import render_template

from . import main
from ..models import *


@main.route('/')
def index():
    return render_template('index.html')
